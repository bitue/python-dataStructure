arr= [12,65,2,89,12,6,67,33];


def bouble_sort (arr) :
    for i in range (0, len(arr)) :
        flag = False;

        for j in range (i+1 , len(arr)):
            if arr[i] > arr[j] :
                [arr[i], arr[j]] = [arr[j], arr[i]]
                flag = True;
        if (not flag) :
            return  arr ;

    return  arr ;



res = bouble_sort(arr)
print(res)