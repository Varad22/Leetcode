class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        # for i in range(int(x/2)+1):
        #     if (i*i)<=x and ((i+1)*(i+1))>x:
        #         return i
        start=0
        end=x
        while abs(start-end)!=1:
            mid=(start+end)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                end=mid
            else:
                start=mid
        return start
