def number_list():
    i = 0
    numbers = []
    highest_number = int(raw_input("What should i go up to? "))
    increment = int(raw_input("What should i increase by? "))
    while i < highest_number:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num
