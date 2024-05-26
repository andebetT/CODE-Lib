def format_number(num):
    if num<0:
        return False
    else:
        m=list(str(num))
        n=''
        for i in range(len(m)-3,0,-3):
            m.insert(i,',')
        for i in range(len(m)):
            n+=m[i]

    return n
print(format_number(1000000))
#method2
def format_number(number):
    return "{:,}".format(number)