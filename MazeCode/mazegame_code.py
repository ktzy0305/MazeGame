"""
Dear all, please write a unit test befor coding a function.
"""

import csv

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
        checkMaze(maze)
        return (errorMsg)
    else:
        errorMsg = "List is empty."
        print (errorMsg)
        return (errorMsg)

#try_list=[["X","O","A","B"], ["1","2"]]
#try_empty = []
#verify_list=[["X","O","A","B"], ["X","O","A","B"]]

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
        
        if total != type_total:
            print ("The list is not a maze.")
            maze_check = False
            return "The list is not a maze."
        
    if maze_check:
        for i in list:
            print(i)
    return "The list is a maze."

def check_option(option):
    if option == "1":
        file = input("Enter the name of the data file: ")
        check_filename(file)
        return "Option 1 selected"
    
    elif option == "2":
        check_List(maze)
        return "Option 2 selected"
    elif option == "3":
        return "Option 3 selected"
    elif option == "4":
        return "Option 4 selected"
    elif option == "0":
        print("Exiting...")
        return False
    else:
        print ("Invalid option")
        return "Invalid Option"

    
while run != False:
    display_menu(True)
    option = input ("Enter your option: ")
    run = check_option(option)