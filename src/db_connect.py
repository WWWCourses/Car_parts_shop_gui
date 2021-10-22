from configparser import ConfigParser
import mysql.connector as mc


def db_connect():
    mydb = mc.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database'])
    return mydb


def read_db_config(filename='config.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)
    try:
        host = parser['mysql']['host']
        user = parser['mysql']['user']
        password = parser['mysql']['password']
        db = parser['mysql']['database']
        db_config = {}
        if parser.has_section(section):
            items = parser.items(section)
            for item in items:
                db_config[item[0]] = item[1]
        else:
            raise Exception(f'{section} not found in the {filename} file')
        return host, user, password, db
    except Exception as e:
        print(f'Error: {e}. Using default mysql config!')
        return {
            'host':'localhost',
            'user':'root',
            'password':'1234',
            'database':'car_parts_gui'
        }





db_config = read_db_config()
