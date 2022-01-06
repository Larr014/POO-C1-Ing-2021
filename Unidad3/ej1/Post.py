class Post:
    
    def __init__(self,userId,id,title,body):
        self.__userId = userId
        self.__id = id
        self.__title = title
        self.__body = body
        
    def get_userId(self):
        return self.__userId
    
    def get_id(self):
        return self.__id
    
    def get_title(self):
        return self.__title
    
    def get_body(self):
        return self.__body
    
    def set_userId(self,userId):
        self.__userId = userId
        
    def set_id(self,id):
        self.__id = id
        
    def set_title(self,title):
        self.__title = title
        
    def set_body(self,body):
        self.__body = body
        
    def mostrar(self):
        print('----Post----')
        print(f'User Id: {self.__userId}')
        print(f'ID: {self.__id}')
        print(f'Title {self.__title}')
        print(f'Body: {self.__body}')