#Hughes Izah , PSID 2310365

def selection_sort_descend_trace(integer_list):
    n = len(integer_list)
    for i in range(n-1):
        max_index = i
        for j in range(i+1,n):
            if(integer_list[j]>integer_list[max_index]):
                max_index = j
        integer_list[i], integer_list[max_index] = integer_list[max_index],integer_list[i]
        for i in integer_list:
            print(i, end=' ')
        print()


if __name__ == "__main__":
    list_of_ints = [int(i) for i in input().split()]
    selection_sort_descend_trace(list_of_ints)
