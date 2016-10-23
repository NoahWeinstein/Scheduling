# all of this code can be copied later into the real file
# just doing this to test and make sure it all works on its own

'''
scheduleDict is a dict of dicts
course_id:
        'popularity': popularity                the popularity of the class
        'time': time_id                         the time slot it's in
        'room': room_id                         the id of the room it's in
        'room_size': room_size_int              the size of the room it's in
        'students': students_list               list of the students in the course
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
                if currentCourse != course and scheduleDict[currentCourse]['time'] == scheduleDict[course]['time']:
                        return false
        return true

'''
        takes the current course and the list of prefs
        returns a list of courses that conflict
'''
def coursesThatConflict(currentCourse, listOfPrefs):
        conflicts = []
        for course in listOfPrefs:
                if scheduleDict[currentCourse]['time'] == scheduleDict[course]['time']:
                        # then it conflicts with this course, can be itself
                        conflicts.append(course)
        return conflicts

'''
        potential for overflow is defined by the popularity and room size
        overflow = room size - popularity
        positive or zero overflow means will not overflow
        negative overflow means has potential to overflow
        returns the course with the least potential for overflow
'''
def leastPotentialForOverflow(conflicts):
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

# isNotFull will be 0 if it's full, so isNotFull is true if it's not full
def isNotFull(course, scheduleDict):
        scheduleDict[course]['room_size'] - len(scheduleDict[course]['students'])

def fillStudents(students, studentPrefs, courseTimesDict, roomDict):
        studentsInCourse = {}
        for student in students:
                prefs = studentPrefs[student]
                for course in prefs:
                        if isNotFull(course, scheduleDict):
                                if  hasNoConflicts(course, prefs):
                                        # if there's room in the course and it doesn't conflict with any other preferences
                                        if studentsInCourse[course]:
                                                studentsInCourse[course].append[student]
                                        else:
                                                studentsInCourse[course] = [student]
                                else:
                                        prefs.append(coursesThatConflict(course,prefs))
                                        # will add a list of courses that conflict in prefs)
                                for removeCourse in coursesThatConflict(course, prefs):
                                        prefs.remove(removeCourse)
                                        # will remove course and courses that conflict with it if any exist
        for student in students:
                prefs = studentPrefs[student]
                for conflictGroup in prefs:
                        # now prefs just has lists of courses that conflict with each other
                        # add the student to the conflicting course with the least potential for overflow
                        if isNotFull(course, scheduleDict):                               
                                studentsInCourse.append(leastPotentialForOverflow(conflictGroup))
                                # and remove conflicts from prefs
                                for conflict in conflicts:
                                        prefs.remove(conflict)
        return studentsInCourse
                        



'''TESTING BELOW'''










