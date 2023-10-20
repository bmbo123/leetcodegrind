
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(n):
            if(((i+1) % 3 == 0) & ((i+1) % 5 == 0)):
                arr.append("FizzBuzz")
            elif((i+1) % 3 == 0):
                arr.append("Fizz")
            elif((i+1) % 5 == 0):
                arr.append("Buzz")
            else:
                arr.append(str(i+1))
        return arr