'''create a nxn matrix manual input numbers 
num=input("Enter 9 numbers with space:").split()
if len(num)!=9:
    print("Enter exactly 9 numbers:")
else:
    numbers=[int(x) for x in num]
    matrix=[[numbers[i*3+j] for j in range(3)] for i in range(3)]
    transpose=[[matrix[i][j] for i in range(3)] for j in range(3)]
for r in matrix:
    print(r)         
for r  in transpose:
    print(r)'''
n=int(input("Enter size:"))    
num=[int(x) for x in input("Enter numbers").split()[:n*n]]
matrix=[[2  if num[i*n+j] %2==0 else 1 for j in range(n)] for i in range(n)]
for k in matrix:
    print(k)
