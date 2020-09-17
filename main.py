"""WIP -- GOING TO BE SOME NASTY CODE FOR NOW, IN ONE FILE."""


def get_games():
    """Gets the user's chosen games for parlays."""
    full_data_list = []
    data_dict = {}
    num_of_games = int(input("* Enter number of games: "))
    game_list = []
    teams1_list = []
    teams2_list = []
    for game in range(num_of_games):
        game_info = []
        print("--------------")
        team1 = input("*- Enter Team 1 Name: ")
        team1_odds = input("*-- Enter Team 1 Odds: ")
        team1_dict = {team1: team1_odds}
        teams1_list.append(team1)
        data_dict.update(team1_dict)

        print("-----")

        team2 = input("*- Enter Team 2 Name: ")
        team2_odds = input("*-- Enter Team 2 Odds: ")
        team2_dict = {team2: team2_odds}
        teams2_list.append(team2)
        data_dict.update(team2_dict)

        print(data_dict)

    # store in object here
    print("Finished entering information!")
    full_data_list.append(teams1_list)
    full_data_list.append(teams2_list)
    full_data_list.append(data_dict)
    print(full_data_list)
    return full_data_list


def get_teams():
    game_list = get_games()


get_teams()


def parlay_hedger():
    """Hedge a single Parlay or Bet easily, perfect to use for big plays you aren't as confident in."""


def parlay_wizard():
    """Finds a combination (if possible) of parlays so you are garaunteed to win money."""


# generate every possible winner combo using permutated lists (maybe?):::
# above 4 teams > or get rid of it
# if list contains team1 && team2 || team3 & team4 ... Get rid of it

# then calculate money for every parlay
# use lists to search dict with parlay odds
# put in parlay caluclation
# calculate how to get that garaunteed $
# add single shot option
