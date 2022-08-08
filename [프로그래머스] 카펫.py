def solution(brown, yellow):
    width= 0
    height= 0
    if yellow == 1:
        return [3, 3]
    else:
        for i in range(1,yellow):
            if yellow%i==0:
                width = yellow//i
                height = i
                if brown == width*2+height*2+4:
                    break
        return [width+2, height+2]
