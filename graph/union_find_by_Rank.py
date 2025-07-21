"""
DisjointSet (Union-Find) Data Structure

Summary:
---------
The DisjointSet class (also known as Union-Find) is a data structure used to efficiently manage and merge disjoint sets.
It supports three primary operations:
1. `find(x)` – Determines the representative (ultimate parent) of the set containing element `x`, with path compression.
2. `union(x, y)` – Merges the sets that contain `x` and `y` using union by rank (keeps the tree shallow).
3. `is_connected(x, y)` – Checks whether elements `x` and `y` are in the same set.

This data structure is widely used in graph algorithms like Kruskal’s Minimum Spanning Tree and in detecting cycles in a graph.
"""

class DisjointSet:
    def __init__(self, size):
        # Initialize each element to be its own parent (self loop)
        self.parent = [i for i in range(size)]
        # Initialize the rank of each node to 0
        self.rank = [0] * size

    def find(self, x):
        # Find the ultimate parent of node x with path compression
        if x != self.parent[x]:
            # Recursively assign the parent of x to its root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find the ultimate parents of x and y
        ultimate_parent_of_x = self.find(x)
        ultimate_parent_of_y = self.find(y)

        # If they are already in the same set, no need to union
        if ultimate_parent_of_x == ultimate_parent_of_y:
            return False

        # Union by rank (attach the tree with lower rank to higher)
        if self.rank[ultimate_parent_of_x] < self.rank[ultimate_parent_of_y]:
            self.parent[ultimate_parent_of_x] = ultimate_parent_of_y
        elif self.rank[ultimate_parent_of_y] < self.rank[ultimate_parent_of_x]:
            self.parent[ultimate_parent_of_y] = ultimate_parent_of_x
        else:
            # If ranks are equal, choose one as parent and increment its rank
            self.parent[ultimate_parent_of_y] = ultimate_parent_of_x
            self.rank[ultimate_parent_of_x] += 1

        return True  # Union was successful

    def is_connected(self, x, y):
        # Check if x and y belong to the same set
        return self.find(x) == self.find(y)


"""
Time and Space Complexity:
--------------------------

Time Complexity (Amortized):
- find(x)        → O(α(N))
- union(x, y)    → O(α(N))
- is_connected() → O(α(N))
Where α(N) is the inverse Ackermann function (very slow-growing, nearly constant for all practical purposes).

Space Complexity:
- O(N), where N is the number of elements (for parent[] and rank[] arrays).
"""
