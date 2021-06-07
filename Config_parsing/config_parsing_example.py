import configparser

parser = configparser.ConfigParser()
parser.read('db.ini')
print(parser.get('mysql', 'host'))

