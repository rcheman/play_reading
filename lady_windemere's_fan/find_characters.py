script = open("lady_windemere's_fan.txt", 'r')

def find_character(name):
    counter = 0
    for line in script:
        if name in line:
            counter += 1
    script.seek(0)
    print(f"{counter}: {name}'s lines")


find_character("LORD WINDERMERE")
find_character("LORD DARLINGTON")
find_character("LORD AUGUSTUS LORTON")
find_character("MR. CECIL GRAHAM")
find_character("MR. DUMBY")
find_character("MR. HOPPER")
find_character("PARKER")
find_character("LADY_WINDERMERE")
find_character("DUCHESS OF BERWICK")
find_character("LADY AGATHA CARLISLE")
find_character("LADY PLYMDALE")
find_character("LADY JEDBURGH")
find_character("STUTFIELD")
find_character("COWPER-COWPER")
find_character("ERLYNNE")
find_character("ROSALIE")



"""in term " python3.9 [title]' | sort -rn"""
