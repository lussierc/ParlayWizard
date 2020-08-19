"""WIP -- GOING TO BE SOME NASTY CODE FOR NOW, IN ONE FILE."""


def get_games():
    """Gets the user's chosen games for parlays."""
    data_dict={}
    num_of_games = int(input("* Enter number of games: "))
    game_list = []
    for game in range(num_of_games):
        game_info = []
        print("--------------")
        team1 = input("*- Enter Team 1 Name: ")
        team1_odds = input("*-- Enter Team 1 Odds: ")
        team1_dict = {team1:team1_odds}
        print(team1_dict)
        print("-----")
        team2 = input("*- Enter Team 2 Name: ")
        team2_odds = input("*-- Enter Team 2 Odds: ")
        team2_dict = {team2:team2_odds}
        game_info.append(team1_dict)
        game_info.append(team2_dict)
        game_list.append(game_info)
        print(game_list)

    # store in object here
    print("Finished entering information!")
    return(game_list)

def get_teams():
    game_list = get_games()
    game_counter = 0
    for game in game_list:
        game_counter += 1
        print("--- Game #", game_counter, " ---")
        for team in game:
            print(team)
            print("KEYS", team.keys())

get_teams()
# grab teams out of game_info using for loop
# generate every possible winner combo using permutated lists (maybe?)
# then calculate money for every parlay
