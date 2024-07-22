import FinanceDataReader as fdr
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
import oracledb as db

class real_plot:
    def data(name):
        try:
            con = db.connect(dsn="127.0.0.1:1521/xe", user="C##STOCK", password="1234")
            cursor = con.cursor() 
            
            cursor.execute(f"select code from stock where id = '{name}'")
            stock_data = cursor.fetchall()
            code = stock_data[0][0]
        
            con.commit
            cursor.close
            con.close
        except db.DatabaseError as e:
            print(e) 
                        
        reality=datetime.now()
        now=datetime.now()-timedelta(days=30)
        
        R=reality.strftime('%Y-%m-%d')
        
        N=now.strftime('%Y-%m-%d')
        
        GS = fdr.DataReader(code,N,R)
        
        x=GS.index
        y=GS['Close']
        
       
        del GS['Change']
        
        return x,y,GS
    