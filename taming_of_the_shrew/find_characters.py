script = open("taming_of_the_shrew.txt", 'r')

def find_character(name):
    counter = 0
    for line in script:
        if name in line:
            counter += 1
    script.seek(0)
    print(f"{counter}: {name}'s lines")


find_character("KATHERINA")
find_character("BIANCA")
find_character("WIDOW")
find_character("PEDANT")
find_character("CURTIS")
find_character("GRUMIO")
find_character("BIONDELLO")
find_character("TRANIO")
find_character("HORTENSIO")
find_character("GREMIO")
find_character("PETRUCHIO")
find_character("LUCENTIO")
find_character("VINCENTIO")
find_character("BAPTISTA")
find_character("SLY")
find_character("HOSTESS")
find_character("LORD")
find_character("FIRST HUNTSMAN")
find_character("SECOND HUNTSMAN")
find_character("SERVANT")
find_character("PLAYER")
find_character("PAGE")
find_character("MESSENGER")
