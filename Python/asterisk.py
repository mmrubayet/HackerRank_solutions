def function(*a):
    print (type(a))
    for i in range(len(a)):
        print ('Position', i, 'is', a[i])

function(4, 4, 5, 6)
