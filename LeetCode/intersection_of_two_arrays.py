def intersect(nums1, nums2):
    """
    Given two arrays, write a function to compute their intersection.
    :param nums1: list
    :param nums2: list
    :return: list
    """

    nums1, nums2 = sorted(nums1), sorted(nums2)
    pt1 = pt2 = 0
    res = []

    while True:
        try:
            if nums1[pt1] > nums2[pt2]:
                pt2 += 1
            elif nums1[pt1] < nums2[pt2]:
                pt1 += 1
            else:
                res.append(nums1[pt1])
                pt1 += 1
                pt2 += 1
        except IndexError:
            break

    return res