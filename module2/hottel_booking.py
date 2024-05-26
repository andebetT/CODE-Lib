def hotel_booking(arrival_date,departure_date,k):
    list1=[]
    list2=[]
    for i in range(len(arrival_date)):
        list1.append((arrival_date[i],"enter"))
    for i in range(len(departure_date)):
        list2.append((departure_date[i],"exit"))
    total_list=list1+list2
    sorted_list=sorted(total_list)
    gust=0
    for i in sorted_list:
        if i[1]=="enter":
            gust+=1
        else:
            gust=gust-1
    if gust>k:
        return 0
    return 1
print(hotel_booking([1,3,5],[2,6,8],1))




