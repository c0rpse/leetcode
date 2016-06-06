import random
def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


def partition(nums, start, end):
    pivot_loc = start
    pivot_val = nums[pivot_loc]

    for index in range(start, end+1):
        if nums[index] < pivot_val:
            pivot_loc += 1
            swap(nums, index, pivot_loc)

    swap(nums, pivot_loc, start)
    return start


def quick_sort(nums, start, end):
    if start < end:
        pos = partition(nums, start, end)
        quick_sort(nums, start, pos-1)
        quick_sort(nums, pos+1, end)


l = list()
for i in xrange(10):
    l.append(random.randint(-10000,10000))
quick_sort(l,0,len(l)-1)
print l

