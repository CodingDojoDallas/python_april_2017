def whatisit(test):
    if type(test) is int:
        if (test) <= 10:
            print "Small Number"
        else:
            print "Big Number!"
    elif type(test) is str:
        if len(test) <= 100:
            print "Short Sentence"
        else:
            print "Long Sentence"
    elif type(test) is list:
        if len(test) <=10:
            print "Short List"
        else:
            print "Big List!"
        
whatisit([1,2,43,556,4,5,6,3,2,3,67,8,"sdflk"])


