import FinanceDataReader as fdr # pip install finance-datareader 설치 
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet     #pip install prophet 설치 
from datetime import datetime
import oracledb as db 

class graf:
    def create_plot(name):
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
                
        now=datetime.now()
        time=now.strftime('%H-%M')
        if time >='09-00' and time<='18-00': 

            GS = fdr.DataReader(code,'2024-01-01',now.strftime('%Y-%m-%d'))#20240101~현재 데이터 가져오기
            df = pd.DataFrame({'ds':GS.index,'y':GS['Close']})
            Day=now.strftime('%Y-%m-%d')
            Today=df.index.get_loc(Day)
            weekday = now.weekday()
        
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
            
            for i in range(0,5):
                if weekday==i:
                    future = m.make_future_dataframe(periods=5-i,freq='d',include_history='False')
                if weekday==5 or weekday==6:
                    return False # 주말에 어플을 켰을 때
            forecast = m.predict(future)
            
            ax = fig.add_subplot(313)
            ax.plot(forecast['ds'][Today:], forecast['yhat'][Today:], label='pred(weekday)', color='red', linewidth=5.0)
            ax.set_title("weekday")
            ax.set_xlabel('Date')
            ax.set_ylabel('stock price')
            ax.legend()

            plt.show()
            return fig
        else:
            return False # 9시 이전, 6시 이후에 어플을 켰을 때