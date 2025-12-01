def myselectionsort(list):
    list = list.copy()
    n = len(list)

    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]

    return list
nums = input("Enter numbers separated by commas: ")
nums_list = [int(x) for x in nums.split(",")]

print("Original list:", nums_list)

sorted_my = myselectionsort(nums_list)
print("Sorted list (using my selection sort):", sorted_my)

sorted_default = sorted(nums_list)
print("Sorted list (using default function):", sorted_default)

if sorted_my == sorted_default:
    print("Both lists are identical!")
else:
    print("The lists are not the same.")