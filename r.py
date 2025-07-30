n=int(input("Enter rows:"))
upper=[' '*(n-i)+''.join('*' if j==0 or j==2*i else ' ' for j in range(2*i+1)) for i in range(n)]
lower=[' '*(i+2)+''.join('*' if j==0 or j==2*(n-i-2)else ' ' for j in range(2*n-i-1)) for i in range(n-1)]
for line in upper+lower:
    print(line)