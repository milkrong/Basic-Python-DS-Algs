class Solution(object):
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    """
    def longest_common_prefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        min_str = min(strs, key = len)
        for i, char in enumerate(min_str):
            for item in strs:
                if item[i] != char:
                    return min_str[:i]
                else:
                    continue
        return min_str