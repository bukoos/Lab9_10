#2.	Дані послідовність чисел. Знайти довжину найдовшої строго зростаючої підпослідовності.
def longest_increasing_subsequence_length(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] > nums[j - 1]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(dp)
    return max(dp)

nums = [15, 7, 24, 25, 7, 19, 55, 64, 78]
print("Довжина найдовшої строго зростаючої підпослідовності:", longest_increasing_subsequence_length(nums))
