
def solution(inputArray):
    max = -10000000000
    for i in range(len(inputArray)-1):
        tempMultiply = inputArray[i] * inputArray[i+1]
        if tempMultiply > max:
            max = tempMultiply
    return max

print(solution([3,6,-2,-5,7,3]))