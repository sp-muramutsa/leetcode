class DSU:
    def __init__(self):
        self.parents = {}
        self.sizes = {}

    def find(self, node):
        """
        Find with path compression
        """

        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])

        return self.parents[node]

    def union(self, node1, node2):
        """
        Union with size heuristic
        """

        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return

        size1 = self.sizes[parent1]
        size2 = self.sizes[parent2]

        if size1 > size2:
            self.parents[parent2] = parent1
            self.sizes[parent1] += self.sizes[parent2]
        else:
            self.parents[parent1] = parent2
            self.sizes[parent2] += self.sizes[parent1]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        dsu = DSU()
        components = []
        names = {}
        n = len(accounts)
        for i, account in enumerate(accounts):
            dsu.parents[i] = i
            dsu.sizes[i] = 1
            names[i] = account[0]

        seen = {}
        for i in range(n):
            for email in accounts[i][1:]:
                if email not in seen:
                    seen[email] = i
                else:
                    dsu.union(seen[email], i)

        # Make each component point to its oldest ancestor
        for component in dsu.parents:
            dsu.parents[component] = dsu.find(component)

        merged = defaultdict(list)
        for child, parent in dsu.parents.items():
            merged[parent].extend(accounts[child][1:])

        result = []
        for idx, emails in merged.items():
            name = names[idx]
            account_emails = sorted(set(emails))
            result.append([name] + account_emails)

        return result

