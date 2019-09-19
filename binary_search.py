# This will contain a function that performs binary search

numList = [1, 2, 12, 234, 345, 456, 777, 999, 2454, 6435, 7687, 99999]
searchNum = 6435

def binary_search(target, nums):

    # 'Walls' of the possible positions
    floor_index = -1
    ceiling_index = len(nums)

    # While there isn't at least 1 index between floor and ceiling
    while floor_index + 1 < ceiling_index:

        # Halfway Index
        distance = ceiling_index - floor_index
        half_distance = distance // 2 # // operator is used to get the floor value
        guess_index = floor_index + half_distance

        guess_value = nums[guess_index]
        if guess_value == target:
            return True

        if guess_value > target:
            ceiling_index = guess_index

        else:
            floor_index = guess_index

    return False

result = binary_search(searchNum, numList)
print(result)