from configparser import ConfigParser
import mysql.connector as mc


def db_connect(db_config):
    mydb = mc.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database'])
    return mydb


def read_db_config(filename='config.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)

    db_config = {}

    if parser.has_section(section):
        items = parser.items(section)

        for item in items:
            db_config[item[0]] = item[1]

    else:
        raise Exception(f'{section} not found in the {filename} file')

    return db_config


if __name__ == '__main__':
   db_config = read_db_config()
   db_connect(db_config)
