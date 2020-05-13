n=int(input("작업의 수: "))
m=int(input("구할 작업 번호: "))
priority=list(map(int, input("작업 우선순위: ").split()))
number=list(range(len(priority)))
number[m]= "cheak"

time=0
while True:
    if priority[0]==max(priority):
        time+=1
        if number[0]=="cheak":
            print(time,"분")
            break
        else:
            priority.pop(0)
            number.pop(0)
    else:
        priority.append(priority.pop(0))
        number.append(number.pop(0))