students_info = {}

class AlreadyExistName(Exception):
    def __init__(self):
        super().__init__('Already exist name!')

class NoStudentData(Exception):
    def __init__(self):
        super().__init__('No student data!')

class NotGetGrade(Exception):
    def __init__(self):
        super().__init__('There is a student who didn\'t get grade.')

##############  menu 1
def Menu1(name, mid_score, final_score) :
    #사전에 학생 정보 저장하는 코딩 
    students_info[name] = [mid_score, final_score]

##############  menu 2
def Menu2() :
    #학점 부여 하는 코딩
    for scores in students_info.values():
        if len(scores) == 2:
            avg = (scores[0] + scores[1]) / 2
            if avg >= 90:
                scores.append('A')
            elif avg >= 80:
                scores.append('B')
            elif avg >= 70:
                scores.append('C')
            else:
                scores.append('D')

##############  menu 3
def Menu3() :
    #출력 코딩
    headBar = "-"*32
    head = "name" + " "*7 + "mid" + " "*4 + "final" + " "*4 + "grade"
    print(headBar)
    print(head)
    print(headBar)

    for name, scores in students_info.items():
        info = f"{name}" + " "*(10-len(name)) + " "*(4-len(str(scores[0]))) + f"{scores[0]}" + " "*(9-len(str(scores[1]))) + f"{scores[1]}" + " "*7 + f"{scores[2]}"
        print(info)

##############  menu 4
def Menu4(name):
    #학생 정보 삭제하는 코딩
    del students_info[name]


#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")

    if choice == "1":
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수)
        try:
            name, mid_score, final_score = input("Enter name mid-score final-score : ").split()
        except ValueError:
            print("Num of data is not 3!")
        else:
            #예외사항 처리(입력 점수 값이 양의 정수인지)
            try:
                mid_score = int(mid_score)
                final_score = int(final_score)
                #예외사항 처리(이미 존재하는 이름)
                if name in students_info:
                    raise AlreadyExistName
            except ValueError:
                print("Score is not positive integer!")
            except AlreadyExistName as e:
                print(e)
            else:
                #예외사항이 아닌 입력인 경우 1번 함수 호출 
                Menu1(name, mid_score, final_score)
        
    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        try:
            if students_info == {}:
                raise NoStudentData
        except NoStudentData as e:
            print(e)
        else:
            #예외사항이 아닌 경우 2번 함수 호출
            Menu2()
            #"Grading to all students." 출력
            print("Grading to all students.")
    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무)
        try:
            if students_info == {}:
                raise NoStudentData
            #예외사항 처리(저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
            for scores in students_info.values():
                if len(scores) != 3:
                    raise NotGetGrade
        except NoStudentData as e:
            print(e)
        except NotGetGrade as e:
            print(e)
        else:
            #예외사항이 아닌 경우 3번 함수 호출
            Menu3()
    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        try:
            if students_info == {}:
                raise NoStudentData
        except NoStudentData as e:
            print(e)
        else:
            #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
            delName = input("Enter the name to delete : ")
            if delName not in students_info:
                #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
                print('Not exist name!')
            else:       
                #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
                Menu4(delName)
                print(f"{delName} student information is deleted")

    elif choice == "5" :
        #프로그램 종료 메세지 출력
        print("Exit Program!")
        #반복문 종료
        break
    else :
        #"Wrong number. Choose again." 출력
        print("Wrong number. Choose again.")