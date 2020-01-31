"""
Dear all, please write a unit test befor coding a function.
"""

import csv
import time

menu = ("Read and load maze from file", "View maze", "Play maze game", "Configure current maze")
run = True
maze = []

#Display menu function
def display_menu(check):
    if check == True:
        print('\n==========\nMAIN MENU \n==========')#to print admin menu heading
        for i, item in enumerate(menu,1):
            print([i],'',item)#to print admin menu choice '' is used for formattig, to format to the same as the sample
        print()# to print a space in between the last choice of Admin Menu and the heading of Rider Menu
        print('[0]  Exit Maze') #to print out the rider menu and choices
        return "Displaying Menu"
    else:
        return "Invalid menu"

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
    if len(maze) != 0:
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
                row =2
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

    
def  current_location(maze_structure):
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

#try_list=[["X","O","A","B"], ["1","2"]]
#try_empty = []
#verify_list=[["X","O","A","B"], ["X","O","A","B"]]



def check_option(option):
    if option == "1":
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
        return "Option 4 selected"
    elif option == "0":
        print("Exiting...")
        time.sleep(3)
        return False
    else:
        print ("Invalid option")
        return "Invalid Option"

    
while run != False:
    display_menu(True)
    #option = 
    run = check_option(input ("Enter your option: "))
