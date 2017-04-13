# PART ONE
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# def names(list):
#     for dict in list:
#         something = ''
#         for key, data in dict.items():
#             something += data + ' '
#
#         print something
# #         # for value in data.iteritems():
# #
#             # print key.values()
# names(students)

# PART TWOOOOOOOO
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

def names2(dict):
    for key, value in dict.items():
        count = 0
        print key
        for listy in value:
            count += 1
            # print key
            print count,'-', listy['first_name'], listy['last_name'], '-', len(listy['first_name']) + len(listy['last_name'])

names2(users)
