import psycopg2 

class Database():
    
    def __init__(self , dsn: str):
        self.dsn = dsn
        
        self.conn = self.__connect()
        self.cursor = self.conn.cursor()
        
    def __connect(self):
        try:
    
            conn = psycopg2.connect(self.dsn)
            
            return conn
        except Exception as e:
            raise Exception(e)
             
            
    def __del__(self):
            self.cursor.close()
            self.conn.close()