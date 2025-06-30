nums = [10,20,20,30,30,30,40]
def removeDuplicates(self, nums):
    list = []
    k = 0
    for c in range(len(nums)):
        for d in range(c+1,len(nums)):
            if nums[c] != nums[d]:
                k += 1
                list.append(nums[c])
    return k, list
print(removeDuplicates(10,nums))