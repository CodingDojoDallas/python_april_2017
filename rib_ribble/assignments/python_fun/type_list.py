def typelist(user):
    num = 0
    my_string = ""
    count_int = 0
    for i in user:
        if type(i) == str:
            my_string += i + " "
        elif type(i) == int:
            num += i
            count_int += 1
                
    if my_string != "" and count_int > 0:
        print "The array you entered is a mixed type"
        print "String is: " +my_string
        print "Sum is: " +str(num)
    elif count_int == 0:
        print "The list you entered is a string type"
        print "String is: " +my_string
    else:
        print "The list you entered is an integer type"
        print "Sum is: " +str(num)
    
        
typelist(['magical unicorns',19,'hello',98.98,'world'])
typelist([1,345,789,-26565354,678])
typelist(["s","d","f"])
         