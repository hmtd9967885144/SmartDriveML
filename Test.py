import configparser

config = configparser.ConfigParser()
config.read_file(open(r'Config.txt'))
path1 = config.get('My Section', 'path1')
path2 = config.get('My Section', 'path2')
path3 = config.get('My Section', 'path3')

print(path1,path2,path3)