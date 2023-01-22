def solution(statues):
    high = max(statues)
    low = min(statues)
    tempArr = []
    for i in range(low,high):
        tempArr.append(i)
    for i in range(len(statues)):
        if statues[i] in tempArr:
            tempArr.remove(statues[i])
    print(tempArr)

solution([6,2,3,8])