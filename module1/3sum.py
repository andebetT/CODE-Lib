def three_sum(arr):
    arr.sort()
    res=[]
    for i in range(len(arr)-2):
        if i>0 and arr[i]==arr[i-1]:
            continue
        l=i+1
        r=len(arr)-1
        while l<r:
            total=arr[i]+arr[l]+arr[r]
            if total<0:
                l+=1
            elif total>0:
                r-=1
            else:
                res.append([arr[i],arr[l],arr[r]])
                while l<r and arr[l]==arr[l+1]:
                    l+=1
                while l<r and arr[r]==arr[r-1]:
                    r-=1
            l+=1
            r-=1
    return res
print(three_sum([2,3,1,-3,2,-1,-3,4]))


def convertString(str):
    m=str.split()
    converted_words = [word.capitalize() for word in m]
    converted_string = ' '.join(converted_words)
    print(converted_string)
print(convertString("andebet tilahun alemu"))