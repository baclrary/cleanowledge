def sortArray(nums):
    nums_len = len(nums)
    for n in nums:
        if n > nums[n+1]:
            temp = nums[n+1]
            nums[n+1] = n
            n = temp
    return nums


array = [1, 5, 3, 2]
print(sortArray(array))
