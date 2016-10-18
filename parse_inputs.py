def parse_constraints(constraints_name):
    constraints_file = open(constraints_name,'r')
    #last number of first line is number of time slots
    num_times = int(constraints_file.readline().split()[-1])

    #set up rooms array
    num_rooms = int(constraints_file.readline().split()[-1])
    rooms = {}
    for i in range(0,num_rooms):
        rooms[i+1] = int(constraints_file.readline().split()[-1])

    num_classes = int(constraints_file.readline().split()[-1])
    
    num_teachers = int(constraints_file.readline().split()[-1])
    teacher_to_classes = {x:[] for x in range(1,num_teachers+1)}
    for i in range(0,num_classes):
        line = constraints_file.readline().split()
        class_id = int(line[0])
        teacher_id = int(line[1])
        teacher_to_classes[teacher_id].append(class_id)
    return (rooms, num_classes, teacher_to_classes)

#for testing
print parse_constraints("demo_constraints.txt")
