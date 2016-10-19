# all of this code can be copied later into the real file
# just doing this to test and make sure it all works on its own

'''
scheduleDict is a dict of dicts
course_id:
	'time': time_id					the time slot it's in
	'room': room_id					the id of the room it's in
	'room_size': room_size_int		the size of the room it's in
	'full': bool					whether or not it is full
	'students': students_list		list of the students in the course
'''
scheduleDict = {}
# flag that coursees are not full

'''
	takes a course and list of coursees and sees if the course conflicts with the others in the list
	listOfPrefs given does not include current course
	returns a boolean
'''
def hasNoConflicts(currentCourse, listOfPrefs):
	# check if their time_id is the same
	for course in listOfPrefs:
		# make sure currentCourse != course bc that'll have the same time
		if currentCourse != course && scheduleDict[currentCourse]['time'] == scheduleDict[course]['time']:
			return false
	return true

def fill_students(students, studentPrefs, courseTimesDict, roomDict):
	studentsInCourse = {}
	for student in students:
		prefs = studentPrefs[student] # rename for nicer code? doesn't matter...
		for course in prefs:
			if !scheduleDict[course]['full'] && hasNoConflicts(course, prefs):
				# if there's room in the course and it doesn't conflict with any other preferences
				if studentsInCourse[course]:
					studentsInCourse[course].append[student]
				else:
					studentsInCourse[course] = [student]
				prefs.remove(course)
	for student in students:
		prefs = studentPrefs[student]
		for course in prefs:
			# now prefs just has courses that conflict


















