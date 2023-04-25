import random

#define the function write
def write():

    #open mylife.txt and put the write function to it
    with open("mylife.txt", "w") as my_life:

        #put a variable to where the user will input their lines
        Line = input("Enter line:")
        print("")

        #to write a new line on the file
        my_life.write(Line + "\n")

        #Ask the user if they want to enter another line
        choices = input("Do you want to enter another line?(y/n):")
        
        #make a comment
        if choices == "y":
            comments = ["You're doing great", "Great Job!", "That last line was beautiful", "A poet in the making "]
            print(random.choice(comments))
            
        else:
             print("Thank you!")
            
        
        #Do a while loop to ask the user repeatedly
        while choices == "y":
            print("")
            Line = input("Enter a line:")
            
            #to write a new line on the file
            my_life.write(Line + "\n")

            #ask again the user if they want to continue
            choices = input("Do you want to enter another line?(y/n):")

            #comments
            comments = ["You're doing great", "Great Job!", "That last line was beautiful", "A poet in the making "]
            print(random.choice(comments))
    
    #close the file
    my_life.close()

#call the function
write()


