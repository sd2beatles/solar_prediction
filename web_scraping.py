import requests
import datetime
import xmltodict
import urllib.parse
import json
import sys
import pymysql
from requests.models import Response
from utilites.errors import ResponseError
from utilites.help_funciton import get_access_config

key='GUuDchm5q0ZypmKGVp8d1thIcw%2BMBuLpaEh9X7feHiw510r3uBVN8ws9nRAH52vMJndtf4QSE4%2FKL4jcK0zwZg%3D%3D'





'''
params (1) type: dictionary (2) keys : Two keys in the upper lavel consists of 'required' and 'option.
       (3) As the name implies,the 'required' key must be specified

url each domain of the public api has thier own address. 
'''
class Base(object):
    def __init__(self,params,url):
        self.params=self.validate_params(params)
        self.url=url
    
    @staticmethod
    def validate_params(params):
        assert type(params)==dict
        if 'required' not in params:
            raise ValueError("parameter must have 'required' key.")
        
        if 'option' in params:
            required,option=params['required'],params['option']
            required.update(option)
        return required 
    
    
    
    # In our params, the name of service key in the params must be provided
    def validate_url(self,service_key_name,encoding=True):
        if encoding:
            decode_key=urllib.parse.unquote(self.params[service_key_name])
            self.params[service_key_name]=decode_key
        
        response=requests.get(self.url,params=self.params)
        parsed_content=xmltodict.parse(response.content)
        result=json.loads(json.dumps(parsed_content))
        
        return result
    
    #get_access_config requires three parameters.
    #path: eneure that you type the path for the config file is sored
    #section: the main section your seeking information is located
    #ouput returns dictionary
    
    
    '''
     
    path='D:\project\solar_prediction\config\dev.ini'
    settings='mysql'


    get_access_config(path,settings,fields)
    
    '''
    def check_db_info(self,path,section):
        fields=['host','port','username','database','password']
        db_info=get_access_config(path,section,fields)
        conn=pymysql.connect(
            host=db_info['host'],
            port=int(db_info['port']),
            user=db_info['username'],
            database=db_info['database'],
            passwd=db_info['password'],
            use_unicode=True,
            charset='utf8')
        cursor=conn.cursor()
        cursor.execute('show tables')
        print(cursor.fetchall())
        
        
'''
Weather does not have proper information

class Weather(Base):
    
    
    def get_data(self, service_key_name, encoding=True):
        result=self.validate_url(service_key_name, encoding=encoding)
        
        if 'OpenAPI_ServiceResponse' in result:
            header=result['OpenAPI_ServiceResponse']['cmmMsgHeader']
            msg={'resultCode':header['returnReasonCode'],'resultMsg':header['returnAuthMsg']}
            raise ResponseError(msg)
        
        data=result['response']['body']['items']['item']
        return data

'''        

    
  
    

    
    

    
    
    
if __name__ == '__main__':
    #decode_key=urllib.parse.unquote(key)
    url="http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList"
    key='GUuDchm5q0ZypmKGVp8d1thIcw%2BMBuLpaEh9X7feHiw510r3uBVN8ws9nRAH52vMJndtf4QSE4%2FKL4jcK0zwZg%3D%3D'
    params={'required':{'serviceKey':key,
        'dataCd':'ASOS',
        'dateCd':'HR',
        'startDt':'20100101',
        'startHh':'01',
        'endDt':'20100601',
        'endHh':'01',
        'stnIds':'108'},
      'option':{"numOfRows":'1'}
        }  
    weather=Base(params=params,url=url)
    path='D:\project\solar_prediction\config\dev.ini'
    section='mysql'
    
    # collect data form database 
    # weather.check_db_info(path,section)

    
    #data=weather.get_data(service_key_name='serviceKey')
    #print(data)
    
    
    # response=requests.get(url,params=param)
    # parsed_content=xmltodict.parse(response.content)
    # # #xml--->json conversion ---> json load
    # json_string=json.loads(json.dumps(parsed_content))
    # print(json_string)