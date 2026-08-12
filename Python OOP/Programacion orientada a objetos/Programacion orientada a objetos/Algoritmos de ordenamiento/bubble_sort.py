def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(n - 1, i, -1):   
            if list[j] < list[j - 1]:   
                list[j], list[j - 1] = list[j - 1], list[j]
    return list

numbers = [5, 2, 8, 1, 9, 3]

result = bubble_sort(numbers)
print(result)