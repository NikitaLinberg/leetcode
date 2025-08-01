class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int1, int2 = int(a, 2), int(b, 2)
        sum_int = int1 + int2
        
        return str(int(format(sum_int, '08b')))
