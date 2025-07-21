# Disjoint Set (Union-Find) using Union by Size and Path Compression
# -------------------------------------------------------------------------------
# This class efficiently manages a collection of disjoint sets.
# It supports three operations:
#   1. find(x): Finds and returns the representative (ultimate parent) of the set
#              that element x belongs to.
#   2. union(x, y): Merges the sets that contain x and y using union by size,
#                   minimizing tree height.
#   3. is_connected(x, y): Checks whether two elements belong to the same set.
#
# Optimization Techniques:
#   - Path Compression in find(): Collapses the path during find so future lookups are faster.
#   - Union by Size in union(): Always attach the smaller tree to the larger one to keep
#                               the overall height minimal.
# -------------------------------------------------------------------------------

class DisjointSet:
    def __init__(self, size):
        # Each node is initially its own parent (self-loop)
        self.parent = [i for i in range(size)]
        # Initialize each set with size 1
        self.size = [1] * size

    def find(self, x):
        # Path Compression: Recursively find root and compress path
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find roots of the sets to which x and y belong
        rootX = self.find(x)
        rootY = self.find(y)

        # If they already belong to the same set, return False (no merge)
        if rootX == rootY:
            return False

        # Union by Size: Attach the smaller tree to the larger tree
        if self.size[rootX] < self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]

        return True  # Merge was successful

    def is_connected(self, x, y):
        # Return True if x and y are in the same set
        return self.find(x) == self.find(y)

# ---------------------------------------------------------------------------------
# Time and Space Complexity:
#
# Time Complexity:
#   - find(x): O(α(n)) — where α(n) is the inverse Ackermann function (very slow-growing),
#             effectively considered as constant time for all practical purposes.
#   - union(x, y): O(α(n)) — due to path compression and union by size.
#   - is_connected(x, y): O(α(n)) — since it relies on find().
#
# Space Complexity:
#   - O(n) — where n is the number of elements. Space is used by:
#           - parent[] array to track the parent of each node.
#           - size[] array to track the size of each disjoint set.
# ---------------------------------------------------------------------------------
