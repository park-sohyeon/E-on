import sys
import os
import train
import reservation

class train_system:
    def __init__(self):
        self.train_contents=[]
        self.trainlist = []
        self.reslist = []
        self.fileLoad()

    def fileLoad(self):
        This_Folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(This_Folder,'TrainList.txt')
        print(my_file)
        file_input = open(my_file, 'r')
        self.train_contents = file_input.readlines()
        for l in self.train_contents[1:]:
            time,start,_,destination,traintype,seats=l.split()
            seats=int(seats)
            self.trainlist.append(train.train(time,start,destination,traintype,seats))

    def menu(self):
        while(True):
            print("------- 기차 예매시스템 ----")
            print("1. 빠른시간 기차 검색 및 예매")
            print("2. 전체 기차 리스트 출력")
            print("3. 나의 예매 현황 출력 및 예매 취소")
            print("4. 프로그램 종료")

            select = int(input("숫자를 입력하세요: "))

            if select == 1:
                self.search()

            elif select == 2:
                self.print()

            elif select == 3:
                self.cancel()

            elif select == 4:
                break
            
            else:
                print("실행 불가능")
                print("메뉴로 돌아갑니다.")
 # 1번 메뉴
    def search(self):
        time,start,destination,traintype=input("시간 출발역 도착역 열차종류를 입력하세요: ").split()
        selecttrain=-1
        for t in range(len(self.trainlist)):
            if(start==self.trainlist[t].start and destination==self.trainlist[t].destination 
               and traintype==self.trainlist[t].traintype and time<=self.trainlist[t].time and self.trainlist[t].seats>0):
                selecttrain=t
                break

        if(selecttrain!=-1):
            print("가장 빠른 열차는")
            self.trainlist[selecttrain].print()
            print("입니다.")
        else:
            print("열차가 없습니다.")
            return
       
        select=input("기차표 예매를 하겠습니까? (y/n): ").lower()

        if select == "y":
            self.trainlist[selecttrain].seats-=1
            self.trainlist[selecttrain].print()
            self.reslist.append(reservation.reservation(
                self.trainlist[selecttrain].time,
                self.trainlist[selecttrain].start,
                self.trainlist[selecttrain].destination,
                self.trainlist[selecttrain].traintype,
                1 ))

        print("예약을 종료합니다.")

    # 2번 메뉴
    def print(self):
        print("기차현황------------------")
        for t in self.trainlist:
            t.print()

    # 3번 메뉴
    def cancel(self):
        # 예매현황 출력
        print("예매현황------------------")
        for r in range(len(self.reslist)):
            if(self.reslist[r].seats==1):
                self.reslist[r].print()
       
       # 예매 취소
        select = input("예매를 취소하시겠습니까? (y/n): ").lower()
        if select == "y":
            time,start,destination,traintype = input("시간 출발역 도착역 열차종류를 입력하시오: ").split()

            selectres=-1
            for t in range(len(self.reslist)):
                if(start==self.reslist[t].start and destination==self.reslist[t].destination 
                and traintype==self.reslist[t].traintype and time==self.reslist[t].time):
                    selectres=t
            if(selectres==-1):
                print("예약내역이 없습니다.")
            else:
                self.reslist[t].seats=0
                for t in range(len(self.trainlist)):
                    if(start==self.trainlist[t].start and destination==self.trainlist[t].destination 
                    and traintype==self.trainlist[t].traintype and time==self.trainlist[t].time):
                        self.trainlist[t].seats+=1

t=train_system()
t.menu()