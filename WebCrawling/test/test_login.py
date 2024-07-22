import bcrypt #pip install bcrypt
import re #정규화식
import oracledb as db 
# 사용자가 입력한 비밀번호 문자열
password_str = '1234'

# 비밀번호를 바이트로 변환
password_bytes = password_str.encode('utf-8')
# 무작위 솔트 생성
salt = bcrypt.gensalt()
#str_salt = salt.decode()
# 비밀번호 해싱
hashed_password_bytes = bcrypt.hashpw(password_bytes, salt)
class login:
    def join(id ,pw, name): # 회원가입
        bytes_pw = pw.encode('utf-8')
        bytes_salt = bcrypt.gensalt() # 무작위 솔트 생성
        bytes_hashed_pw = bcrypt.hashpw(bytes_pw, bytes_salt) # 비밀번호 해싱
        
        pattern = r'^[가-힣]{2,4}$'
        
        if re.match(pattern, name): # 이름이 한글이고, 2자 ~ 4자 일때
            try:
                con=db.connect(dsn='127.0.0.1:1521/xe',user='C##STOCK',password='1234')
                cursor=con.cursor()
                
                cursor.execute("select * from login")
                log_data = cursor.fetchall()
                for i in log_data: # 중복 방지
                    if i[2]==id and i[3]==name:
                        print('이름과 아이디가 중복됩니다.')
                        cursor.close()
                        con.close()
                        return False
  
                cursor.execute("insert into login values(:hashed_pw, :salt, :id, :name)", hashed_pw=bytes_hashed_pw, salt=bytes_salt, id=id, name=name)
       
            except db.DatabaseError as e:
                print(e)
            con.commit()
            cursor.close()
            con.close()
            return True # 정상적인 회원가입
        else:
            return False # 이름이 정규식에 해당 안 될때.

    def log(id, pw): # 로그인
        bytes_pw = pw.encode('utf-8')
        bytes_salt = bcrypt.gensalt() # 무작위 솔트 생성
        bytes_hashed_pw = bcrypt.hashpw(bytes_pw, bytes_salt) # 비밀번호 해싱
        
        try:
            con=db.connect(dsn='127.0.0.1:1521/xe',user='C##STOCK',password='1234')
            cursor=con.cursor()
            cursor.execute(f"SELECT hashed_pw, salt, id FROM LOGIN where ID = '{id}'")
            log_data = cursor.fetchall()
            
            for i in log_data:
                bytes_DB_salt = i[1].read()
                hashed_pw = bcrypt.hashpw(bytes_pw, bytes_DB_salt) # 현재 로그인 한 해싱
                bytes_DB_hashed = i[0].read() # DB에 저장된 해싱
                
                if bytes_DB_hashed == hashed_pw and i[2] == id:
                    print('로그인 되었습니다.')
                    con.commit()
                    cursor.close()
                    con.close()
                    return True
            print('해당하는 아이디, 비밀번호가 없습니다.')
        
        except db.DatabaseError as e:
            print(e)
        con.commit()
        cursor.close()
        con.close()
        
    
    #join('Hello' ,'1234', '이대환')
    join('World','5678','서현기')
    join('Robot','1357','정재환')
    #log('Hello', '1234')
    log('World','1234')
    log('World','5678')