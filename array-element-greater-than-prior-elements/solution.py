nums = [4,2,7,5,9]

def countPriorGreaterElements(nums):
    max = nums[0]
    count = 1
    for i in range(1,len(nums)):
        if nums[i] > max:
            max = nums[i]
            count += 1
    return count

print(countPriorGreaterElements(nums))

            