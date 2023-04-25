#define the function write
def write():
    #open mylife.txt and put the write function to it
    with open("mylife.txt", "w") as my_life:
        #put a variable to where the user will input their lines
        Line = ("Enter line:")
