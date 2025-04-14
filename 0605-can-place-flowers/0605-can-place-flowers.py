class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            if flowerbed[i] == 0:
                if i != 0:
                    if flowerbed[i+1] == 1 or flowerbed[i-1] == 1:
                        continue
                    else:
                        flowerbed[i] = 1
                        n -= 1
                else:
                    if flowerbed[i+1] == 1:
                        continue
                    else:
                        flowerbed[i] = 1
                        n -= 1
        print(flowerbed)
        print(n)
        return n == 0 