class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        n = len(beginWord)
        neighboring = defaultdict(list)
        wildcards = defaultdict(list)

        if endWord not in wordList:
            return 0

        # wordList.append(beginWord)
        for word in wordList + [beginWord]:
            for i in range(n):
                state = word[:i] + "*" + word[i + 1 : n]
                wildcards[word].append(state)
                neighboring[state].append(word)


        def get_neighbors(node: str) -> List[str]:
            neighbors = set()
            for state in wildcards[node]:
                for x in neighboring[state]:
                    if x == node:
                        continue
                    neighbors.add(x)

            return neighbors

        q = deque([(1, beginWord)])
        visited = set()

        while q:

            level, curr = q.popleft()

            # Check for goal state
            if curr == endWord:
                return level

            if curr in visited:
                continue

            visited.add(curr)

            for neighbor in get_neighbors(curr):
                if neighbor not in visited:
                    q.append((level + 1, neighbor))

        return 0

