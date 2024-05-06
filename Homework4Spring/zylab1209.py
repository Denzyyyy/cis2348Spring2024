#Hughes Izah , PSID 2310365


# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except ValueError:
        age = 0
    print(f'{name} {age}')
    parts = input().split()
    name = parts[0]
