class ResponseError(ValueError):
    def __init__(self,msg):
        super().__init__('Error Code {}:{}'.foramt(msg['resultCode'],msg['resultMsg'])) 

