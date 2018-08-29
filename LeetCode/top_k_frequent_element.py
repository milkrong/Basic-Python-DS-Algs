def top_k_frequent(nums, k):
    """
    Given a non-empty array of integers, return the k most frequent elements.

    :param nums: list
    :param k: int
    :return: int
    """
    temp = {}
    for num in nums:
        if num in temp:
            temp[num] += 1
        else:
            temp[num] = 1

    bucket = [[] for _ in range(len(nums) + 1)]
    for key, val in temp.items():
        bucket[val].append(key)

    ret = []
    for row in reversed(bucket):
        if not row:
            continue
        else:
            for i in range(len(row)):
                ret.append(row[i])
                if len(ret) == k:
                    return ret
