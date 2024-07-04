class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        copyDigits = digits[::-1]
        if copyDigits[0]!=9:
            copyDigits[0]+=1
            return copyDigits[::-1]
        else:
            for i in range(len(copyDigits)):
                if copyDigits[i]==9:
                    copyDigits[i]=0
                else:
                    copyDigits[i]+=1
                    return copyDigits[::-1]
            return [1]+copyDigits[::-1]
