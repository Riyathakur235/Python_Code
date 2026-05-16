arr =[10,5,10,15,10,5]
n=6
freq={}
for i in range(n):
    freq[arr[i]] = freq.get(arr[i], 0) + 1

for auto in freq:
    print(auto ,"->",freq[auto])
print(freq)
