nums = input()
lst = nums.split()

new_list = []

for i in lst:  # for loop to see if i in lst is true
    if int(i) > 0:
        new_list.append(int(i))

new_list.sort()

for x in new_list:
    print(x, end=' ')
