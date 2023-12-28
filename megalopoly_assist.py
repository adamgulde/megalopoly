from colorama import Fore, Back, Style
"""
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
properties = {"Mediterranean Avenue":   (60, 50, 2, 10, 30, 90, 160, 250, 30, "\033[38;5;94m"),
              "Baltic Avenue":          (60, 50, 4, 20, 60, 180, 320, 450, 30, "\033[38;5;94m"),
              "Oriental Avenue":        (100, 50, 6, 30, 90, 270, 400, 550, 50, "\033[1;34m"),
              "Vermont Avenue":         (100, 50, 6, 30, 90, 270, 400, 550, 50, "\033[1;34m"),
              "Conneticut Avenue":      (120, 50, 8, 40, 100, 300, 450, 600, 60, "\033[1;34m"),
              "St. Charles Place":      (140, 100, 10, 50, 150, 450, 625, 750, 70, "\033[1;31m"),
              "States Avenue":          (140, 100, 10, 50, 150, 450, 625, 750, 70, "\033[1;31m"),
              "Virginia Avenue":        (160, 100, 12, 60, 180, 500, 700, 900, 80, "\033[1;31m"),
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
special_properties = {
              "Reading Railroad":       (200, 25, 50, 100, 200, 100, Fore.LIGHTBLACK_EX),
              "Pennsylvania Railroad":  (200, 25, 50, 100, 200, 100, Fore.LIGHTBLACK_EX),
              "B&O Railroad":           (200, 25, 50, 100, 200, 100, Fore.LIGHTBLACK_EX),
              "Short Line":             (200, 25, 50, 100, 200, 100, Fore.LIGHTBLACK_EX),
              "Electric Company":       (150, 4, 10, -1, -1, 75, Fore.YELLOW),
              "Water Works":            (150, 4, 10, -1, -1,75, Fore.CYAN)
              }

# Maps to rename other game's locations to the standardized properties 
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

def get_deed(title: str) -> None:
    exists = False
    for sw_key in starwars_properties:
        if sw_key.lower().startswith(title.lower()):
            data = properties.get(starwars_properties.get(sw_key))
            print(f"""{data[9]}
            {ascii_art.get("title deed")}
            {ascii_art.get("divider")}
        === {sw_key} ===
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
            exists = True
            break
        else: 
            data = None
    
    print(Style.RESET_ALL, end="")
    
    for t_key in target_properties:
        if t_key.lower().startswith(title.lower()):
            data = properties.get(target_properties.get(t_key))
            print(f"""{data[9]}
            {ascii_art.get("title deed")}
            {ascii_art.get("divider")}
        === {t_key} ===
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
            exists = True
            break
        else: 
            data = None
    
    print(Style.RESET_ALL, end="")
    
    for key in properties:
        if key.lower().startswith(title.lower()):
            data = properties.get(key)
            print(f"""{data[9]}
            {ascii_art.get("title deed")}
            {ascii_art.get("divider")}
        === {key} ===
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
            exists = True
            break
        else: 
            data = None  
    
    print(Style.RESET_ALL, end="")
    
    for sp_key in special_properties:
        if sp_key.lower().startswith(title.lower()):
            special_data = special_properties.get(sp_key)
            print(f"""{special_data[6]}
        {ascii_art.get("title deed")}
        {ascii_art.get("divider")}
        === {sp_key} ===
        Purchase Price: {special_data[0]}
        Rent (or multiplier) w 1 type: {special_data[1]} 
        Rent (or multiplier) w 2 types: {special_data[2]}
        Rent w 3 types: {special_data[3]}
        Rent w 4 types: {special_data[4]}
        Mortgage Value: {special_data[5]}
        {ascii_art.get("divider")}
        """)
            exists = True
            break
        else: 
            special_data = None
    
    print(Style.RESET_ALL, end="")

    for sp_st_key in special_starwars_properties:
        if sp_st_key.lower().startswith(title.lower()):
            special_data = special_properties.get(special_starwars_properties.get(sp_st_key))
            print(f"""{special_data[6]}
        {ascii_art.get("title deed")}
        {ascii_art.get("divider")}
        === {sp_st_key} ===
        Purchase Price: {special_data[0]}
        Rent (or multiplier) w 1 type: {special_data[1]} 
        Rent (or multiplier) w 2 types: {special_data[2]}
        Rent w 3 types: {special_data[3]}
        Rent w 4 types: {special_data[4]}
        Mortgage Value: {special_data[5]}
        {ascii_art.get("divider")}
        """)
            exists = True
            break
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
            "dollar": text[2],
            "title deed": text[3]}



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
        return 'Sorry, but I cannot understand your operation'


if __name__ == "__main__":
    ascii_art = get_graphics()

    # Some text outputting using colorama and the ascii.txt readins
    print(Fore.LIGHTYELLOW_EX)
    print(ascii_art.get("title"), end="")
    print(Style.RESET_ALL)

    # Main querying loop
    stdIn = ""
    while True:
        stdIn = input(Fore.GREEN + "\nQuery? " + Style.RESET_ALL).lower()
        if(stdIn != "" and not stdIn.isspace()):    
            if(stdIn != "exit" and stdIn != "quit" and stdIn != "math"):
                get_deed(stdIn)
            elif(stdIn == "math"):
                print(Back.LIGHTGREEN_EX + Fore.BLACK)
                try:
                    print(calculate(int(input("Value 1: ")), input("Operation: "), int(input("Value 2: "))), end="")
                except ZeroDivisionError:
                    print("Cannot divide by 0!")
                except ValueError:
                    print("Invalid character.")
                print(Style.RESET_ALL)
            else:
                print(Fore.LIGHTYELLOW_EX+ "Thanks for using the Megalopoly Assistant. Goodbye!"+ Style.RESET_ALL)
                quit(0)