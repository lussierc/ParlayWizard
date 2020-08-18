"""WIP GOING TO BE SOME NASTY CODE FOR NOW, IN ONE FILE."""

def get_games():
    """Gets the user's chosen games for parlays."""
    num_of_games = int(input("* Enter number of games: "))
    for game in range(num_of_games):
        print("--------------")
        team1 = input("*- Enter Team 1 Name: ")
        team1_odds = input("*-- Enter Team 1 Odds: ")
        print("-----")
        team2 = input("*- Enter Team 2 Name: ")
        team2_odds = input("*-- Enter Team 1 Odds: ")
        # store in object here
    print("Finished entering information!")

get_games()
