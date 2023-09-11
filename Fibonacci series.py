Loop = int(input("How much Time you want to print: "))
FirstNum = 0
SecNum = 1
print(f" Fibonacci series is:", end=' ')
count = 1
while (count <= Loop):
    count += 1
    print(FirstNum, end=' ')
    Sum = FirstNum + SecNum
    FirstNum = SecNum
    SecNum = Sum

