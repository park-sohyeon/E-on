import sys
import os
import book1_1

class book_system:
    
    def __init__(self):
        self.library_class=book1_1.book_menu()
        self.menu()

    

#메뉴 설정
    def menu(self):
        
        print("1. 도서 추가")
        print("2. 도서 검색")
        print("3. 도서 정보 수정")
        print("4. 도서 삭제")
        print("5. 현재 총 도서 목록 출력")
        print("6. 저장")
        print("7. 프로그램 나가기")
        select=int(input("숫자를 입력하세요: "))

        if select ==1:
            self.library_class.add()
            self.menu()
        elif select ==2:
            self.library_class.search()
            self.menu()
        elif select ==3:
            self.library_class.change()
            self.menu()
        elif select ==4:
            self.library_class.delete()
            self.menu()
        elif select ==5:
            self.library_class.list_print()
            self.menu()
        elif select ==6:
            self.library_class.save()
            self.menu()
        elif select ==7:
            self.library_class.end()
        else:
            print("실행 불가능")
            print("메뉴로 돌아갑니다.")
            self.menu()



a=book_system()



    

            
