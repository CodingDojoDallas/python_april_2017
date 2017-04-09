def names(students):

	for student in students:
		print student['first_name'] + " "+ student['last_name']


students = [
	{'first_name':  'Michael', 'last_name' : 'Jordan'},
	{'first_name' : 'John', 'last_name' : 'Rosales'},
	{'first_name' : 'Mark', 'last_name' : 'Guillen'},
	{'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names2(users):

	for key,value in users.iteritems():
		tracked_num = 0 
		print key
		for user in value:
			tracked_num += 1
			print str(tracked_num) + " - " + user['first_name'] +" "+ user['last_name'] + " " + str(len(user['first_name']) + len(user['last_name']))

users = {
	'Students': [
		{'first_name':  'Michael', 'last_name' : 'Jordan'},
     	{'first_name' : 'John', 'last_name' : 'Rosales'},
     	{'first_name' : 'Mark', 'last_name' : 'Guillen'},
     	{'first_name' : 'KB', 'last_name' : 'Tonel'}
  	],
 	'Instructors': [
     	{'first_name' : 'Michael', 'last_name' : 'Choi'},
     	{'first_name' : 'Martin', 'last_name' : 'Puryear'}
  	]
 }

names2(users)	