class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['isWord'] = True
        

    def search(self, word: str) -> bool:
        return self.search_helper(word, self.trie)
    # recursion
    def search_helper(self, word, node):
        cur = node
        for i, ch in enumerate(word):
            if ch not in cur:
                if ch == '.':
                    for k in cur:
                        if k != 'isWord' and self.search_helper(word[i + 1:], cur[k]):
                            return True
                # if no nodes lead to answer 
                # or the cur char != '.'
                return False
            # if char is found
            # go down to the next level
            else:
                cur = cur[ch]
        return 'isWord' in cur