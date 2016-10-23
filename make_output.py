def make_output(out_dict,output_name):
	"""
	Given an output dictionary that looks like {course_number : [Room, Teacher, Time, students]} makes an a file at output_name that is essentially a .tsv
	"""
	with open(output_name,'w') as f:
		output = ["Course\tRoom\tTeacher\tTime\tStudents"]
		for course in out_dict:
			line_out = [str(course)]
			rtts_list = [
				str(out_dict[course]["Room"]),
				str(out_dict[course]["Teacher"]),
				str(out_dict[course]["Time"]),
				" ".join([str(item) for item in out_dict[course]["Students"]])
				]
			line_out.extend(rtts_list)
			output.append(("\t").join(line_out))
		f.write(("\n").join(output))

#This is just a little test to make sure it is working as desired
#out_dict = {1:{"Room":1,"Teacher":2,"Time" :2, "Students" :[2,3,4,7,8,9,10]},2:{"Room":3,"Teacher" : 2, "Time" : 4, "Students" : [4,9]}}
#print out_dict
#print make_output(out_dict, "outtt.txt")
			
		
