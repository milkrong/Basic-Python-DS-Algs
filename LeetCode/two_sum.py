def two_sum(numbers, target):

    i, j = 0, len(numbers) - 1

    while i < j:
        sum = numbers[i] + numbers[j]
        if sum == target:
            return (i+1,j+1)
        elif sum < target:
            i += 1
        else:
            j -= 1

    return None

#test
numbers = [1,2,3,4,5]
target = 7

print(two_sum(numbers, target))