class Solution(object):
    def buy_coupons(self, coupons):
        cp_dict = {}
        min_coup = len(coupons) + 1
        for i, v in enumerate(coupons):
            if v in cp_dict.keys():
                min_coup = min(min_coup, i - cp_dict[v] + 1)
            else:
                cp_dict[v] = i

        return min_coup if min_coup < len(coupons) + 1 else -1

s = Solution()
res = s.buy_coupons([2,4,5,4,3,5,1])
print(res)