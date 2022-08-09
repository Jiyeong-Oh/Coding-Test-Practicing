def solution(people, limit):
    count=0
    people.sort()
    lightest = 0
    heaviest = len(people)-1
    while lightest <= heaviest:
        if people[lightest]+people[heaviest]<=limit:
            lightest+=1
        count+=1
        heaviest-=1
    return count
