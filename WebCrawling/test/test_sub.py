import FinanceDataReader as fdr # pip install finance-datareader 설치 
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet     #pip install prophet 설치 
from datetime import datetime
import oracledb as db 
from prophet.plot import plot_components

class graf:
    def creat_plot(): 
        try:
            con = db.connect(dsn="127.0.0.1:1521/xe", user="C##STOCK", password="1234")
            cursor = con.cursor() 
                   
            now=datetime.now()
            
            GS = fdr.DataReader('022100','2024-01-01',now.strftime('%Y-%m-%d'))#20240101~현재 데이터 가져오기
            df = pd.DataFrame({'ds':GS.index,'y':GS['Close']})
            Day=now.strftime('%Y-%m-%d')
            Today=df.index.get_loc(Day)
            
            m = Prophet()
            m.fit(df)
            future = m.make_future_dataframe(periods=6,freq='ME',include_history='False')#30일후 예측 
            forecast = m.predict(future)
            
            fig = plt.figure(figsize=(12, 6))
            ax = fig.add_subplot(311) 
            ax.plot(forecast['ds'][Today:], forecast['yhat'][Today:], label='pred(6Mouth)', color='red', linewidth=5.0)
            ax.set_title("6Mouth")
            ax.set_xlabel('Date')
            ax.set_ylabel('stock price')
            ax.legend()
            
            future = m.make_future_dataframe(periods=7,freq='d',include_history='False')
            forecast = m.predict(future)
            
            ax = fig.add_subplot(313)
            ax.plot(forecast['ds'][Today:], forecast['yhat'][Today:], label='pred(7Day)', color='red', linewidth=5.0)
            ax.set_title("7Day")
            ax.set_xlabel('Date')
            ax.set_ylabel('stock price')
            ax.legend()

            #plt.show()
            
            


            con.commit
            cursor.close
            con.close
        except db.DatabaseError as e:
            print(e)
        return fig
        
        
       
        
    
        
        
       
        
        
       