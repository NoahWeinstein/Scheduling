# all of this code can be copied later into the real file
# just doing this to test and make sure it all works on its own


'''
        takes a course and list of coursees and sees if the course conflicts with the others in the list
        listOfPrefs given does not include current course
        returns a boolean
'''
def hasNoConflicts(currentCourse, listOfPrefs, courseDict):
        # check if their time_id is the same
        for course in listOfPrefs:
                # make sure currentCourse != course bc that'll have the same time
                if currentCourse != course and courseDict[currentCourse]['time'] == courseDict[course]['time']:
                        return False
        return True

'''
        takes the current course and the list of prefs
        returns a list of courses that conflict
'''
def coursesThatConflict(currentCourse, listOfPrefs, courseDict):
        conflicts = []
        for course in listOfPrefs:
                if courseDict[currentCourse]['time'] == courseDict[course]['time']:
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
def leastPotentialForOverflow(conflicts, courseDict):
        # if positive or zero has no potential to overflow
        # if negative, has potential, so looking for course with overflow closest to 0
        leastOverflowValue = float("-infinity")
        leastOverflowCourse = null
        noOverflowList = []
        for course in conflicts:
                overflow = courseDict['roomSize'] - courseDict['popularity']
                if overflow >= 0:
                        # if there's a course with no overflow, then choose it (random one)
                        return course
                else:
                        if overflow > leastOverflowValue:
                                leastOverflowValue = overflow
                                leastOverflowCourse = course
        return leastOverflowCourse

# isNotFull will be 0 if it's full, so isNotFull is true if it's not full
def isNotFull(course, courseDict):
        return courseDict[course]['roomSize'] - len(courseDict[course]['students'])

def fillStudents(studentPrefs, courseDict):
        for student in studentPrefs:
                prefs = studentPrefs[student]
                for course in prefs:
                        if isNotFull(course, courseDict):
                                if  hasNoConflicts(course, prefs, courseDict):
                                        # if there's room in the course and it doesn't conflict with any other preferences
                                        courseDict[course]['students'].append(student)
                                else:
                                        prefs.append(coursesThatConflict(course, prefs, courseDict))
                                        # will add a list of courses that conflict in prefs)
                                for removeCourse in coursesThatConflict(course, prefs, courseDict):
                                        prefs.remove(removeCourse)
                                        # will remove course and courses that conflict with it if any exist
        for student in studentPrefs:
                prefs = studentPrefs[student]
                for conflictGroup in prefs:
                        # now prefs just has lists of courses that conflict with each other
                        # add the student to the conflicting course with the least potential for overflow
                        if isNotFull(course, courseDict):                               
                                studentsInCourse.append(leastPotentialForOverflow(conflictGroup, courseDict))
                                # and remove conflicts from prefs
                                for conflict in conflicts:
                                        prefs.remove(conflict)
                        



'''TESTING BELOW'''


# QUESTION: WHERE IS SCHEDULE DICT? IS IT IN THE FUNCTION OR IS IT JUST IN OUR CODE
'''
courseDict is a dict of dicts
courseId:
        'popularity': popularity                the popularity of the class
        'time': time_id                         the time slot it's in
        'room': room_id                         the id of the room it's in
        'roomSize': room_size_int              the size of the room it's in
        'students': students_list               list of the students in the course
                                                        this gets appended with our fill students
'''
#sample courseDict
courseDict = {        1: {    'popularity': 20,
                                'time': 1,
                                'room': 1,
                                'roomSize': 20},
                        2: {    'popularity': 15,
                                'time': 2,
                                'room': 1,
                                'roomSize': 20},
                        3: {    'popularity': 15,
                                'time': 3,
                                'room': 1,
                                'roomSize': 20},
                        4: {    'popularity': 10,
                                'time': 4,
                                'room': 1,
                                'roomSize': 20},
                        5: {    'popularity': 15,
                                'time': 1,
                                'room': 2,
                                'roomSize': 10},
                        6: {    'popularity': 10,
                                'time': 2,
                                'room': 2,
                                'roomSize': 10}
                }










