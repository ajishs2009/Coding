def Multiple_tuple(nums):
    numbers = list(nums)
    product = 1
    for x in numbers:
        product *= x
    return product
nums = (4,3,2,-1,18)
print("Original Tuple: ")
print(nums)
print("The product is:", Multiple_tuple(nums))