# mysql을 사용하기 위해 pymysql을 불러옵니다.
import pymysql

class Language:
    # 클래스 안에서 conn과 curs 변수를 사용하기 위해 __init__에 추가합니다.
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='pj_java', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    # mysql에서 불러온 값을 출력하는 함수입니다.
    def print_value(self):
        rows = self.curs.fetchone()
        print("")
        for a in rows:
            print(rows[a])
        print("-------")
        print("")

    # 각 목적에 맞게 알맞은 데이터베이스를 꺼내오도록 하는 함수입니다.
    def select_lan(self):
        while True:
            print("설치할 언어를 선택하세요\n1 : Java, 2 : Python, 3 : JQuery, 0 : Exit")
            la = int(input(": "))
            
            if la == 1 :
                sql = "select * from installway where proname=%s"
                self.curs.execute(sql, ('java'))
                self.print_value()

            elif la == 2 :
                sql = "select * from installway where proname=%s"
                self.curs.execute(sql, ('python'))
                self.print_value()

            elif la == 3 :
                sql = "select * from installway where proname=%s"
                self.curs.execute(sql, ('JQuery'))
                self.print_value()
                
            elif la == 0 :
                break
            else :
                print("잘못된 입력입니다. 다시 입력해주세용\n")
    
        self.conn.close()

# la = Language()
# la.select_lan()