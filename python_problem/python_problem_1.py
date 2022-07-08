from xml.etree.ElementTree import TreeBuilder


curNum = 0
num = 0
end = False


while(1):
    while(1):
        try:
            num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
        except:
            print("정수를 입력하세요")
        else:
            if num != 1 and num != 2 and num != 3:
                print("1, 2, 3 중 하나를 입력하세요")
            else:
                break;

    for i in range(1, num+1):
        curNum += 1
        print(f"player A : {curNum}")
        if(curNum == 31):
            print("playerB win!")
            end = True
            break
    if(end):
        break

    while(1):
        try:
            num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
        except:
            print("정수를 입력하세요")
        else:
            if num != 1 and num != 2 and num != 3:
                print("1, 2, 3 중 하나를 입력하세요")
            else:
                break;

    for i in range(1, num+1):
        curNum += 1
        print(f"player B : {curNum}")
        if(curNum == 31):
            print("playerA win!")
            end = True
            break
    if(end):
        break

