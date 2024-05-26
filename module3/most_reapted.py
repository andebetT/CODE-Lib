#Boyer-Moore Majority vote algorithm
def finding_mostreapeted(array):
    count=0
    candidate=None
    for num in array:
        if count==0:
            candidate=num
        count+=1 if candidate==num else -1
    return candidate
ar=[2,2,1,1,1,2,2]
print(finding_mostreapeted(ar))
