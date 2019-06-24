import pymysql
import math

class Star :
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='pj_java', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        self.st2 = ""

    def select_sta(self):
        print("-------")
        st1 = int(input("별점의 개수를 입력해주세요. (1 ~ 10) \n : "))
        if st1 < 11 and st1 > 0:
            print("-------")
            print("★"*st1)
            print("-------")
            if st1 < 5:
                print("보완할 점을  입력해주세요.(1: Yes, 2: No)")
                st = int(input(": "))
                if st == 2:
                    print("감사합니다.")
                elif st == 1:
                    self.st2 = input("입력 : ")
                    print("감사합니다. 추후 업데이트에 반영하겠습니다.")
                else:
                    print("잘못 입력하셨습니다.")
            else:
                print("감사합니다 !")
        elif st1 > 10 or st1 < 0:
            print("1 ~ 10으로 다시 입력해주세요.")
            st1 = int(input(": "))
            if st1 < 11 and st1 > 0:
                print("★"*st1)
            else:
                print("프로그램이 종료됩니다.")
        else:
            print("프로그램이 종료됩니다.")

        sql = "insert into star2(count, comment) values (%s, %s)"
        self.curs.execute(sql, (st1, self.st2))

        self.conn.commit()

        sql = "select avg(count) from star2"
        self.curs.execute(sql)
        a = self.curs.fetchone()

        print("\n★별점주기★\n")
        print(round(a['avg(count)'], 2))
        print("-------")

        self.conn.close()

# s = Star()
# s.select_sta()