rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

# Vacuum starts at Room A
location = 'A'

print("Initial State:")
print("Room A:", rooms['A'])
print("Room B:", rooms['B'])
print("Vacuum Location:", location)
print()

# Continue until both rooms are clean
while True:

    if rooms[location] == 'Dirty':
        print("Vacuum is in Room", location)
        print("Action: SUCK")
        rooms[location] = 'Clean'

    else:
        print("Vacuum is in Room", location)
        print("Action: MOVE")

        if location == 'A':
            location = 'B'
        else:
            location = 'A'

    print("Current State:")
    print("Room A:", rooms['A'])
    print("Room B:", rooms['B'])
    print("Vacuum Location:", location)
    print()

    # Goal Test
    if rooms['A'] == 'Clean' and rooms['B'] == 'Clean':
        print("Goal Achieved!")
        print("Both rooms are clean.")
        break