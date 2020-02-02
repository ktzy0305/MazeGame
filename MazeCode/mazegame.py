"""
Dear all, please write a unit test before coding a function.
"""

import csv
import time
import re



# Options for main menu
menu = ("Read and load maze from file", "View maze", "Play maze game", "Configure current maze")
# Options for configuration menu
configuration_menu = ["Create wall", "Create passageway", "Create start point", "Create end point"]
# State to check if game is running
run = True
# Variable to store maze object
maze = []

#Classes
class GameError(Exception):
    pass

#Display menu function
def display_menu(check):
    if check == True:
        print('\n==========\nMAIN MENU \n==========')#to print admin menu heading
        for i, item in enumerate(menu,1):
            print([i],'',item)#to print admin menu choice '' is used for formatting, to format to the same as the sample
        print()# to print a space in between the last choice of Admin Menu and the heading of Rider Menu
        print('[0]  Exit Maze') #to print out the rider menu and choices
        print('')
        return "Displaying Menu"
    else:
        return "Invalid menu"

# Display Configuration Menu Function
def displayConfigurationMenu():
    title = "CONFIGURATION MENU"
    print("\n{0}\n{1}".format(title, len(title)*"="))
    for i, item in enumerate(configuration_menu, 1):
        print("[{0}]  {1}".format(i, item))
    print()# to print a space in between the last choice
    print('[0]  Exit to Main Menu') 
    return "Displaying Configuration Menu"

# Function to check if maze is empty
def isEmpty(maze):
    return len(maze) == 0

# Function to check filename
def check_filename(filename):
    try :
        f = open(filename)
        csv_reader = csv.reader(f,delimiter=',')
        line_count = 0
        for row in csv_reader:
            maze.append(row)
            line_count += 1
        print("Number of lines read: " + str(line_count))
        return "Filename correct"
    except IOError:
        print("Error, file not found")
        return "Filename incorrect"

def check_List(maze):
    if not isEmpty(maze):
        errorMsg = "List is occupied."
        return (errorMsg)
    else:
        errorMsg = "List is empty."
        print (errorMsg + " Please load the maze with Option 1")
        return (errorMsg)

def checkMaze(list):
    maze_check = True
    for i in list:
        type_total = 0
        total = len (i)
        typeX = i.count("X")
        typeO = i.count("O")
        typeA = i.count("A")
        typeB = i.count("B")
        type_total = typeX + typeO + typeA + typeB
        #print(total, type_total, typeX, typeO, typeA, typeB) # can use to debug
        #print(maze)# can use to debug
        #print(i)# can use to debug

        if total != type_total:
            print ("The list is not a maze.")
            maze_check = False
            return "The list is not a maze."
        
    if maze_check:
        row=1
        for i in list:
            if row == 1:
                print("="*(len(i)*3))
                print("")
                row = 2
            print(i)
    return "The list is a maze."

def move(movement, start=''):
    movement = movement.upper()
    if movement == "W":
        print ("Moving upwards")
        if (start[0]-1 <0):
            print ("\nDead End. Please move in another direction.")
            return "Invalid Movement. Please try again."
        else:
            direction = maze[start[0]-1][start[1]]
            nextposition = SpaceCheck(direction)
            if nextposition == "Wall":
                print("Wall ahead. Please choose another direction.")
                return "Wall ahead"
            elif nextposition == "Space":
                final = (start[0]-1,start[1])
                change_postition(start, final)
            elif nextposition == "End":
                final = (start[0]-1,start[1])
                change_postition(start, final)
                game_end()
                return False
            else:
                print("Unknown attribute found")
                return ("Unknown")
        #raise IndexError
        return "Moved upwards"
    elif movement == "S":
        print("Moving downwards")
        if (start[0]+1 >len(maze)):
            print ("\nDead End. Please move in another direction.")
            return "Invalid Movement. Please try again."
        else:
            direction = maze[start[0]+1][start[1]]
            nextposition = SpaceCheck(direction)
            if nextposition == "Wall":
                print("Wall ahead. Please choose another direction.")
                return "Wall ahead"
            elif nextposition == "Space":
                final = (start[0]+1,start[1])
                change_postition(start, final)
            elif nextposition == "End":
                final = (start[0]+1,start[1])
                change_postition(start, final)
                game_end()
                return False
            else:
                print("Unknown attribute found")
                return ("Unknown")
        return "Moved downwards"
    elif movement == "A":
        print("Moving left")
        if (start[1]-1 <0):
            print ("\nDead End. Please move in another direction.")
            return "Invalid Movement. Please try again."
        else:
            direction = maze[start[0]][start[1]-1]
            print(direction)
            nextposition = SpaceCheck(direction)
            if nextposition == "Wall":
                print("Wall ahead. Please choose another direction.")
                return "Wall ahead"
            elif nextposition == "Space":
                final = (start[0],start[1]-1)
                change_postition(start, final)
            elif nextposition == "End":
                final = (start[0],start[1]-1)
                change_postition(start, final)
                game_end()
                return False
            else:
                print("Unknown attribute found")
                return ("Unknown")
        return "Moved left"
    elif movement == "D":
        print("Moving right")
        if (start[1]+1 >= len(maze[0])):
            print ("\nDead End. Please move in another direction.")
            return "Invalid Movement. Please try again."
        else:
            direction = maze[start[0]][start[1]+1]
            #print(direction)
            #print(maze)
            nextposition = SpaceCheck(direction)
            if nextposition == "Wall":
                print("Wall ahead. Please choose another direction.")
                return "Wall ahead"
            elif nextposition == "Space":
                final = (start[0],start[1]+1)
                change_postition(start, final)
            elif nextposition == "End":
                final = (start[0],start[1]+1)
                change_postition(start, final)
                game_end()
                return False
            else:
                print("Unknown attribute found")
                return ("Unknown")
        return "Moved right"
    elif movement == "M":
        print("Exiting to Menu...")
        time.sleep(2)
        return False
    else:
        msg = "Invalid Movement. Please try again."
        print(msg)
        return msg

    
def current_location(maze_structure):
    check = True
    for location in maze_structure:
        if "A" in  location:
            check = False
            print ("\nLocation of Start (A) = ( Row " + str(maze_structure.index(location)) + ", Column " + str(location.index("A")) + ")")
            return (maze_structure.index(location), location.index("A"))
    if check:
        print("\nNo starting point found. ")
        return "Error"
        
def end_location(maze_structure):
    check = True
    for location in maze_structure:
        if "B" in  location:
            print ("Location of End (B) = ( Row " + str(maze_structure.index(location)) + ", Column " + str(location.index("B"))+ ")")
            return (maze_structure.index(location), location.index("B"))
    if  check:
        print ("No ending point found.")
        return "Error"
    
def SpaceCheck(direction_value):
    if direction_value == "X":
        return("Wall")
    elif direction_value == "O":
        return("Space")
    elif direction_value == "B":
        return("End")
    else:
        return("Unknown")

def change_postition(initial, final):
    maze[initial[0]][initial[1]] = "O"
    maze[final[0]][final[1]] = "A"
    return "Position changed"

def game_end():
    print("CONGRATS!! YOU HAVE COMPLETE THE MAZE.")
    i = 5
    while i>0:
        print("Exiting game in..." + str(i))
        time.sleep(1)
        i -= 1
    print("Exiting...")

# Function to check if the text matches the coordinate pattern
def is_a_coordinate(text):
    match = re.search("^[0-9],[0-9]$", text)
    if match:
        return True
    else:
        return False

# Function to split the coordinate text into a list containing 2 numbers
def coordinate_text_split(text):
    # txt = "The rain in Spain"
    x = text.split(",")
    coordinates = list(map(lambda item: int(item), x))
    return coordinates

# Function to modify value in maze:
def modifyMaze(value, *args):
    if isEmpty(maze):
        raise GameError("No maze is loaded")
    else:
        if len(args) > 2:
            raise ValueError()
        else:
            row = args[0]
            column = args[1]
            if(row < 1):
                raise GameError("Invalid Row Value")
                # print("Invalid Row Value: {0}".format(row))
            elif(column < 1):
                raise GameError("Invalid Column Value")
                # print("Invalid Column Value: {0}".format(column))
            elif(len(maze) < row):
                raise GameError("Invalid Row Value")
            elif(len(maze[row]) < column):
                raise GameError("Invalid Column Value")
            else:
                maze[row-1][column-1] = value

# Create Wall
def createWall(*args):
    modifyMaze("X", *args)

def createPassageWay(*args):
    modifyMaze("O", *args)

def createStartPoint(*args):
    modifyMaze("A", *args)

def createEndPoint(*args):
    modifyMaze("B", *args)

def handle_configuration_option_input(value, function):
    if is_a_coordinate(value):
        coordinates = coordinate_text_split(value)
        try:
            function(*coordinates)
        except GameError:
            print("Invalid Coordinates {0}".format(tuple(coordinates)))
        return False
    elif value == 'B':
        return False
    elif value == 'M':
        return True
    else:
        return False
        
def check_configuration_option(option):
    if option == "1":
        print("Enter the coordinate of the item you wish to change.")
        print("Format: Row,Column\tExample: 3,4")
        print("Type 'B' to return Configuration Menu")
        print("Type 'M' to return to Main Menu") 
        action = handle_configuration_option_input(input("Coordinate: "), createWall)
        if(action):
            return False
        return "Configuration Option 1 is selected"

    elif option == "2":
        print("Enter the coordinate of the item you wish to change.")
        print("Format: Row,Column\tExample: 3,4")
        print("Type 'B' to return Configuration Menu")
        print("Type 'M' to return to Main Menu") 
        action = handle_configuration_option_input(input("Coordinate: "), createPassageWay)
        if(action):
            return False
        return "Configuration Option 2 is selected"
        
    elif option == "3":
        print("Enter the coordinate of the item you wish to change.")
        print("Format: Row,Column\tExample: 3,4")
        print("Type 'B' to return Configuration Menu")
        print("Type 'M' to return to Main Menu") 
        action = handle_configuration_option_input(input("Coordinate: "), createStartPoint)
        if(action):
            return False
        return "Configuration Option 3 is selected"

    elif option == "4":
        print("Enter the coordinate of the item you wish to change.")
        print("Format: Row,Column\tExample: 3,4")
        print("Type 'B' to return Configuration Menu")
        print("Type 'M' to return to Main Menu") 
        action = handle_configuration_option_input(input("Coordinate: "), createEndPoint)
        if(action):
            return False
        return "Configuration Option 4 is selected"
        
    elif option == "0":
        print("Exiting Configuration Menu...")
        time.sleep(2)
        return False
    else:
        print ("Invalid option")
        return "Invalid Configuration Option"

#try_list=[["X","O","A","B"], ["1","2"]]
#try_empty = []
#verify_list=[["X","O","A","B"], ["X","O","A","B"]]

<<<<<<< HEAD:MazeCode/mazegame.py


def check_option(option, end=''):
=======
def check_option(option):
>>>>>>> 8c276d4908d299e9e9685c63e4eacc36b1c91c58:MazeCode/mazegame_code.py
    if option == "1":
        if end=="break":
            return "Option 1 selected"
        maze.clear()
        file = input("Enter the name of the data file: ")
        check_filename(file)
        return "Option 1 selected"

    elif option == "2":
        empty = check_List(maze)
        if empty == "List is occupied.":
            checkMaze(maze)
        return "Option 2 selected"
    
    elif option == "3":
        if end=="break":
            return "Option 3 selected"
        continu = True
        while continu != False:
            mazecheck = check_List(maze)
            check_if_maze = checkMaze(maze)
            if (mazecheck== "List is occupied." and check_if_maze == "The list is a maze."):
                current = current_location(maze)
                end = end_location(maze)
                if (end== "Error" or  current == "Error"):
                    print("\nIncomplete Maze. Please load a complete Maze or Reload a complete Maze to play.")
                    break
                else:
                    print ("\nPress 'W' for UP, 'A' for LEFT, 'S' for DOWN, 'D' for RIGHT, 'M' for MENU")
                    choice = input("Select your Move: ")
                    movement = move(choice, current)
                    continu = movement
            else:
                break
                    
        return "Option 3 selected"
    
    elif option == "4":
<<<<<<< HEAD:MazeCode/mazegame.py
        if end=="break":
            return "Option 4 selected"
        displayConfigurationMenu()
        config_option = input("Enter your options: ")
=======
        empty = check_List(maze)
        if empty == "List is occupied.":
            isDisplayingConfigurationMenu = True
            while isDisplayingConfigurationMenu != False:
                checkMaze(maze)
                displayConfigurationMenu()
                print("\n\n")
                isDisplayingConfigurationMenu = check_configuration_option(input("Enter your option: "))

>>>>>>> 8c276d4908d299e9e9685c63e4eacc36b1c91c58:MazeCode/mazegame_code.py
        return "Option 4 selected"

    elif option == "0":
        print("Exiting...")
        time.sleep(3)
        return False

    else:
        print ("Invalid option")
        return "Invalid Option"

<<<<<<< HEAD:MazeCode/mazegame.py
    
"""while run != False:
    display_menu(True)
    #option = 
    run = check_option(input ("Enter your option: "))"""
=======
if __name__ == "__main__":
    while run != False:
        display_menu(True)
        run = check_option(input ("Enter your option: "))
>>>>>>> 8c276d4908d299e9e9685c63e4eacc36b1c91c58:MazeCode/mazegame_code.py
