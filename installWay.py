# 2417 전은정

# 이지심플인스톨 프로젝트는 쉽고 간편하게 프로그램 및 개발 언어를 설치하고, 
# 환경 변수 및 서버 연결하는 방법을 알려주는 프로그램입니다.
# 별점 기능 및 보완할 부분을 입력할 수 있도록 하여, 프로그램 업데이트가 가능하도록 하였습니다.

# mysql과 연동하여 사용하기 위해 pymysql을 불러옵니다.
import pymysql

# 파일의 함수를 사용하기 위해 제가 만든 파일을 불러옵니다.
import language
import program
import guitar
import star

class installWay :
    # 함수를 사용하기 위해 객체를 생성합니다.
    def __init__(self):
        self.la = language.Language()
        self.pr = program.Program()
        self.gu = guitar.Guitar()
        self.st = star.Star()

    # 이 함수는 계속 반복하여 실행되어 언어 설치, 프로그램 설치, 기타에 계속 접속할 수 있습니다.
    def select_first(self) :
        while True :
            print("1 : 언어 설치, 2 : 프로그램 설치, 3 : 기타, 4 : 별점 주기, 0 : 종료")
            a1 = int(input(" : "))
            # if문을 이용하여 각 목적에 맞게 함수를 불러오도록 했습니다.
            if a1 == 1:
                self.la.select_lan()
            elif a1 == 2:
                self.pr.select_pro()
            elif a1 == 3:
                self.gu.select_gui()
            elif a1 == 4:
                self.st.select_sta()
                break
            elif a1 == 0:
                break
            else :
                print("잘못된 입력입니다.")

# 함수가 실행되도록 하기 위해 객체를 생성하고, 함수를 불러옵니다.
iw = installWay()
iw.select_first()
