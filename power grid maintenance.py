class Solution(object):
    def processQueries(self, c, connections, queries):
        """
        :type c: int
        :type connections: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        parent = range(c + 1)
        rank = [0] * (c + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        for u, v in connections:
            union(u, v)

        comp_members = {}
        for i in range(1, c + 1):
            r = find(i)
            comp_members.setdefault(r, []).append(i)
        for r in comp_members:
            comp_members[r].sort()
        comp_ptr = {r: 0 for r in comp_members}

        online = [False] * (c + 1)
        for i in range(1, c + 1):
            online[i] = True

        def smallest_online_in_comp(root):
            if root not in comp_members:
                return -1
            members = comp_members[root]
            p = comp_ptr[root]
            n = len(members)
           
            while p < n and not online[members[p]]:
                p += 1
            comp_ptr[root] = p
            return members[p] if p < n else -1

        ans = []
        for typ, x in queries:
            if typ == 1:
                if online[x]:
                    ans.append(x)
                else:
                    ans.append(smallest_online_in_comp(find(x)))
            else:  
                if online[x]:
                    online[x] = False  

        return ans