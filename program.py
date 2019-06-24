import pymysql

class Program:
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