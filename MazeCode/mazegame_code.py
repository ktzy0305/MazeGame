"""
Dear all, please write a unit test befor coding a function.
"""

menu = ("Read and load maze from file", "View maze", "Play maze game", "Configure current maze")
run = True
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

def check_option(option):
    if option == "1":
        return "Option 1 selected"
    elif option == "2":
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
