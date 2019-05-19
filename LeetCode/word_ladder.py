import collections

class Solution(object):
    def ladder_length(self, begin_word, end_word, word_list):
        word_list = set(word_list)
        queue = collections.deque([begin_word, 1])

        while queue:
            word, length = queue.popleft()
            if word == end_word:
                return length
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[i:] + c + word[i+1:]
                    if new_word in word_list:
                        word_list.remove(new_word)
                        queue.append([new_word, length+1])

        return 0