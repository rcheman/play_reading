script = open("twelfth_night.txt", 'r')

def find_character(name):
    counter = 0
    for line in script:
        if name in line:
            counter += 1
    script.seek(0)
    print(f"{counter}: {name}'s lines")


find_character("VIOLA")
find_character("DUKE")
find_character("OLIVIA")
find_character("SEBASTIAN")
find_character("MALVOLIO")
find_character("CLOWN")
find_character("CAPTAIN")
find_character("CURIO")
find_character("SIR TOBY")
find_character("MARIA")
find_character("VALENTINE")
find_character("SIR ANDREW")
find_character("ANTONIO")
find_character("FABIAN")
find_character("SERVANT")
find_character("FIRST OFFICER")
find_character("SECOND OFFICER")
find_character("PRIEST")
