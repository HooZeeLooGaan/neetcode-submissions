class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if flowerbed[i]:
                i += 2
            else:
                left_flowerbed = i == 0 or flowerbed[i - 1] == 0
                right_flowerbed = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
                
                if right_flowerbed and left_flowerbed:
                    flowerbed[i] = 1
                    n -= 1
                    i += 2
                
                else:
                    i += 1

        if n > 0:
            return False
        return True

            