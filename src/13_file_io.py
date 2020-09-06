"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

f = open("src/foo.txt", "r")
for x in f:
  print(x)
f.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
haiku = ["Like the moon over", "the day my genius and brawn", "are lost on these fools", "~ Bowser's Haiku"]


b = open("src/bar.txt", "x")
for line in haiku:
    b.write(line)
    b.write("\n")
b.close()

c = open("src/bar.txt", "r")
for x in c:
    print(x)
c.close()