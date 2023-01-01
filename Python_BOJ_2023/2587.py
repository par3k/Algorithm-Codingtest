# 대표값2

nums = list()
for i in range(5):
    nums.append(int(input()))
print(sum(nums) // 5)

nums.sort()
print(nums[len(nums) // 2])