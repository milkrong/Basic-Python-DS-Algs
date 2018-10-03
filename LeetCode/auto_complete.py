class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.data = None
        self.rank = 0



class AutocompleteSystem:
    """
    Design a search autocomplete system for a search engine.
    Users may input a sentence (at least one word and end with a special character '#').
    For each character they type except '#', you need to return the top 3 historical hot sentences
    that have prefix the same as the part of sentence already typed.
    """
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = TrieNode()
        self.keyword = ""
        for i, sentence in enumerate(sentences):
            self.add_record(sentence, times[i])

    def add_record(self, sentence, hot):
        p = self.root
        for char in sentence:
            if char not in p.children:
                p.children[char] = TrieNode()
            p = p.children[char]
        p.is_end = True
        p.data = sentence
        p.rank -= hot

    def dfs(self, root):
        ret = []
        if root:
            if root.is_end:
                ret.append((root.rank, root.data))
            for child in root.children:
                ret.extend(self.dfs(root.children[child]))
        return ret

    def search(self, sentence):
        p = self.root
        for char in sentence:
            if char not in p.children:
                return []
            p = p.children[char]

            return self.dfs(p)

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        result = []
        if self.keyword != "#":
            self.keyword += c
            result = self.search(self.keyword)
        else:
            self.add_record(self.keyword, 1)
            self.keyword = ""

        return [item[1] for item in sorted(result)[:3]]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)