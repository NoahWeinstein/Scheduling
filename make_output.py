def make_output(out_dict,output_name):
"""
Given an output dictionary that looks like {course_number : [Room, Teacher, Time, students]} makes an a file at output_name that is essentially a .tsv
"""
	with open(output_name,'w') as f:
		output = ["Course\tRoom\tTeacher\tTime\tStudents"]
		for course in out_dict:
			line_out = [str(course)]
			line_out.extend([str(info) for info in out_dict[course]])
			output.append(("\t").join(line_out))
		f.write(("\n").join(output))

#This is just a little test to make sure it is working as desired
#out_dict = {1:[1,2,2,[2,3,4,7,8,9,10]],2:[3,2,4,[4,9]]}
#print out_dict
#print make_output(out_dict, "outtt.txt")
			
		
