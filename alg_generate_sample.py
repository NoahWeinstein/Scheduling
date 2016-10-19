from random import randint
import argparse

import parse_inputs

parser = argparse.ArgumentParser(description='Create a schedule')
parser.add_argument('constraints', type=str, nargs=1,
                    help='Name of constraints file.')
parser.add_argument('preferences', type=str, nargs=1,
                    help='Name of student preferences file.')
parser.add_argument('output', type=str, nargs = 1,
                    help='Name of output file.')

args = parser.parse_args()

constraints = parse_inputs.parse_constraints(args.constraints[0])
rooms = constraints[0]
courses = constraints[1]
teachers = constraints[2]
times = constraints[3]

studentPrefs = parse_inputs.parse_prefs(args.preferences[0])
print rooms, courses, teachers, times, studentPrefs

"""
def make_student_dictionary(c,s):
	student_dictionary = {}
	for student in range(0,s):
		student_dictionary[student]=[randint(0,c)]
		while len(student_dictionary[student]) != 4:
			new_class = randint(0,c)
			if new_class not in student_dictionary[student]:
				student_dictionary[student].append(new_class)
	return student_dictionary


def make_teachers(c):
	teachers={}
	n = 0
	for cc in range(0,c/2):
		teachers[cc]= [n,n+1]
		n+=1
	return teachers

"""
	
def make_conflict_matrix(student_dictionary,c):
	conflict_dict = {}
	for i in range(0,c):
		for j in range(0,c):
			conflict_dict[(i,j)] = 0
			for student in student_dictionary:
				if i in  student_dictionary[student] and j in  student_dictionary[student]:
					conflict_dict[(i,j)] += 1
	return conflict_dict
	

def assign_rooms(class_times_dict, rooms, con_mat):
    class_to_room = {}
    big_rooms = sorted(rooms, reverse = True)
    for slot in class_times_dict:
        #sort descending based on popularity
        pop_slot = sorted(slot, key = lambda x: con_mat[(x,x)], reverse = True)
        counter = 0
        for pop_class in pop_slot:
            class_to_room[pop_class] = big_rooms[counter]
            counter += 1
    return class_to_room


def make_schedule(class_times,rooms,students,teachers,con_mat,c):
	popularity = []	
	for i in range(0,c):
		popularity.append((i,con_mat[(i,i)]))
	popularity.sort(key= lambda student: student[1])
	print popularity
	for key in class_times:
		class_times[key].append(popularity.pop())
	print class_times
	while len(popularity) != 0:
		current = popularity.pop()
		min_conflict = (55,1000000)
		for time in class_times:
			conflict = 0
			for item in class_times[time][1:]:
				conflict += con_mat[(item[0],current[0])]
			if conflict<min_conflict[1]:
				min_conflict = (time, conflict)
		class_times[min_conflict[0]].append(current)
		class_times[min_conflict[0]][0] += min_conflict[1]
	print class_times
	total = 0
	for key in class_times:
		total += class_times[key][0]
	print "Total Conflict:",total		

def courseAssignment(courses, rooms, times, teachers, studentPrefs):
    return

c = 100
 	

#students = make_student_dictionary(c,1000)

con_mat = make_conflict_matrix(studentPrefs,c)

#teachers = make_teachers(c)


rooms = [20, 30, 30, 40]

class_times = {1:[0],2:[0],3:[0],4:[0],5:[0],6:[0]}

#make_schedule(class_times,rooms,students,teachers,con_mat,c)
