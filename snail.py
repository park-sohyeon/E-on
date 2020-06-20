size =int(input("수를 입력하세요: ")) #배열 크기
number=0
step=1 # 증가 감소 크기
a=-1 #칸
b=0 # 줄 위치

arr = [[0]*size for i in range(size)]

def snail_List(b,a,number,step,size):
    for _ in range(1,size+1):
        number+= 1
        a+= step
        arr[b][a]= number
    size -=1
  
    for _ in range(1, size+1):
        number+=1
        b+=step
        arr[b][a]=number
    step=-step
    if size==0:
        return 0

    return snail_List(b,a,number,step,size)

snail_List(b,a,number,step,size)
for b in range(size):
    print(arr[b])


