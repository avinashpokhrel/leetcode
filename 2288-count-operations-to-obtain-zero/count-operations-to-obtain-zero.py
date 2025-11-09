class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ops = 0
        
        while not (num1 == 0 or num2 == 0):
            if num1 == num2:
                num1, num2 = num1 - num2, num2 - num1
            elif num1 > num2:
                num1 -= num2
            elif num2 > num1:
                num2 -= num1
            
            ops += 1

        return ops