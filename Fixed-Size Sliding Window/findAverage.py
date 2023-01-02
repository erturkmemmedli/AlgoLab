def findAverage(nums, k):
    windowAverage = sum(nums[:k])
    output = [windowAverage / k]
    for i in range(len(nums) - k):
        windowAverage += nums[i + k] - nums[i]
        output.append(windowAverage / k)
    return output
	
# Official solution given

def findAverage(nums, k):
    windowSum = sum(nums[:k])
    average = windowSum / k
    result = [average]

    for i in range(len(nums) - k):
        windowSum = windowSum - nums[i] + nums[i + k]
        average = windowSum / k
        result.append(average)

    return result
