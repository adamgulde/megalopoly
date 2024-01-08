# Author: Adam Gulde
# Created: 12/30/2023
# Last Modified: 1/7/2024
# Purpose: Simulate a game of Monopoly to determine the most visited locations

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

    # Initialize lists to store number of landings and dice rolls
    board_landings = [0] * 40
    property_landings = [0] * NUM_ROLLS
    dice_rolls = [0] * NUM_ROLLS

    # Initialize location, chance card deck position, and chance cards
    location = 0
    ch_deck_pos = 0
    # List of location indices for cards, -1 if the card does not move the player
    chance_cards = [0, 24, 11, 30, 39, 5, "R", "R", "U", -3, -1, -1, -1, -1, -1, -1]
    random.shuffle(chance_cards)
    community_chest_cards = [0, 30, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    random.shuffle(community_chest_cards)

    # Simulation loops    
    for p in range(NUM_PLAYERS):
        for i in range(NUM_ROLLS):
            directional_die = int(random.random()*6)+1
            white_die = int(random.random()*6)+1
            dice_rolls[i] = directional_die + white_die
            location += dice_rolls[i]
            
            if location>39:
                location -= 40
            property_landings[i] = location

            # Chance conditions
            if(location == 7 or location == 22 or location == 36):
                # Check card at deck position is a moving location card
                if(chance_cards[ch_deck_pos] != -1):
                    if(type(chance_cards[ch_deck_pos]) == int):
                        location = chance_cards[ch_deck_pos]
                    # If the card is a railroad, advance using while loop
                    elif(chance_cards[ch_deck_pos] == 'R'):
                        while(location != 5 and location != 15 and location != 25 and location != 35):
                            location += 1
                            if(location>39):
                                location -= 40
                    elif(chance_cards[ch_deck_pos] == 'U'):
                        location = {True: 12, False: 28} [location - 12 < 0]
                    property_landings.append(location)
                ch_deck_pos += 1
                if(ch_deck_pos == 16):
                    ch_deck_pos = 0   # Reset deck position

            # Community chest conditions
            if(location == 2 or location == 17 or location == 33):
                # Check card at deck position is a moving location card
                if(community_chest_cards[ch_deck_pos] != -1):
                    location = community_chest_cards[ch_deck_pos]
                    property_landings.append(location)
                ch_deck_pos += 1
                if(ch_deck_pos == 16):
                    ch_deck_pos = 0

            if(location == 30):
                location = 10  # Go to jail

            # Condition for rolling doubles
            doubles_count = 0
            while(directional_die == white_die and location != 10):
                doubles_count += 1
                directional_die = int(random.random()*6)+1
                white_die = int(random.random()*6)+1
                dice_rolls.insert(i+1, directional_die + white_die)
                location += dice_rolls[i+1]

                if location>39:
                    location -= 40
                property_landings.append(location)
                if(location == 30 or doubles_count == 3):
                    location = 10  # Go to jail
                    directional_die = -1
                    white_die = -2

        location = 0 # Reset location for next player
            
        for i in range(len(dice_rolls)):
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

def display_statistics(board_landings: list):
    import matplotlib.pyplot as plt
    # Assuming board_landings is your data
    bar_data = board_landings

    # CC1 = Community Chest 1, Ch1 = Chance 1, etc.
    loc_abbrev = ["Go", "MA", "CC1", "BA", "IT", "RR", "OA", "Ch1", "VA", "CA", 
                  "Ja", "CP", "EC", "SA", "VA", "PR", "JP", "CC2", "TA", "NY", 
                  "FP", "KA", "In", "Ch2", "Il", "BR", "AA", "VA", "WW", "MG", 
                  "GJ", "Pa", "NC", "CC3", "Pe", "SL", "Ch3", "PP", "LT", "Bo"]

    # Create the bar chart
    plt.bar(loc_abbrev, bar_data)

    # Optionally, you can set the labels for the x-axis and y-axis, and the title
    plt.xlabel('Locations')
    plt.ylabel('Number of times landed on')
    plt.title('Megalopoly Statistics')

    plt.ylim((min(bar_data), 0) [min(bar_data)-1 < 0], max(bar_data)+1)

    # Display the chart
    plt.show()

if __name__ == "__main__":
    num_games = int(input("Indicate number of games to simulate: "))
    num_players = int(input("Indicate number of players to simulate: "))
    num_rolls = int(input("Indicate number of turns to simulate: "))
    print("Simulating...")

    board_landings = [0] * 40
    property_landings = [0] * num_rolls

    for i in range(num_games):
        print(f"Game {i+1} of {num_games}", end="\r")

        # Get the list from simulate_game
        simulate_game_values = simulate_game(num_rolls, num_players)

        # Add the values to the corresponding values in board_landings
        board_landings = [x + y for x, y in zip(board_landings, simulate_game_values[0])]

        # Add the values to the corresponding values in property_landings
        property_landings = [x + y for x, y in zip(property_landings, simulate_game_values[1])]

    print_board(board)
    print()
    print_board(board_landings)
    print()
    print_statistics(board, board_landings, num_rolls)
    print(Style.RESET_ALL)

    display_statistics(board_landings)