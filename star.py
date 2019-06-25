# mysql을 사용하기 위해 pymysql을 불러옵니다.
# round() 함수를 사용하기 위해 math를 불러옵니다.
import pymysql
import math

class Star :
    # 클래스 안에서 conn과 curs 변수를 사용하기 위해 __init__에 추가합니다.
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='pj_java', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        self.st2 = None

    # 별점과 보완할 점을 입력할 수 있도록 하는 함수입니다.
    def select_sta(self):
        print("-------")
        st1 = int(input("\n별점의 개수를 입력해주세요. (1 ~ 10) \n : "))
        st = 0
        if st1 < 11 and st1 > 0:
            print("-------")
            print("★"*st1)
            print("-------")
            # 별이 5개 미만일 경우, 보완할 점을 입력할 수 있습니다.
            if st1 < 5:
                print("보완할 점을  입력해주세요.(1: Yes, 2: No)")
                st = int(input(": "))

                if st == 2:
                    self.st2 = None
                    print("감사합니다.")

                elif st == 1:
                    self.st2 = input("입력 : ")
                    print("감사합니다. 추후 업데이트에 반영하겠습니다.")
                else:
                    print("잘못 입력하셨습니다.")
            else:
                print("감사합니다 !")
            
            self.st2 = None
        elif st1 > 10 or st1 < 0:
            print("1 ~ 10으로 다시 입력해주세요.")
            st1 = int(input(": "))
            if st1 < 11 and st1 > 0:
                print("★"*st1)
            else:
                st1 = 0
                print("프로그램이 종료됩니다.")
        else:
            print("프로그램이 종료됩니다.")

        # 별점의 개수와 입력한 보완할 점을 데이터베이스에 넣습니다.
        sql = "insert into star2(count, comment) values (%s, %s)"
        self.curs.execute(sql, (st1, self.st2))
        self.conn.commit()

        # 별점 평균을 구하기 위해 데이터베이스에서 별점의 개수의 평균값을 가져옵니다.
        sql = "select avg(count) from star2"
        self.curs.execute(sql)
        a = self.curs.fetchone()

        print("\n★ 별점평균 ★")
        # 소숫점 2번째 자리까지 출력합니다.
        if 'avg(count)' is not None:
            print(round(a['avg(count)'], 2))
            print("-------")
        self.conn.close()

# s = Star()
# s.select_sta()