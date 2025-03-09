# The idea is to know which half of the array is sorted
# If we find the middle element and compare it with terminal elements
# If the first element is smaller that the mid element then it means the left half is sorted
# If the last element is greater than the mid element then it means the right half is sorted

# Now decide where to move:
# Compare the target with arr[si] and arr[mid] in case 1
# Compare the target with arr[mid] and arr[ei] in case 2

def search(nums, target):
    si, ei = 0, len(nums)-1

    while si <= ei:
        mid = (si+ei)//2

        if nums[mid] == target:
            return mid
        
        elif nums[si] <= nums[mid]:
            if nums[si] <= target < nums[mid]:
                ei = mid - 1
            else:
                si = mid + 1
        
        else:
            if nums[mid] <= target <= nums[ei]:
                si = mid + 1
            
            else:
                ei = mid - 1
    
    return -1

arr = [10, 20, 40, 5, 6, 8]
print(search(arr, 6))