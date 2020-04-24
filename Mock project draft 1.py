#-----------------------------------------#
# This is the mock project draft no. 1    #
# Written in Python 3.8.2                 #
# April 2020                              #
# Written by Henry T-I                    #
# Stowe school                            #
# Mr Gupta, C04A                          #
#-----------------------------------------#

#Function to check the RLE length#
def Enter_RLE(RLE_Length):
    for i in range(0, RLE_Length):
        input("Please enter line 1")
RLE_Length = 3
aline = []
for i in range (0, RLE_Length):
    line = input("Enter RLE")
    aline.append(line)
    print(aline)

for j in range (0, len(aline)):
    cstr = aline[j]
    for i in range(0, len(Cstr), 3):
        num = int(Cstr[i]+Cstr[i+1])
        print (num*Cstr[i+2], end="")
    print()
        
    
    

    
##a=[]
##
##b=input("Enter RLE")
##
##a.append[b]
##
##Cstr = "02A188"#
##
##for i in range (0, len(Cstr), 3):
##    num = int(Cstr[i]+Cstr[i+1])
##    print (num*Cstr[i+2], end="")

#Function to Display ASCII art#
##def Display_ASCII(ASCII_art):


#Function to convert ASCII art#
#def Convert_ASCII(Convert_RLE):
 #   F1 = open("LogoRLE.txt", "r")
    #print (F1.read())

  #  for i in F1.readlines():
   #     for j in range(0, len(i)-1, 3):
    #        num = int(i[j]+i[j+1])
     #       print(num*i[j+2], end="")
      #  print("\n")
    #F1.close()#


#--------------------------------------------------------------------------------------------#
# THE MAIN PROGRAM vvvvv                                                                     #
#--------------------------------------------------------------------------------------------#

#Introduction to the menu#

print("********************************************")
print("* Welcome to the Mock project program Menu *")
print("* You are able to do the following things  *")
print("* 1 - Enter RLE                            *")
print("* 2 - Display ASCII art                    *")
print("* 3 - Convert to ASCII art                 *")
print("* 4 - Quit this program                    *")                                                                               
print("********************************************")
print("")

#Sets a data variable for user input#
user_input = ""

#this is a loop that lets a menu number be entered but stops when the user chooses to quit#
while user_input != "4":
    print("Please enter a menu choice: ")
    print("Press '1' to enter the required RLE")
    print("Press '2' to display the ASCII art from the required text file")
    print("Press '3' to convert the required text file of RLE into ASCII art")
    print("Press '4' to quit the program")
    user_input = input("number: ")

    #Menu choice 1#
    if user_input == "1":
        print("How many lines of RLE compressed data would you like to enter?")
        print("It should be more than 2 lines long")
        print("If it's not, it won't work")
        RLE_Length = int(input("RLE_Length: "))
        while RLE_Length <= 2:
            RLE_Length = int(input("RLE_Length: "))
            
            

        Enter_RLE(RLE_Length)
        

    #Menu choice 2#
    elif user_input == "2":

        #Calling the Display ASCII function#
        print("Please enter the name of the text file containing the ASCII art")
        print(ASCII_art)

    #Menu choice 3#
    elif user_input == "3":

        #Calling the convert to ASCII function#
        print("Please enter the name of the text file containing the RLE data")
        print(Convert_RLE)

    #Menu choice 4 / end of loop#
    elif user_input == "4":
        print("Goodbye for now :)")
        exit

    else:
        print("Sorry! You can only choose 1, 2, 3 or 4")










