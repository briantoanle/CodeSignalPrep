
# code signal first try

def solution(numbers):
    # 1 2 3 4 5
    newArr = []
    for i in range(len(numbers)-2):
        if numbers[i] < numbers[i+1] and numbers[i+1] > numbers[i+2]:
            newArr.append(1)

        elif numbers[i] > numbers[i+1] and numbers[i+1] < numbers[i+2]:
            newArr.append(1)
        else:
            newArr.append(0)
    return newArr




