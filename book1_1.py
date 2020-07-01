import os
import sys

class book_menu:
    def __init__(self):
        self.fileLoad()

    def fileLoad(self):
        This_Folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(This_Folder,'input.txt')

        file_input = open(my_file,'r')
        self.book_contents = file_input.readlines()
        self.booklist = []
        for i in range(len(self.book_contents)):
            self.booklist.append(self.book_contents[i].split())


    # def input_list(self):
    #     new_List=' '.join(self.book_contents)
    #     THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    #     my_file = os.path.join(THIS_FOLDER, 'input.txt')
    #     d = open(my_file,'w')
    #     d.write(new_List)
    #     d.close()
        
    #1번 메뉴
    def add(self):
        print("ex) 걷는사람 하정우 2018 문학동네 자기계발 ")
        #book_contents=[]
        userInputData = str(input("도서명 작가 출판연도 장르를 입력하세요: ")).split()
        # self.booklist = []
        # for i in range(len(userInputData)):
        self.booklist.append(userInputData)
        
        
    
    #2번 메뉴
    def search(self):
        print("1. 도서명")
        print("2. 저자")
        print("3. 출판연도")
        print("4. 출판사명")
        print("5. 장르")
        book_search=int(input("찾고 싶은 정보의 숫자를 입력하세요:"))

        if book_search ==1:
            book_name=str(input("도서명을 입력하세요:"))
            for i in range(len(self.booklist)):
                if book_name == self.booklist[i][0]:
                    print(self.booklist[i])
                    #self.menu(booklist)
        elif book_search ==2:
            book_person=str(input("저자를 입력하세요:"))
            for i in range(len(self.booklist)):
                if book_person == self.booklist[i][1]:
                    print(self.booklist[i])
                    #self.menu(booklist)
        elif book_search ==3:
            book_year=str(input("출판연도를 입력하세요:"))
            for i in range(len(self.booklist)):
                if book_year == self.booklist[i][2]:
                    print(self.booklist[i])
                    #self.menu(booklist)
        elif book_search ==4:
            book_company=str(input("출판사명을 입력하세요:"))
            for i in range(len(self.booklist)):
                if book_company == self.booklist[i][3]:
                    print(self.booklist[i])
                    #self.menu(booklist)
        elif book_search ==5:
            book_genre=str(input("장르를 입력하세요:"))
            for i in range(len(self.booklist)):
                if book_genre == self.booklist[i][4]:
                    print(self.booklist[i])
                    #self.menu(booklist)
#3번 메뉴
    def change(self):
        book_change=str(input("수정하고 싶은 정보의 도서명을 입력하세요: "))

        for i in range(len(self.booklist)):
            if book_change==self.booklist[i][0]:
                book_change_list=str(input("도서명 작가 출판연도 장르를 입력하세요: ")).split()
                del self.booklist[i]
                self.booklist.append(book_change_list)
                #self.menu(booklist)

    #4번 메뉴
    def delete(self):
        book_delete=str(input("삭제하고 싶은 정보의 도서명을 입력하세요: "))
        for i in range(len(self.booklist)):
            if book_delete==self.booklist[i][0]:
                del self.booklist[i]
                break
                #self.menu(booklist)

    #5번 메뉴
    def list_print(self):
        print(self.booklist)
        #self.menu(self.booklist)

    #6번 메뉴
    def save(self):
        This_Folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(This_Folder,'input.txt')
        newfile = open(my_file,'w')
        for k in range(len(self.booklist)):
            newfile.writelines(' '.join(self.booklist[k]))
            newfile.writelines('\n')
        newfile.close()
        # This_Folder = os.path.dirname(os.path.abspath(__file__))
        # my_file = os.path.join(This_Folder,'input.txt')

        # file_input = open(my_file,'w')
        # self.book_contents = file_input.readlines()
        # self.booklist = []

    def end(self):
        print("종료합니다.")
        sys.exit()


  
    
                

