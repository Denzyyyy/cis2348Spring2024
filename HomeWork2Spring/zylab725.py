def exact_change(user_total):
    num_dollars = user_total // 100
    user_total %= 100

    num_quarters = user_total // 25
    user_total %= 25

    num_dimes = user_total // 10
    user_total %= 10

    num_nickels = user_total // 5
    user_total %= 5

    num_pennies = user_total

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    input_val = int(input())

    if input_val <= 0:
        print("no change")
    else:
        dollars, quarters, dimes, nickels, pennies = exact_change(input_val)

        if dollars:
            print(f"{dollars} {'dollar' if dollars == 1 else 'dollars'}")
        if quarters:
            print(f"{quarters} {'quarter' if quarters == 1 else 'quarters'}")
        if dimes:
            print(f"{dimes} {'dime' if dimes == 1 else 'dimes'}")
        if nickels:
            print(f"{nickels} {'nickel' if nickels == 1 else 'nickels'}")
        if pennies:
            print(f"{pennies} {'penny' if pennies == 1 else 'pennies'}")
