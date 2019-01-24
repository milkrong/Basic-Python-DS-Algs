class Solution(object):
    def plus_one(self, digits):

        if digits == []:  #just for case: digits = [9]
            return [1]
        if digits[-1] != 9:
            return digits[:-1]+[digits[-1]+1]
        else:
            return self.plusOne(digits[:-1])+[0]