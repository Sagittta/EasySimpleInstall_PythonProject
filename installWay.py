import pymysql

import language
import program
import guitar
import star

class installWay :
    la = language.Language()
    pr = program.Program()
    gu = guitar.Guitar()
    st = star.Star()

    def select_first(self) :
        while True :
            print("1 : 언어 설치, 2 : 프로그램 설치, 3 : 기타, 4 : 별점 주기, 0 : 종료")
            # 언어 설치 : 자바, 파이썬, 제이쿼리 / 기타 : 패스 설정 (자바, 파이썬), 이클립스-톰캣 서버 연결
            a1 = int(input(" : "))
            if a1 == 1:
                self.la.select_lan()
            elif a1 == 2:
                self.pr.select_pro()
            elif a1 == 3:
                self.gu.select_gui()
            elif a1 == 4:
                self.st.select_sta()
            elif a1 == 0:
                break
            else :
                print("잘못된 입력입니다.")

iw = installWay()
iw.select_first()