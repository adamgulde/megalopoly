import megalopoly_assist as MA
import random
from colorama import Style
from statistics import mean, median

# Color literals for printing board
COLORS = {"BROWN": "\033[38;5;94m",
          "LIGHTBLUE": "\033[38;5;117m",
          "ROUGE": "\033[38;5;162m",
          "ORANGE": "\033[38;5;202m",
          "RED": "\033[38;5;9m",
          "YELLOW": "\033[38;5;226m",
          "GREEN": "\033[38;5;2m",
          "BLUE": "\033[38;5;12m",
          "WHITE": "\033[38;5;15m",
          "CYAN": "\033[38;5;14m",
          "LIGHTGRAY": "\033[38;5;7m"}

# Literals for community chest and chance draws
CC = COLORS.get("CYAN") + "CC"
C = COLORS.get("ORANGE") + "Ch"

board = [COLORS.get("WHITE")+"Go", 
         COLORS.get("BROWN")+"MA",
         CC,
         COLORS.get("BROWN")+"BA",
         COLORS.get("WHITE")+"IT",
         COLORS.get("LIGHTGRAY")+"RR",
         COLORS.get("LIGHTBLUE")+"OA",
         C, 
         COLORS.get("LIGHTBLUE")+"VA",
         COLORS.get("LIGHTBLUE")+"CA",
         COLORS.get("WHITE")+"Ja",
         COLORS.get("ROUGE")+"CP",
         COLORS.get("YELLOW")+"EC",
         COLORS.get("ROUGE")+"SA",
         COLORS.get("ROUGE")+"VA",
         COLORS.get("LIGHTGRAY")+"PR",
         COLORS.get("ORANGE")+"JP",
         CC,
         COLORS.get("ORANGE")+"TA",
         COLORS.get("ORANGE")+"NY",
         COLORS.get("WHITE")+"FP",
         COLORS.get("RED")+"KA",
         COLORS.get("RED")+"In",
         C,
         COLORS.get("RED")+"Il",
         COLORS.get("LIGHTGRAY")+"BR",
         COLORS.get("YELLOW")+"AA",
         COLORS.get("YELLOW")+"VA",
         COLORS.get("CYAN")+"WW",
         COLORS.get("YELLOW")+"MG",
         COLORS.get("WHITE")+"GJ",
         COLORS.get("GREEN")+"Pa",
         COLORS.get("GREEN")+"NC",
         CC,
         COLORS.get("GREEN")+"Pe",
         COLORS.get("LIGHTGRAY")+"SL",
         C,
         COLORS.get("BLUE")+"PP",
         COLORS.get("WHITE")+"LT",
         COLORS.get("BLUE")+"Bo"]

def print_board(board:list):    
    # Print board with string values (when displaying property names.)
    # Print with manual 4 space padding to center text
    if(type(board[0]) == str):    
        # Top row
        for i in range(20, 31):
            print(f"{Style.RESET_ALL}[ {board[i]}{Style.RESET_ALL} ]", end="")
        print()

        # Middle rows of board
        for i in range(19, 10, -1):
            if i == 15:
                print(f"{Style.RESET_ALL}[ {board[i]}{Style.RESET_ALL} ]                      MEGALOPOLY                      [ {board[20-i+30]} ]")
            else:    
                print(f"{Style.RESET_ALL}[ {board[i]}{Style.RESET_ALL} ]                                                      [ {board[20-i+30]} ]")

        # Bottom of board
        for i in range(11):
            print(f"{Style.RESET_ALL}[ {board[10-i]}{Style.RESET_ALL} ]", end="")
        print()

    # Print board of integer values (when displaying number of landings.)
    # Print with automatic 4 space padding to center text
    elif(type(board[0]) == int):
        # Top row
        for i in range(20, 31):
            print(f"{Style.RESET_ALL}[{str(board[i]).center(4)}{Style.RESET_ALL}]", end="")
        print()

        # Middle rows of board
        for i in range(19, 10, -1):
            if i == 15:
                print(f"{Style.RESET_ALL}[{str(board[i]).center(4)}{Style.RESET_ALL}]                      MEGALOPOLY                      [{str(board[20-i+30]).center(4)}]")
            else:    
                print(f"{Style.RESET_ALL}[{str(board[i]).center(4)}{Style.RESET_ALL}]                                                      [{str(board[20-i+30]).center(4)}]")

        # Bottom of board
        for i in range(11):
            print(f"{Style.RESET_ALL}[{str(board[10-i]).center(4)}{Style.RESET_ALL}]", end="")
        print()

def simulate_game(num_rolls:int, num_players:int) -> (list, list):
    # Constants to determine dice rolls
    NUM_ROLLS = num_rolls
    NUM_PLAYERS = num_players

    board_landings = [0] * 40
    property_landings = [0] * NUM_ROLLS
    dice_rolls = list(range(NUM_ROLLS))

    location = 0

    # Add rolling doubles
    # Add chance / community chest jail cards (1/52 chance)
    # Add chance / community chest location cards (railroad, boadwalk, utility, etc.)
    # Add chance / community chest advance to GO cards
    # Add megalopoly directional die
     
    for p in range(NUM_PLAYERS):
        for i in range(NUM_ROLLS):
            directional_die = int(random.random()*6)+1
            white_die = int(random.random()*6)+1
            dice_rolls[i] = directional_die + white_die
            location += dice_rolls[i]
            if location>39:
                location -= 40
            property_landings[i] = location
            if(location == 30):
                location = 10  # Go to jail
        location = 0 # Reset location for next player
            
        for i in range(NUM_ROLLS):
            board_landings[property_landings[i]] += 1

    return board_landings, property_landings

def print_statistics(board:list, board_landings:list, num_rolls:int):
    print(f"Statistics for {num_rolls} turns:")
    print(f"Mean: {mean(board_landings)}")
    print(f"Median: {median(board_landings)}")
    print(f"Max: {max(board_landings)}")
    print(f"Min: {min(board_landings)}")
    
    # Pair each location with its number of visits
    location_visits = list(zip(board, board_landings))

    # Sort the pairs by number of visits in descending order
    location_visits.sort(key=lambda x: x[1], reverse=True)

    # Get the top 5 locations
    top_5_locations = [location for location, visits in location_visits[:5]]

    # Get the bottom 5 locations
    bottom_5_locations = [location for location, visits in location_visits[-5:]]

    # Print the top 5 locations
    print(f"Top locations visited:")
    for n in range(len(top_5_locations)):
        print(f"{Style.RESET_ALL}{1+n}. {top_5_locations[n]}")

    print(Style.RESET_ALL)

    print(f"Locations least visited:")
    for n in range(len(bottom_5_locations)):
        print(f"{Style.RESET_ALL}{36+n}. {bottom_5_locations[n]}")

def display_statistics(board_landings):
    import matplotlib.pyplot as plt
    # Assuming board_landings is your data
    bar_data = board_landings

    loc_abbrev = ["Go", "MA", "CC", "BA", "IT", "RR", "OA", "Ch", "VA", "CA", 
                  "Ja", "CP", "EC", "SA", "VA", "PR", "JP", "CC", "TA", "NY", 
                  "FP", "KA", "In", "Ch", "Il", "BR", "AA", "VA", "WW", "MG", 
                  "GJ", "Pa", "NC", "CC", "Pe", "SL", "Ch", "PP", "LT", "Bo"]

    # Create the bar chart
    plt.bar(loc_abbrev, bar_data)

    # Optionally, you can set the labels for the x-axis and y-axis, and the title
    plt.xlabel('Locations')
    plt.ylabel('Number of times landed on')
    plt.title('Megalopoly Statistics')

    plt.ylim(min(bar_data)-1, max(bar_data)+1)

    # Display the chart
    plt.show()

if __name__ == "__main__":
    num_games = int(input("Indicate number of games to simulate: "))
    num_rolls = int(input("Indicate number of turns to simulate: "))
    num_players = int(input("Indicate number of players to simulate: "))
    input("Press enter to simulate game(s)...")

    board_landings = [0] * 40
    property_landings = [0] * num_rolls

    for i in range(num_games):
        # Get the list from simulate_game
        simulate_game_values = simulate_game(num_rolls, num_players)[0]

        # Add the values to the corresponding values in board_landings
        board_landings = [x + y for x, y in zip(board_landings, simulate_game_values)]
        
        # Get the list from simulate_game
        simulate_game_values = simulate_game(num_rolls, num_players)[1]

        # Add the values to the corresponding values in property_landings
        property_landings = [x + y for x, y in zip(property_landings, simulate_game_values)]

    print_board(board)
    print()
    print_board(board_landings)
    print()
    print_statistics(board, board_landings, num_rolls)
    print(Style.RESET_ALL)

    display_statistics(board_landings)