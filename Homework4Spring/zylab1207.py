#Hughes Izah , PSID 2310365

def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return age


# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = 0.70 * (220-age)
    return heart_rate


if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f'Fat burning heart rate for a {age} year-old: {heart_rate} bpm')
    except ValueError as ve:
        print('Invalid age.')
        print('Could not calculate heart rate info.', end='')

