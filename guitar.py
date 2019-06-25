# mysql을 사용하기 위해 pymysql을 불러옵니다.
import pymysql

class Guitar:
    # 클래스 안에서 conn과 curs 변수를 사용하기 위해 __init__에 추가합니다.
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='pj_java', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        self.sql = ""

    # mysql에서 불러온 값을 출력하는 함수입니다.
    def print_value(self):
        rows = self.curs.fetchone()
        print("")
        print("-------")
        for a in rows:
            if rows[a] is None:
                break
            print(rows[a])
        print("-------")
        print("")

    # select 명령어를 줍니다.
    def select_sql(self):
        self.sql = "select * from installway where proname=%s"

    # 각 목적에 맞게 알맞은 데이터베이스를 꺼내오도록 하는 함수입니다.
    def select_gui(self):
        while True:
            print("\n1 : 환경변수 설정, 2 : 리눅스 설치, 3 : Bitnami 설치, 4 : Apache Tomcat 설치, 5 : Git 설치 및 간단한 사용법, 0 : 종료")
            gu1 = int(input(": "))
            if gu1 == 0 :
                break
            # 환경변수 종류를 자바와 파이썬으로 나누어 알고 싶은 정보에 더 가까이 다가갈 수 있도록 했습니다.
            elif gu1 == 1 :
                print("1 : Java 환경변수, 2 : Python 환경변수")
                gu2 = int(input(": "))
                
                if gu2 == 1 :
                    self.select_sql()
                    self.curs.execute(self.sql, ('javaPath'))
                    self.print_value()
                elif gu2 == 2 :
                    self.select_sql()
                    self.curs.execute(self.sql, ('pythonPath'))
                    self.print_value()
                else :
                    print("잘못 입력하셨습니다.")

            elif gu1 == 2 :
                self.select_sql()
                self.curs.execute(self.sql, ('linux'))
                self.print_value()

            elif gu1 == 3 :
                self.select_sql()
                self.curs.execute(self.sql, ('bitnami'))
                self.print_value()

            elif gu1 == 4 :
                self.select_sql()
                self.curs.execute(self.sql, ('tomcat'))
                self.print_value()

            elif gu1 == 5 :
                self.select_sql()
                self.curs.execute(self.sql, ('git'))
                self.print_value()

            else :
                print("잘못 입력하셨습니다.")

#   g = Guitar()
#   g.select_gui()
