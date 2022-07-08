import random

curNum = 0
num = 0

playerA = "computer"
playerB = "player"

def brGame(player):
    global curNum
    global num
    if player == "computer":
        num = random.randint(1, 3)
    if player == "player":
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
    for _ in range(1, num+1):
        curNum += 1
        print(f"{player} : {curNum}")
        if(curNum == 31):
            return False

while(1):
    a = brGame(playerA)
    if a == False :
        print(f"{playerB} win!")
        break;
    b = brGame(playerB)
    if b == False :
        print(f"{playerA} win!")
        break;
    
