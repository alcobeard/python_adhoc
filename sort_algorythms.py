import random

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    # Если взять самый худший случай (изначально список отсортирован 
    # по убыванию), затраты времени будут равны O(n²), где n — количество элементов списка.

def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    # Затраты времени на сортировку выборкой в среднем составляют O(n²), где n — количество элементов списка.

random_list = random.sample(range(1, 100), 20)
print(random_list)
selection_sort(random_list)
print(random_list)