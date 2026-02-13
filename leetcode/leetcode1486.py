class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        answer=start
        for i in range(n-1):
            num=start+2*(i+1)
            answer=answer^num
        return answer
