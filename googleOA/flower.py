def solution(plants, capacity):
    # write your code in Python 3.6
    step = 0 
    
    refill  = capacity
    for plant in plants:
        if capacity < plant:
            step += step*2
            capacity = refill
        step += 1
        capacity -= plant
    
    return step

print(solution([2, 4, 5, 1, 2], 6))