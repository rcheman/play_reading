import sys

# get script text from command line
script = open(sys.argv[1], 'r')

# get user input for the numebr of characters
num_char = int(input("Enter the number of characters: "))

# declare character list for names and lines
characters = []
n = 0
# create character class
class Character:
    def __init__(self, name, lines):
        self.name = name
        self.lines = lines

    def assign_name(self):
        characters.append(self)
    def __str__(self):
        return self.name + str(self.lines)

# match character name to script and match lines
def find_character(name, lines, k):
    lines = 0
    for line in script:
        if name.upper() in line:
            lines += 1
    # return to the beginning of the script for next character
    script.seek(0)
    characters[k].lines = lines

# key for sort to sort by number of lines
def sort_lines(character):
    return character.lines

# get user input for character names
for i in range(num_char):
    inputname = Character(input("Character name: "), 0)
    inputname.assign_name()
    n += 1

# declare variable to track index in characters
k = 0
# iterate through all the characters in the play, putting their lines in the characters list with their name
for i in range(num_char):
    find_character(characters[k].name, characters[k].lines, k)
    k += 1

# sort characters list by line number
characters.sort(reverse=True, key=sort_lines)

# print out character list in order
m =0
for i in range(num_char):
    print(f"{characters[m].lines}: {characters[m].name.upper()}'s lines")
    m += 1


