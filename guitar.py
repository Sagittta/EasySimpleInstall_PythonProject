import pymysql

class Guitar:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='pj_java', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def print_value(self):
        rows = self.curs.fetchone()
        print("")
        for a in rows:
            print(rows[a])
        print("-------")
        print("")

    def select_gui(self):
        while True:
            print("1 : 환경변수 설정, 2 : 리눅스 설치, 3 : Bitnami 설치, 4 : Apache Tomcat 설치, 5 : Git 설치 및 간단한 사용법, 0 : 종료")
            gu1 = int(input(": "))
            if gu1 == 0 :
                break
            elif gu1 == 1 :
                print("1 : Java 환경변수, 2 : Python 환경변수")
                gu2 = int(input(": "))
                
                if gu2 == 1 :
                    sql = "select * from installway where proname=%s"
                    self.curs.execute(sql, ('javaPath'))
                    self.print_value()
                elif gu2 == 2 :
                    sql = "select * from installway where proname=%s"
                    self.curs.execute(sql, ('pythonPath'))
                    self.print_value()
                else :
                    print("잘못 입력하셨습니다.")

            elif gu1 == 2 :
                sql = "select * from installway where proname=%s"
                self.curs.execute(sql, ('linux'))
                self.print_value()

            elif gu1 == 3 :
                sql = "select * from installway where proname=%s"
                self.curs.execute(sql, ('bitnami'))
                self.print_value()

            elif gu1 == 4 :
                sql = "select * from installway where proname=%s"
                self.curs.execute(sql, ('tomcat'))
                self.print_value()

            elif gu1 == 5 :
                sql = "select * from installway where proname=%s"
                self.curs.execute(sql, ('git'))
                self.print_value()

            else :
                print("잘못 입력하셨습니다.")
