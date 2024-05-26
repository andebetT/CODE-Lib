#longest increasing sub array
def longest_subarray(arrr):
    pos=0
    result=0
    for i in range(0,len(arrr)):
        if arrr[i]<arrr[i-1]:
            pos=i
        result=max(result,i-pos+1)

    return result
a=[1,2,3,1,3,2]
print(longest_subarray(a))
def option_two(list2):
    q=0
    for i in range(len(list2)):
        for j in range(len(list2)):
            if j >0 and list2[j]<list2[j-1]:
                i=j
            q=max(q,j-i+1)
    return q
print(option_two(a))
#the smallest sub array size those sum eqal or greater the certain value
def smallest_sub_array_size(array,traget):
    p=0
    z=100
    for i in range(len(array)):
        x=0
        for j in range(i,len(array)):
            x+=array[j]
            if x>=traget:
                z=min(z,j-i+1)
                break
    return z
at=[1,2,3,4,5,6,7]
print(smallest_sub_array_size(at,7))
def daynamic_slaiding_window(lst,target):
    sum=0
    x1=1000
    y1=0
    for i in range(len(lst)):
        sum+=lst[i]
        while sum>=target:
            x1=min(x1,i-y1+1)
            sum-=lst[y1]
            y1+=1

    return x1
print(daynamic_slaiding_window(at,7))

def longest_palindrome_sub_string(string):
    pointer1=0
    pointer2=0
    m=len(string)
    for i in range(m):
        if i>0 and string[i]!=string[i-1]:
            m=string[pointer1:i+1]
            if m==m[::-1]:
                pointer2=max(pointer2,i-pointer1+1)
            else:
                pointer1+=1
        else:
            pointer1=i
    return pointer2
st="ANDEBET"
print(longest_palindrome_sub_string(st))
#finding the the largest sub array with given length using static window


def static_sliding_window(arrr,k):
   current_sum=sum(arrr[:k])
   maximum_val=current_sum
   for i in range(1,len(arrr)-k+1):
       current_sum=current_sum-arrr[i-1]
       current_sum=current_sum+arrr[i+k-1]
       maximum_val=max(maximum_val,current_sum)
   return maximum_val
print(static_sliding_window([1,2,3,4,5,6,7],3))






