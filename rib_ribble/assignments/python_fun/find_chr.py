def command_F(string_list,char_kb):
    new_list = []
    for i in string_list:
        if char_kb in i:
            new_list.append(i)
    print "This is the new list: "
    print new_list
        
        
        
        
        
l =['hello','world','my name','is','Anna']
char = 'o'

command_F(l, char)
