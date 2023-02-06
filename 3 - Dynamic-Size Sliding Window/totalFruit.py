class Solution:
    def totalFruit(self, fruits):
        window = {}
        left = 0
        maxFruits = 0
        for right in range(len(fruits)):
            if len(window) < 2:
                window[fruits[right]] = window.get(fruits[right], 0) + 1
                maxFruits = max(maxFruits, right - left + 1)
            elif fruits[right] in window:
                window[fruits[right]] += 1
                maxFruits = max(maxFruits, right - left + 1)
            else:
                while len(window) == 2:
                    window[fruits[left]] -= 1
                    if window[fruits[left]] == 0:
                        del window[fruits[left]]
                    left += 1
                window[fruits[right]] = 1
        return maxFruits
        
# Official solution

class Solution:
    def totalFruit(self, fruits):
        n = len(fruits)

        windowStart = 0
        basket = {}
        maxFruits = 0

        for windowEnd in range(n):
            fruit = fruits[windowEnd]

            if fruit not in basket:
                basket[fruit] = 1

                while len(basket) > 2:
                    fruitToRemove = fruits[windowStart]
                    basket[fruitToRemove] -= 1

                    if basket[fruitToRemove] == 0:
                        del basket[fruitToRemove]

                    windowStart += 1
            else:
                basket[fruit] += 1

            maxFruits = max(maxFruits, windowEnd - windowStart + 1)

        return maxFruits
