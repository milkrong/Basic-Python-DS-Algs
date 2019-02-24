class Solution(object):  
    def totalFruit(self, tree):
            count = {}
            i = res = 0
            for j, v in enumerate(tree):
                count[v] = count.get(v, 0) + 1
                while len(count) > 2:
                    count[tree[i]] -= 1
                    if count[tree[i]] == 0: del count[tree[i]]
                    i += 1
                res = max(res, j - i + 1)
            return res
s = Solution()
print(s.totalFruit([2,3,2,2,1]))