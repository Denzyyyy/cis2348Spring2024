def display_roster(roster):
    print("\nROSTER")
    for jersey, rating in sorted(roster.items()):
        print("Jersey number: {}, Rating: {}".format(jersey, rating))


def add_player(roster):
    jersey = int(input("\nEnter a new player's jersey number: "))
    rating = int(input("Enter the player's rating: "))
    roster[jersey] = rating


def delete_player(roster):
    jersey = int(input("\nEnter a jersey number: "))
    if jersey in roster:
        del roster[jersey]
        print("Player removed.")
    else:
        print("Jersey number not found.")


def update_player_rating(roster):
    jersey = int(input("\nEnter a jersey number: "))
    if jersey in roster:
        rating = int(input("Enter a new rating for player: "))
        roster[jersey] = rating
    else:
        print("Jersey number not found.")


def output_players_above_rating(roster):
    rating_threshold = int(input("\nEnter a rating: "))
    print("\nABOVE", rating_threshold)
    for jersey, rating in sorted(roster.items()):
        if rating > rating_threshold:
            print("Jersey number: {}, Rating: {}".format(jersey, rating))


def main():
    roster = {}
    for i in range(5):
        jersey = int(input("Enter player {}'s jersey number:\n".format(i + 1)))
        rating = int(input("Enter player {}'s rating:\n".format(i + 1)))
        roster[jersey] = rating

    print("\nROSTER")
    for jersey, rating in sorted(roster.items()):
        print("Jersey number: {}, Rating: {}".format(jersey, rating))

    while True:
        print(
            "\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n")
        choice = input("Choose an option:\n")

        if choice == 'a':
            add_player(roster)
        elif choice == 'd':
            delete_player(roster)
        elif choice == 'u':
            update_player_rating(roster)
        elif choice == 'r':
            output_players_above_rating(roster)
        elif choice == 'o':
            display_roster(roster)
        elif choice == 'q':
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
