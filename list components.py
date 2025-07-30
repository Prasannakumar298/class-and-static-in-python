'''rows=int(input("Enter rows:"))
pattern=[(' ' * (rows-i) + '*' * (2*i-1)) for i in range(1,rows+1)]
for line in pattern:
    print(line)'''
'''       rows=int(input("Enter rows:"))
pattern=[' '.join([str(num) for num in range(1, rows-i+1)]) for i in range(rows)]
for line in pattern:
    print(line)'''
n=int(input("Enter rows:"))
pattern=[['*' if i==0 or i==n-1 or j==0 or j==n-1 else ' 'for i in range(n)]for j in range(n)]
for i in pattern:
    print(' '.join(i))