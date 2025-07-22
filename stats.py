def calc(nums):
    total = 0
    a = nums[0]
    b = nums[0]
    
    for n in nums:
        total += n
        if n > a:
            a = n
        if n < b:
            b = n
    avg = total / len(nums)
    print("Sum:", total)
    print("Average:", avg)
    print("Max:", a)
    print("Min:", b)

list_nums = [3, 5, 2, 8, 1, 4]
calc(list_nums)
