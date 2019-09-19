unsortedList = [1, 5, 4, 8, 2345, 67, 24, 83, 4356, 7347, 2, 7, 0, 345345, 234, 732, 9999]

def merge_sort(list_to_sort):
    
    # Base Case
    if len(list_to_sort) < 2:
        return list_to_sort
    
    # Divide the list in half
    mid_index = len(list_to_sort) // 2  # // operator to get the floor value
    left = list_to_sort[:mid_index]     # everything from the beginning to the mid index
    right = list_to_sort[mid_index:]    # everything from the mid index to the end

    # Sort each half
    # This is done recursively
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Merge the sorted halves
    sorted_list = []
    current_index_left = 0
    current_index_right = 0

    # The element from the sorted left comes first if 
    # it's less than the first index of the sorted right
    while len(sorted_list) < len(left) + len(right):    # While the final list is smaller than the halves combined
        if ( (current_index_left < len(left)) 
                and (current_index_right == len(right) 
                or sorted_left[current_index_left] < sorted_right[current_index_right])):
            
            sorted_list.append(sorted_left[current_index_left])
            current_index_left += 1
        
        else:
            sorted_list.append(sorted_right[current_index_right])
            current_index_right += 1
    
    return sorted_list

result = merge_sort(unsortedList)
print(result)