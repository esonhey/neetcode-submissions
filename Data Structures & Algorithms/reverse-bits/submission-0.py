class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        for i in range(32):
            reverse += 1 << (31 -i) if n & 1 > 0 else 0
            n >>= 1
        return reverse

        