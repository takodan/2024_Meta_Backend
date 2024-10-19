# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination, call):
    print(f"{" "*(len(call)-1)}start call {call}")
    
    # Base Condition
    if (disks == 1):
        print(f"{" "*(len(call)-1)}Disk {disks} moves from tower {source} to tower {destination}. #1")
        move_a_disk(disks, destination, call)
        print(f"{" "*(len(call)-1)}end call {call}")
        return

    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, helper, call + "-1")
    print(f"{" "*(len(call)-1)}continue call {call}")
    print(f"{" "*(len(call)-1)}Disk {disks} moves from tower {source} to tower {destination}. #2")
    move_a_disk(disks, destination, call)
    hanoi(disks - 1, helper, source, destination, call + "-2")
    print(f"{" "*(len(call)-1)}end call {call}")
    print()

# Driver code
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''

# For tracking Tower status
tower_A = [i+1 for i in range(disks)]
tower_B = []
tower_C = []

def move_a_disk(disk, destination, call):
    if disk in tower_A:
        tower_A.pop(0)
        if destination == "B":
            tower_B.insert(0, disk)
        else:
            tower_C.insert(0, disk)
    elif disk in tower_B:
        tower_B.pop(0)
        if destination == "A":
            tower_A.insert(0, disk)
        else:
            tower_C.insert(0, disk)
    else:
        tower_C.pop(0)
        if destination == "A":
            tower_A.insert(0, disk)
        else:
            tower_B.insert(0, disk)
    print(f"{" "*(len(call)-1)}A:{tower_A}, B:{tower_B}, C:{tower_C}")



# Actual function call
print(f"A:{tower_A}, B:{tower_B}, C:{tower_C}")
hanoi(disks, 'A', 'B', 'C', "1")