class Solution:
    def minDominoRotations(self, tops, bottoms):
        def check(x):
            rotations_top = rotations_bottom = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')
                elif tops[i] != x:
                    rotations_top += 1
                elif bottoms[i] != x:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)

        rotations = min(check(tops[0]), check(bottoms[0]))
        return -1 if rotations == float('inf') else rotations
