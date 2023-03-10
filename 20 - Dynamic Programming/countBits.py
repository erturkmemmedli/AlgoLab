class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]
        power = 0

        while n >= len(output) * 2:
            for i in range(len(output)):
                output.append(output[i] + 1)

        index = n - len(output) + 1

        for i in range(index):
            output.append(output[i] + 1)

        return output
