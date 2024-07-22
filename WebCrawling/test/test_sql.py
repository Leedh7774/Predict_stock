import oracledb as db # 오라클 데이터베이스

class DB_data:
    try:
        con = db.connect(dsn="127.0.0.1:1521/xe", user="C##STOCK", password="1234")
        cursor = con.cursor() # DB상호작용 메소드

        select_table = cursor.execute("Select * from stock_data") # JDBC를 통해 sql에 Select 작업

        for row in select_table: #for 문으로 select_table의 리스트 읽기
            print(row)
    except db.DatabaseError as e:
        print(e)

    con.commit()
    cursor.close()
    con.close()
    
    
    

    