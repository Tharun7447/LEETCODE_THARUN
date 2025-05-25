class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        freq = Counter(words)

        reverse = set()
        reverse_count = 0
        same_count = 0
        middle = 0
        for k, v in freq.items():
            if k != k[::-1]:
                if k not in reverse:
                    reverse_count += min(v,freq[k[::-1]])
                    reverse.add(k[::-1])
            else:
                middle |= v % 2
                same_count += v // 2
        
        return reverse_count * 4 + same_count * 4 + middle * 2
            