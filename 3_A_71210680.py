input = input("Input : ")
count = len(input)
print("Output : ",end="")
for i in range(0, count, 1):
    for j in range(0, i, 1):
        print(input[j] , end='')
    print('')
for i in range(count,0,-1):
    for j in range(0, i):
        print(input[j] , end='')
    print('')