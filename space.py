# n=5
# for i in range(n):
#     for j in range(2*n-1):
#         if(i==0 or i==n-1 or j==0 or j==2*n-2 or
#             i+j==n-1 or i-j==n-1 + n):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")    
#     print()    
    

# star shape pattern
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)