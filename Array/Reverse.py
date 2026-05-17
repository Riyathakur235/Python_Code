def reverse(arr,l,r):
    if l>=r:
        return
    arr[l],arr[r] = arr[r],arr[l]
    reverse(arr,l+1,r-1)
    
arr=[12,56,34,65,67]
reverse(arr,0,len(arr)-1)
print("Reversed array: ",arr)    