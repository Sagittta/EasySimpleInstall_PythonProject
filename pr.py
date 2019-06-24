# import pymysql

# conn = pymysql.connect(host = 'localhost', user = 'root', password = 'mirim2' ,db = 'mydb', charset='utf8')
# # host = DB주소(localhost 또는 ip주소), user = DB id, password = DB password, db = DB명
# curs = conn.cursor()

# sql = "SELECT * FROM practice" # 실행 할 쿼리문 입력
# curs.execute(sql) # 쿼리문 실행

# rows = curs.fetchall() # 데이터 패치 / 
# # fetchall() -> 모든 데이터를 한 번에 클라이언트로 가져올 때 사용
# # fetchone() -> 한 번 호출에 하나의 row만 가져올 때 사용(많이 사용 시 호출한만큼 row 가져옴.), 
# # fetchmany(n) -> n개 만큼 데이터 가져옴.

# for i in rows :
#      print(i)

# # db연결 닫기
# conn.close()

# # 데이터 갱신 : insert/update/delete 후 commit()로 데이터 확정 갱신


import pymysql

conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='mydb', charset='utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

sql = "select * from practice where loc=%s"
curs.execute(sql, ('Korea'))

rows = curs.fetchall()
for row in rows:
    print(row)
    print(row['id'], row['name'], row['loc'])
    print("-----------")


conn.close()