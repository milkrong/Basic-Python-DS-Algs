student_number, operation_number = [int(x) for x in input().split()]
scores = [int(x) for x in input().split()]
for _ in range(operation_number):
    operation, a, b = input().split()
    if operation == "Q":
        a, b = int(a), int(b)
        if a == b:
            print(scores[a-1])
        print(max(scores[a-1:b]))
    else:
        a, b = int(a), int(b)
        scores[a] = b