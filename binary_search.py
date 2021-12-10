import math
nums =[23,56,89,90,100,675]

def binary_search(arr , target):
    start = 0
    end = len(arr) -1

    while start <= end :
        mid = math.floor((start+end)/2)
        if arr[mid]> target :
            end = mid -1

        if arr[mid] < target :
           start = mid +1


        if arr[mid] == target :
            return  mid


    return -1  


selected = input('enter the target value')
res = binary_search(nums , int(selected))

print(res)