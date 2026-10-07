# arr =[2,4,3,5,7,8,9]
# target = 7

# def find_pairs(arr,target):
#     pairs = []
    
#     for i in range(len(arr)):
#      for j in range(i+1,len(arr)):
#          if arr[i] +arr[j] == target:
#              pairs.append((arr[i] , arr[j]))
             
#     return pairs         

# print(find_pairs(arr,target))


# Pancake sorting is a problem in which we are given an array of intefers and we have to sort the array using only a specific operation called a pancake flip. A pancake flip consists of choosing an integer k and reversing the order of the first k elements of the array. We want to sort the array in as few pancake flips as possible.
def flip(v,k):
    v[:k] =v[:k][::-1]
v= [3,6,2,4,7,1,5]
for n in range(len(v), 1, -1):
    m = v.index(max(v[:n]))
    if m != n-1:
            flip(v, m+1)
            flip(v, n)
            
print(v)            
