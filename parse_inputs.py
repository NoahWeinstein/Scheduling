def parse_constraints(constraints_name):
    constraints_file = open(constraints_name,'r')
    #last number of first line is number of time slots
    num_times = int(constraints_file.readline().split()[-1])

    #set up rooms array
    num_rooms = int(constraints_file.readline().split()[-1])
    rooms = {}
    for i in range(0,num_rooms):
        rooms[i+1] = int(constraints_file.readline().split()[-1])

    print rooms
    return

#for testing
parse_constraints("demo_constraints.txt")
