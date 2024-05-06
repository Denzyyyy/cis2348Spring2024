#Hughes Izah , PSID 2310365


class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def get_win_percentage(self):
        if self.wins + self.losses == 0:
            return 0.0
        return self.wins / (self.wins + self.losses)

    def print_standing(self):
        win_percentage = self.get_win_percentage()
        if win_percentage > 0.5:
            print(f"Congratulations, Team {self.name} has a winning average!")
        elif win_percentage < 0.5:
            print(f"Team {self.name} has a losing average.")
        else:
            print(f"Team {self.name} has an exactly even average.")


if __name__ == "__main__":
    team = Team()

    user_name = input()
    user_wins = int(input())
    user_losses = int(input())

    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses

    team.print_standing()
