def minimum_box(apple,box):
    total_apple=sum(apple)
    box_number=0
    box.sort(reverse=True)
    for i in box:
        total_apple-=i
        box_number+=1
        if total_apple<=0:
            break
    return box_number
apple=[2,1,4]
box=[5,8,1]
print(minimum_box(apple,box))
