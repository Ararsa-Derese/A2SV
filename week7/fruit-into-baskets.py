class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        right = 0
        left = 0
        fruit = 0
        mp = {}

        while right < len(fruits):
            if fruits[right] not in mp:
                if len(mp) == 2:
                    ind = right - 1
                    temp = fruits[ind]
                    while ind >= 0:
                        if fruits[ind] != temp:
                            del mp[fruits[ind]]
                            break
                        ind -= 1
                    left = ind + 1
                mp[fruits[right]] = 1
            right += 1
            fruit = max(fruit, right - left)

        return fruit