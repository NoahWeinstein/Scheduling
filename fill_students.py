# all of this code can be copied later into the real file
# just doing this to test and make sure it all works on its own

'''
scheduleDict is a dict of dicts
course_id:
	'popularity': popularity 		the popularity of the class
	'time': time_id					the time slot it's in
	'room': room_id					the id of the room it's in
	'room_size': room_size_int		the size of the room it's in
	'full': bool					whether or not it is full
	'students': students_list		list of the students in the course
'''
scheduleDict = {}
# flag that coursees are not full

'''list of tuples, classes with popularities, sorted by popularity'''
popularityList = []

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

'''
	takes the current course and the list of prefs
	returns a list of courses that conflict
'''
def coursesThatConflict(currentCourse, listOfPrefs):
	conflicts = []
	for course in listOfPrefs:
		if currentCourse != course && scheduleDict[currentCourse]['time'] == scheduleDict[course]['time']:
			# then it conflicts with this course
			conflicts.append(course)
	return conflicts

'''
	potential for overflow is defined by the popularity and room size
	overflow = room size - popularity
	positive or zero overflow means will not overflow
	negative overflow means has potential to overflow
	returns the course with the least potential for overflow
'''
def leastPotentialForOverflow(currentCourse, conflicts):
	# if positive or zero has no potential to overflow
	# if negative, has potential, so looking for course with overflow closest to 0
        leastOverflowValue = float("-infinity")
        leastOverflowCourse = null
        noOverflowList = []
	for course in conflicts:
                overflow = scheduleDict['room_size'] - scheduleDict['popularity']
                if overflow >= 0:
                        # if there's a course with no overflow, then choose it (random one)
                        return course
                else:
                        if overflow > leastOverflowValue:
                                leastOverflowValue = overflow
                                leastOverflowCourse = course
        return leastOverflowCourse

'''NEED TO ACCOUNT FOR IF THE COURSE IS FULL!!! (can do it here or where this is used in fill...)'''
                        


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
			# now prefs just has courses that conflict with each other
			conflicts = coursesThatConflict(course, prefs)
			'''BUT WE MIGHT NEED CONFLICTS TO INCLUDE THE CURRENT COURSE TOO
                                LIKE COURSES THAT CONFLICT WITH EACH OTHER, INCLUDING THE CURRENT'''
			# add the student to the conflicting course with the least potential for overflow
			studentsInCourse.append(leastPotentialForOverflow(course, conflicts))
			# and remove conflicts from prefs
                        for conflict in conflicts:
                                prefs.remove(conflict)
        return studentsInCourse
			

















