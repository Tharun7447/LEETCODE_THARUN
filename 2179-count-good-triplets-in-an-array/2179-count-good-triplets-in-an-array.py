class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 2)
        self.n = size + 2

    def update(self, i, delta):
        i += 1
        while i < self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        pos2 = {val: i for i, val in enumerate(nums2)}

        index_in_pos2 = [pos2[val] for val in nums1]

        left_tree = FenwickTree(n)
        right_tree = FenwickTree(n)

        for i in index_in_pos2:
            right_tree.update(i, 1)

        result = 0
        for idx in index_in_pos2:
            right_tree.update(idx, -1)
            left_count = left_tree.query(idx - 1)
            right_count = right_tree.query(n - 1) - right_tree.query(idx)
            result += left_count * right_count
            left_tree.update(idx, 1)

        return result
