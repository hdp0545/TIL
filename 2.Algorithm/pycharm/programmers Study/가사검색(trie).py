class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.cnt = 0

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, words):
        cur = self.head
        n = len(words)
        for word in words:
            cur.cnt += 1
            if word not in cur.children:
                cur.children[word] = Node(word)
            cur = cur.children[word]
        cur.cnt += 1
        cur.data = words

    def search(self, words):
        cur = self.head
        n = len(words)
        for word in words:
            if word != '?':
                if word not in cur.children:
                    return 0
                cur = cur.children[word]
            else:
                return cur.cnt

def solution(words, queries):
    answer = []
    my_dict = {}
    for word in words:
        n = len(word)
        if n not in my_dict:
            my_dict[n] = [Trie(), Trie()]
        my_dict[n][0].insert(word)
        my_dict[n][1].insert(word[::-1])
    for query in queries:
        n = len(query)
        if n not in my_dict:
            answer.append(0)
        else:
            trie, trie_rev = my_dict[n]
            if query[-1] != '?':
                answer.append(trie_rev.search(query[::-1]))
            else:
                answer.append(trie.search(query))
    return answer