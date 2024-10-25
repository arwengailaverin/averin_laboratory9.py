#input digit:
num = int(input("Enter a number: "))
#create a loop "FOR": 
for i in range(5):
    for j in range(i+1):
        print(num, end=" ")
        num = num+1
    print()