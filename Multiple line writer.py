#define the function write
def write():

    #open mylife.txt and put the write function to it
    with open("mylife.txt", "w") as my_life:

        #put a variable to where the user will input their lines
        Line = ("Enter line:")
        print("")

        #to write a new line on the file
        my_life.write(Line + "\n")

        #Ask the user if they want to enter another line
        choices = input("Do you want to enter another line?(y/n):")
        
        #Do a while loop to ask the user repeatedly
        while choices == "y":
            Line = ("Enter a line:")
            print("")

        #to write a new line on the file
        my_life.write(Line + "\n")

    


