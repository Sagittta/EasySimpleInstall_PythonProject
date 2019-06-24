# mysql을 사용하기 위해 pymysql을 불러옵니다.
import pymysql

class Program:
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
    def select_pro(self):
        while True:
            print("설치할 프로그램을 선택하세요\n1 : Android Studio, 2 : Eclipse, 3 : Pycharm, 4 : Unity, 5 : EditPlus3, 6 : Visual Studio, 0 : 종료")
            pr = int(input(": "))
            
            if pr == 0:
                break
                
            elif pr == 1:
                sql = "select * from installway where proname=%s"
                self.curs.execute(sql, ('andstudio'))
                self.print_value()

            # Eclipse를 JSP 용도로 사용하기 위해서는 기타 설정해야 할 것이 있기 때문에 두 가지 선택으로 나눴습니다.
            elif pr == 2:
                print("For Java : 1, For JSP : 2")
                pr2 = int(input(": "))

                if pr2 == 1:
                    sql = "select * from installway where proname=%s"
                    self.curs.execute(sql, ('ejava'))
                    self.print_value()

                elif pr2 == 2:
                    sql = "select * from installway where proname=%s"
                    self.curs.execute(sql, ('eJSP'))
                    self.print_value()

                else:
                    print("잘못 입력하셨습니다.")

            elif pr == 3:
                sql = "select * from installway where proname=%s"
                self.curs.execute(sql, ('pycharm'))
                self.print_value()
            
            elif pr == 4:
                sql = "select * from installway where proname=%s"
                self.curs.execute(sql, ('unity'))
                self.print_value()
            
            elif pr == 5:
                sql = "select * from installway where proname=%s"
                self.curs.execute(sql, ('editplus3'))
                self.print_value()

            # HTML 또는 Python 용도로 주로 사용하는 Visual Studio Code와 
            # C언어 개발을 용도로 주로 사용하는 Visual Studio 2019이기 때문에 두 가지 선택으로 나눴습니다.
            elif pr == 6:
                print("Visual Studio Code : 1, Visual Stduio 2019 : 2")
                pr2 = int(input(": "))

                if pr2 == 1 :
                    sql = "select * from installway where proname=%s"
                    self.curs.execute(sql, ('vscode'))
                    self.print_value()

                elif pr2 == 2 :
                    sql = "select * from installway where proname=%s"
                    self.curs.execute(sql, ('vs2019'))
                    self.print_value()

                else :
                    print("잘못 입력하셨습니다.")

            else:
                print("잘못 입력하셨습니다.")

# p = Program()
# p.select_pro()