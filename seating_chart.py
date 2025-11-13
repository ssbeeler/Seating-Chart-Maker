import random 
import math

################################################################################################################################################
################################################################################################################################################

tables = [1, 2, 3, 4, 5, 6, 7, 8, 9]
seats_per_table = [3, 3, 3, 3, 3, 3, 3, 3, 2]
ideal_group_num = 3

students = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

do_not_group = [['A', 'B'], ['C', 'D'], ['E', 'F']]
group_together = [['A','T'], ['F', 'G']]
specific_seats = [['A', 1, 2, 3], ['U', 4, 5]]

################################################################################################################################################
################################################################################################################################################


def place_student(s_to_place, s_to_avoid):
    unseated = True
    count = 0
    while unseated and count < 50:
        table_num = random.randint(0, len(tables) - 1)   # pick random table
        desired_table = seating_chart[table_num]

        if desired_table.count(0) > 0 and not any(s == s_to_avoid for s in desired_table):
            desired_table[desired_table.index(0)] = s_to_place
            unseated = False

        count += 1
    
    if count == 50:
        print('Impossible specifications. Check input parameters.')
        quit()


# check that seats = tables
if len(tables) != len(seats_per_table):
    print("Size mismatch: Check the number of tables and seats per table.")
    quit()

# TODO check that students don't appear multiple times in group_together
# TODO add error checking

# remove tables to avoid gaps
total_seats = sum(seats_per_table)
num_students = len(students)

num_groups = math.ceil(num_students/ideal_group_num)
ideal_num_seats = num_groups * ideal_group_num

while total_seats - ideal_num_seats >= seats_per_table[-1]:
    seats_per_table = seats_per_table[:-1]
    tables = tables[:-1]

    total_seats = sum(seats_per_table)


# sort lists
do_not_group = sorted(do_not_group, key=len)
group_together = sorted(group_together, key=len)
specific_seats = sorted(specific_seats, key=len)


# create seating chart
seating_chart = []
for table in range(len(tables)):
    seating_chart.append([])

    for seat in range(seats_per_table[table]):
        seating_chart[table].append(0)


# assign students who need specific seats
for i in specific_seats:
    unseated = True
    count = 0
    while unseated and count < 50: 
        student = i[0]
        seat = random.randint(0, len(i) - 2)   # get random seat 
        table_num = i[seat + 1] - 1   # adjusted table number (index of desired table)
        desired_table = seating_chart[table_num]

        if desired_table.count(0) > 0:  # if table has empty seat
            # check if student has a partner
            if any(student in group for group in group_together):
                # check that there's room at the table for an additional person
                for group in group_together:
                    if student in group:
                        if desired_table.count(0) >= len(group_together[group_together.index(group)]):  # have enough room :)
                            for s in group:
                                desired_table[desired_table.index(0)] = s          

                            unseated = False
                        break

            else:
                desired_table[desired_table.index(0)] = student
                unseated = False
        
        count += 1
    
    if count == 50:
        print('Impossible specifications. Check input parameters.')
        quit()


# assign students who need to sit together
for group in group_together:
    if any(group[0] in table for table in seating_chart):
        continue

    unseated = True
    count = 0
    while unseated and count < 50:
        table_num = random.randint(0, len(tables) - 1)   # pick random table
        desired_table = seating_chart[table_num]

        if desired_table.count(0) >= len(group):
            for s in group:
                desired_table[desired_table.index(0)] = s
            unseated = False

        count += 1
    
    if count == 50:
        print('Impossible specifications. Check input parameters.')
        quit()


# assign students who cannot sit together 
for group in do_not_group:
    s1 = group[0]
    s2 = group[1]

    if any(s1 in table for table in seating_chart):
        if any(s2 in table for table in seating_chart):
            # both students already seated
            continue
        
        # student 1 seated, student 2 not seated
        place_student(s2, s1)
    
    elif any(s2 in table for table in seating_chart):
        # student 2 seated, student 1 not seated
        place_student(s1, s2)

    else:
        # neither student seated 
        place_student(s1, '')

        # student 1 seated, student 2 not seated
        place_student(s2, s1)


# assign remaining students
for student in students:
    if not any(student in table for table in seating_chart):
        place_student(student, '')


# print seating chart
for i, table in enumerate(seating_chart):
    students = ''
    for s in table:
        if s != 0:
            students = students + s + '  '

    print('Table ' + str(tables[i]) + ':  ' + students)
