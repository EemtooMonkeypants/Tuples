count = 0
while count < 2:
    print(f"Enter the details for group {count+1}:")
    groupname = input("What was the name of the group?")
    size = input("How many people in the group?")
    date = input("When was the competition?")
    venue = input("Where was the competition?")
    type = input("What was the type of the medal?")
    group = (groupname, size, date, venue, type)
    count +=1
    print(group)

    if count == 2:
        break