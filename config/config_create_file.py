from configparser import ConfigParser

config=ConfigParser()
# a fucntion to manage confidential inforation that you want to keep out of any public code 

config['mysql']={
    'host':'insert',
    'port':0,
    'username':'',
    'database':'',
    'password':''
}


with open('dev.ini','w') as f:
    config.write(f)



