# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(x):
    if x % 2 == 0:
        return True 
    else:
        return False
       

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
is_even(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def shout(x):
    if is_even(x) == True:
        print("Even!")
    else:
        print("Odd")

shout(num)