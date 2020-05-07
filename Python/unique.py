def unique(list1):
    unique_list = []

    for x in list1:
        if x not in unique_list:
            unique_list.append(x)

    return unique_list

list2 =[2, 1, 1, 3, 4, 3, 3, 5]
print("\nthe unique values from 2nd list is")

print(unique(list2))
