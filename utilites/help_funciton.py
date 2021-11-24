from configparser import ConfigParser, NoSectionError

from requests.api import get

class ParserError(NoSectionError):
    def __init__(self,field):
        super().__init__('Configparser does not have the section of {}'.format(field))
        
def get_access_config(path,setting,fields):
    parser=ConfigParser()
    parser.read(path)
    info={}
    for field in fields:
        try:
            value=parser.get(setting,field)
            info[field]=value
        except:
            raise ParserError(field)
    return info

path='D:\project\solar_prediction\config\dev.ini'
settings='mysql'
fields=['port','host']

data=get_access_config(path,settings,fields)
print(data)
   