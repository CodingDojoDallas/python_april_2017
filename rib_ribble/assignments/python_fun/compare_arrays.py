def compare(list1,list2):
    if len(list1) != len(list2):
        print "The lists are not the same."
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            print "The list are not the same"
            return False
    print "The lists are the same"
    
list1 = []
list2 = []
compare(list1,list2)
            
    
    
