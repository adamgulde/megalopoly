from colorama import Fore, Back, Style
properties = {"Mediterranean Avenue":   (60, 50, 2, 10, 30, 90, 160, 250, 30, "\033[38;5;94m"),
              "Baltic Avenue":          (60, 50, 4, 20, 60, 180, 320, 450, 30, "\033[38;5;94m"),
              "Oriental Avenue":        (100, 50, 6, 30, 90, 270, 400, 550, 50, "\033[38;5;117m"),
              "Vermont Avenue":         (100, 50, 6, 30, 90, 270, 400, 550, 50, "\033[38;5;117m"),
              "Conneticut Avenue":      (120, 50, 8, 40, 100, 300, 450, 600, 60, "\033[38;5;117m"),
              "St. Charles Place":      (140, 100, 10, 50, 150, 450, 625, 750, 70, "\033[38;5;162m"),
              "States Avenue":          (140, 100, 10, 50, 150, 450, 625, 750, 70, "\033[38;5;162m"),
              "Virginia Avenue":        (160, 100, 12, 60, 180, 500, 700, 900, 80, "\033[38;5;162m"),
              "St. James Place":        (180, 100, 14, 70, 200, 550, 750, 950, 90, "\033[38;5;202m"),
              "Tennessee Avenue":       (180, 100, 14, 70, 200, 550, 750, 950, 90, "\033[38;5;202m"),
              "New York Avenue":        (200, 100, 16, 80, 220, 600, 800, 1000, 100, "\033[38;5;202m"),
              "Kentucky Avenue":        (220, 150, 18, 90, 250, 700, 875, 1050, 110, Fore.RED),
              "Indiana Avenue":         (220, 150, 18, 90, 250, 700, 875, 1050, 110, Fore.RED),
              "Illinois Avenue":        (240, 150, 20, 100, 300, 750, 925, 1100, 120, Fore.RED),
              "Atlantic Avenue":        (260, 150, 22, 110, 330, 800, 975, 1150, 130, "\033[38;5;226m"),
              "Ventnor Avenue":         (260, 150, 22, 110, 330, 800, 975, 1150, 130, "\033[38;5;226m"),
              "Marvin Gardens":         (280, 150, 24, 120, 360, 850, 1025, 1200, 140, "\033[38;5;226m"),
              "Pacific Avenue":         (300, 200, 26, 130, 390, 900, 1100, 1275, 150, Fore.GREEN),
              "North Carolina Avenue":  (300, 200, 26, 130, 390, 900, 1100, 1275, 150, Fore.GREEN),
              "Pennsylvania Avenue":    (320, 200, 28, 150, 450, 1000, 1200, 1400, 160, Fore.GREEN),
              "Park Place":             (350, 200, 35, 175, 500, 1100, 1300, 1500, 175, Fore.BLUE),
              "Boardwalk":              (400, 200, 50, 200, 600, 1400, 1700, 2000, 200, Fore.BLUE)
            }
"""
@properties
Key: title
Value: tuple with values as follows:
    0 - Purchase Price
    1 - Price Per House
    2 - Rent
    3 - Rent w 1 House
    4 - Rent w 2 House
    5 - Rent w 3 House
    6 - Rent w 4 House
    7 - Rent w Hotel
    8 - Mortgage Value
    9 - Color Code
"""

RR_RENTS = [25, 50, 100, 150, 250, 450, 700, 1000, 1250, 1500, 1750, 2000]
UT_RENTS = [4, 10, 25, 50, 100, 300]
"""
@RR_RENTS constant
and 
@UT_RENTS constant
Constant values for railroad and utility rents according to Megalopoly ruleset.
Adjust as needed.
"""
special_properties = {
              "Reading Railroad":       (200, RR_RENTS[0], RR_RENTS[1], RR_RENTS[2], RR_RENTS[3], RR_RENTS[4], 
                                         RR_RENTS[5], RR_RENTS[6], RR_RENTS[7], RR_RENTS[8], RR_RENTS[9], 
                                          RR_RENTS[10], RR_RENTS[11], 100, Fore.LIGHTBLACK_EX),
              "Pennsylvania Railroad":  (200, RR_RENTS[0], RR_RENTS[1], RR_RENTS[2], RR_RENTS[3], RR_RENTS[4], 
                                         RR_RENTS[5], RR_RENTS[6], RR_RENTS[7], RR_RENTS[8], RR_RENTS[9], 
                                          RR_RENTS[10], RR_RENTS[11], 100, Fore.LIGHTBLACK_EX),
              "B&O Railroad":           (200, RR_RENTS[0], RR_RENTS[1], RR_RENTS[2], RR_RENTS[3], RR_RENTS[4], 
                                         RR_RENTS[5], RR_RENTS[6], RR_RENTS[7], RR_RENTS[8], RR_RENTS[9], 
                                          RR_RENTS[10], RR_RENTS[11], 100, Fore.LIGHTBLACK_EX),
              "Short Line":             (200, RR_RENTS[0], RR_RENTS[1], RR_RENTS[2], RR_RENTS[3], RR_RENTS[4], 
                                         RR_RENTS[5], RR_RENTS[6], RR_RENTS[7], RR_RENTS[8], RR_RENTS[9], 
                                          RR_RENTS[10], RR_RENTS[11], 100, Fore.LIGHTBLACK_EX),
              "Electric Company":       (150, UT_RENTS[0], UT_RENTS[1], UT_RENTS[2], UT_RENTS[3],
                                          UT_RENTS[4], UT_RENTS[5], -1, -1, -1, -1, -1, -1, 75, Fore.YELLOW),
              "Water Works":            (150, UT_RENTS[0], UT_RENTS[1], UT_RENTS[2], UT_RENTS[3],
                                          UT_RENTS[4], UT_RENTS[5], -1, -1, -1, -1, -1, -1, 75, Fore.CYAN)
              }
"""
@special_properties
These properties do not follow the above rent pattern, 
so they are given their own individual dictionary.
Key: title
Value: tuple with values as follows:
    0 - Purchase Price
    1 - Rent (or multiplier) with 1 location owned
    2 - Rent (or multiplier) with 2 location owned
    3 - Rent (or multiplier) with 3 location owned
    4 - Rent (or multiplier) with 4 location owned
    5 - Rent (or multiplier) with 5 location owned
    6 - Rent (or multiplier) with 6 location owned
    7 - Rent with 7 railroads owned
    8 - Rent with 8 railroads owned
    9 - Rent with 9 railroads owned
    10 - Rent with 10 railroads owned
    11 - Rent with 11 railroads owned
    12 - Rent with 12 railroads owned
    13 - Mortgage Value
    14 - Color Code
"""

# Maps to rename other game's locations to the standardized Monopoly properties 
target_properties = {  "Coffee": "Mediterranean Avenue",
                       "Honey": "Baltic Avenue",
                       "Shampoo": "Oriental Avenue",
                       "Vitamins": "Vermont Avenue",
                       "Make Up": "Conneticut Avenue",
                       "Treats": "St. Charles Place",
                       "Chew Toys": "States Avenue",
                       "Catnip": "Virginia Avenue",
                       "Sweater": "St. James Place",
                       "Shoes": "Tennessee Avenue",
                       "Jewelry": "New York Avenue",
                       "Books": "Kentucky Avenue",
                       "Music": "Indiana Avenue",
                       "Movies": "Illinois Avenue",
                       "Action Figures": "Atlantic Avenue",
                       "Board Games": "Ventnor Avenue",
                       "Bicycle": "Marvin Gardens",
                       "Tableware": "Pacific Avenue",
                       "Bedding": "North Carolina Avenue",
                       "Furniture": "Pennsylvania Avenue",
                       "Tablet": "Park Place",
                       "TV": "Boardwalk"
                    }

starwars_properties = {"Tatooine Dune Sea": "Mediterranean Avenue",
                       "Tatooine System": "Baltic Avenue",
                       "Bothawui": "Oriental Avenue",
                       "Ruusan": "Vermont Avenue",
                       "Abregado System": "Conneticut Avenue",
                       "Rugosa": "St. Charles Place",
                       "Toydaria System": "States Avenue",
                       "Rishi": "Virginia Avenue",
                       "Teth Castle": "St. James Place",
                       "Teth Jungle": "Tennessee Avenue",
                       "Teth System": "New York Avenue",
                       "Kalida Nebula": "Kentucky Avenue",
                       "Antar": "Indiana Avenue",
                       "Rodia": "Illinois Avenue",
                       "Ryloth": "Atlantic Avenue",
                       "Florrum": "Ventnor Avenue",
                       "Vassak": "Marvin Gardens",
                       "Crystal City Plaza Center": "Pacific Avenue",
                       "Crystal City": "North Carolina Avenue",
                       "Christophsis System": "Pennsylvania Avenue",
                       "Ziro's Palace": "Park Place",
                       "Jabba's Palace": "Boardwalk",
                    }
special_starwars_properties = {
                       "The Twilight": "Reading Railroad",
                       "The Resolute": "Pennsylvania Railroad",
                       "The Malevolence": "B&O Railroad", 
                       "The Defender": "Short Line",
                       "Skytop Station": "Electric Company",
                       "Republic Medical Station": "Water Works"
                       }

def print_deed(k: str, data: list) -> None:
    if len(data)==10:
        print(f"""{data[9]}
        {ascii_art.get("title deed")}
        {ascii_art.get("divider")}
    === {k} ===
    Purchase Price: {data[0]}
    Price Per House: {data[1]}
    Rent: {data[2]}
    Rent w 1 house: {data[3]} 
    Rent w 2 houses: {data[4]}
    Rent w 3 houses: {data[5]}
    Rent w 4 houses: {data[6]}
    Rent w hotel: {data[7]}
    Mortgage Value: {data[8]}
        {ascii_art.get("divider")}
        """)
    else:
        print(f"""{data[14]}
        {ascii_art.get("title deed")}
        {ascii_art.get("divider")}
    === {k} ===
    Purchase Price: {data[0]}
    Rent (or multiplier) with 1 locations owned: {data[1]}
    Rent (or multiplier) with 2 locations owned: {data[2]}
    Rent (or multiplier) with 3 locations owned: {data[3]}
    Rent (or multiplier) with 4 locations owned: {data[4]}
    Rent (or multiplier) with 5 locations owned: {data[5]}
    Rent (or multiplier) with 6 locations owned: {data[6]}
    Rent with 7 railroads owned: {data[7]}
    Rent with 8 railroads owned: {data[8]}
    Rent with 9 railroads owned: {data[9]}
    Rent with 10 railroads owned: {data[10]}
    Rent with 11 railroads owned: {data[11]}
    Rent with 12 railroads owned: {data[12]}
    Mortgage Value: {data[13]}
        {ascii_art.get("divider")}
        """)

def get_deed(title: str) -> None:
    exists = False
    for sw_key in starwars_properties:
        if sw_key.lower().startswith(title.lower()):
            data = properties.get(starwars_properties.get(sw_key))
            print_deed(sw_key, data)
            exists = True
            return
        else: 
            data = None

    for t_key in target_properties:
        if t_key.lower().startswith(title.lower()):
            data = properties.get(target_properties.get(t_key))
            print_deed(t_key, data)
            exists = True
            return
        else: 
            data = None

    for key in properties:
        if key.lower().startswith(title.lower()):
            data = properties.get(key)
            print_deed(key, data)
            exists = True
            return
        else: 
            data = None  
    
    print(Style.RESET_ALL, end="")
    
    for sp_key in special_properties:
        if sp_key.lower().startswith(title.lower()):
            special_data = special_properties.get(sp_key)
            print_deed(sp_key, special_data)
            exists = True
            return
        else: 
            special_data = None
    
    print(Style.RESET_ALL, end="")

    for sp_st_key in special_starwars_properties:
        if sp_st_key.lower().startswith(title.lower()):
            special_data = special_properties.get(special_starwars_properties.get(sp_st_key))
            print_deed(sp_st_key, special_data)
            exists = True
            return
        else: 
            special_data = None
    
    if not exists:
        print(Fore.RED + "Unrecognized property!", end="")
    print(Style.RESET_ALL, end="")

# Cool fonts generated here: https://patorjk.com/software/taag/
def get_graphics() -> dict:
    with open("ascii.txt") as f:
        text = f.read().split("BREAK_TEXT")

    return {"title": text[0],
            "divider": text[1],
            "help": text[2],
            "title deed": text[3]}

def print_properties():

    property_tuples = []

    property_tuples.append([Fore.LIGHTYELLOW_EX + "Standard Monopoly properties", 
                            Fore.LIGHTYELLOW_EX + "Standard Star Wars Monopoly properties", 
                            Fore.LIGHTYELLOW_EX + "Standard Target Monopoly properties"])
    
    special_property_tuples = []

    for key in properties:
        property_tuples.append([properties.get(key)[9] + key, "", ""])
    for key in special_properties:
        special_property_tuples.append([special_properties.get(key)[14] + key, ""])
    
    i = 1
    for key in starwars_properties:
        property_tuples[i][1] = properties.get(starwars_properties.get(key))[9] + key
        i+=1
    
    i = 0
    for key in special_starwars_properties:
        special_property_tuples[i][1] = special_properties.get(special_starwars_properties.get(key))[14] + key
        i+=1

    i = 1
    for key in target_properties:
        property_tuples[i][2] = properties.get(target_properties.get(key))[9] + key
        i+=1
    

    for tup in property_tuples:
        for str_n in tup:
            for i in range(41-len(str_n[str_n.find('m'):])):
                str_n += '.'
            print(str_n, end=' $$ ')
        print()
    for tup in special_property_tuples:
        for str_n in tup:
            for i in range(41-len(str_n[str_n.find('m'):])):
                str_n += '.'
            print(str_n, end=' $$ ')
        print()


def calculate(first_number, operator, second_number):
    # Addition (+)
    if(operator == '+'):
        return first_number + second_number
    # Substraction (-)
    elif(operator == '-'):
        return first_number - second_number
    # Multiplication (*)
    elif(operator == '*'):
        return first_number * second_number
    # Division (/)
    elif(operator == '/'):
        return first_number / second_number
    # Modulo (%)
    elif(operator == '%'):
        return first_number % second_number
    # Unknown
    else:
        return 'Invalid operation!'


if __name__ == "__main__":
    ascii_art = get_graphics()

    # Some text outputting using colorama and the ascii.txt readins
    print(Fore.LIGHTYELLOW_EX)
    print(ascii_art.get("title"), end="")
    print(Style.RESET_ALL)

    # Main querying loop
    while True:
        stdIn = input(Fore.WHITE + "\nQuery? " + Style.RESET_ALL).lower()
        if(stdIn != "" and not stdIn.isspace()):    
            if(stdIn != "exit" and stdIn != "quit" and stdIn != "math" and stdIn != "help" and stdIn != "list"
               and not stdIn.isdigit()):
                get_deed(stdIn)
            elif(stdIn == "math" or stdIn.isdigit()):
                print(Back.LIGHTGREEN_EX + Fore.BLACK)
                try:
                    if(stdIn.isdigit()):
                        print(calculate(int(stdIn), input("Operation: "), int(input("Value 2: "))), end="")
                    else:
                        print(calculate(int(input("Value 1: ")), input("Operation: "), int(input("Value 2: "))), end="")
                except ZeroDivisionError:
                    print("Cannot divide by 0!")
                except ValueError:
                    print("Invalid character.")
                print(Style.RESET_ALL)
            elif(stdIn == "help"):
                print(Fore.LIGHTYELLOW_EX+ ascii_art.get('help'))
            elif(stdIn == "list"):
                print_properties()
            else:
                print(Fore.LIGHTYELLOW_EX+ "Thanks for using the Megalopoly Assistant. Goodbye!"+ Style.RESET_ALL)
                quit(0)