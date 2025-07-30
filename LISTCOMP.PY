#list comprehension ....... input version.....
# step by step input of lc
'''nums=[int(input(f"Enter number{i+1}:"))for i in range(10)]
print(nums)'''
num=[int(x) for x  in input("Enter 5 num with space:").split()[:5]]
print(num)
'''nested lc ..... loop within loop in a single : lc'''
'''
n=int(input("Enter the table size:"))
table=[[i*j for j in range(1,n+1)] for i in range(1,n+1)]
print("Table of match")
for row in table:
    print(row)'''
