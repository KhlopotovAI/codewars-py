class DynamicConnectivity(object):
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(0, n)]
        self.size = [1] * n

    def find(self, p):
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p != root_q:
            if self.size[root_p] < self.size[root_q]:
                self.parent[root_p] = root_q
            else:
                self.parent[root_q] = root_p

    def connected(self, p, q):
        return self.find(p) == self.find(q)
