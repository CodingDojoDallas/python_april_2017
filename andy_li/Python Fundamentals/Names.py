# # Part I
# def names(lst):
#     for elem in lst:
#         line_str = ""
#         for key, val in elem.items():
#             line_str += val + " "
#
#         print line_str
#
#
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}]
#
# names(students)

# Part II
def names2(dict):
    for key, val in dict.items():
        print key
        for index in range(0, len(val)):
            name_str = val[index].values()[0] + " " + val[index].values()[1]
            print "{} - {} - {}".format(index + 1, name_str, len(name_str) - 1)

        # for val_lst in val1:
        #     count += 1
        #     name_str = ""
        #     for key2, val2 in val_lst.items():
        #         name_str += (val2 + " ").upper()
        #
        #     name_str_len = len(name_str) - 2
        #
        #     print str(count), "-", str(name_str) + "-", str(name_str_len)



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
  ]}

names2(users)
