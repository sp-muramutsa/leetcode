class Solution:
    def alienOrder(self, words: List[str]) -> str:

        adj = defaultdict(set)
        in_degree = defaultdict(int)
        for word in words:
            counter = Counter(word)
            for char in counter:
                in_degree[char] = 0

        n = len(words)
        for first_word, second_word in zip(words, words[1:]):
            for char1, char2 in zip(first_word, second_word):
                if char1 != char2:
                    if char2 not in adj[char1]:
                        adj[char1].add(char2)
                        in_degree[char2] += 1
                    break

            else:
                if len(first_word) > len(second_word):
                    return ""

        q = deque([node for node in in_degree if in_degree[node] == 0])
        top_sort = []

        while q:

            curr = q.popleft()
            top_sort.append(curr)

            for dest in adj[curr]:
                in_degree[dest] -= 1

                if in_degree[dest] == 0:
                    q.append(dest)

        if len(top_sort) < len(in_degree):
            return ""

        return "".join(top_sort)

