import random 
import math
import csv

# TODO add more error checking

################################################################################################################################################

print('Enter the filename of your specifications file (ex: specifications.csv): ')
filename = input()
print()
finished = False

with open(filename) as specs:
    reader = csv.reader(specs)
    rows = []
    for row in reader:
        rows.append(list(filter(lambda x: x != '', row)))

tables = list(map(int, rows[0][1:]))
seats_per_table = list(map(int, rows[1][1:]))
ideal_group_num = int(rows[2][1])
students = rows[3][1:]

group_together = []
for group in rows[4][1:]:
    if len(group.split()) > max(seats_per_table):
        print('No table has enough room for specified group of students to sit together:', group)
        print('Revise specifications and try again.')
        quit()
    group_together.append(group.split())

do_not_group = []
for pair in rows[5][1:]:
    if(len(pair.split()) > 2):
        print('"Do Not Pair" must only contain pairs of students. Revise specifications and try again.')
        quit()
    do_not_group.append(pair.split())

specific_seats = []
for spec in rows[6][1:]:
    specification = spec.split()
    for i, table in enumerate(specification[1:]):
        specification[i + 1] = int(table)
    specific_seats.append(specification)

################################################################################################################################################

def place_student(s_to_place, s_to_avoid):
    unseated = True
    count = 0
    while unseated and count < 50:
        table_num = random.randint(0, len(tables) - 1)   # pick random table
        desired_table = seating_chart[table_num]

        if desired_table.count(0) > 0 and not any(s == s_to_avoid for s in desired_table):
            # check if student has a partner
            if any(s_to_place in group for group in group_together):
                # check that there's room at the table for an additional person
                for group in group_together:
                    if s_to_place in group:
                        if desired_table.count(0) >= len(group_together[group_together.index(group)]):  # have enough room :)
                            for s in group:
                                desired_table[desired_table.index(0)] = s          

                            unseated = False
                        break

            else:
                desired_table[desired_table.index(0)] = s_to_place
                unseated = False

        count += 1
    
    if count == 50:
        print_seating_chart(seating_chart)
        print('Encountered infinite loop attempting to assign a seat to ' + s_to_place + '. Check specifications and try again.')
        quit()


def print_seating_chart(seating_chart):
    for i, table in enumerate(seating_chart):
        students = ''
        for s in table:
            if s != 0:
                students = students + s + '  '

        print('Table ' + str(tables[i]) + ':  ' + students)
        
    print()

################################################################################################################################################

# check that seats = tables
if len(tables) != len(seats_per_table):
    print('Size mismatch: Check the number of tables and seats per table.')
    quit()


# verify that there are enough seats
total_seats = sum(seats_per_table)
num_students = len(students)

if(num_students > total_seats):
    print(str(total_seats) + ' seats and ' + str(num_students) + ' students. Not enough seats for all students. Revise specifications and try again.')
    quit()


# remove tables to avoid gaps
if ideal_group_num:
    ideal_number_of_groups = math.ceil(num_students/ideal_group_num)
    while total_seats - num_students >= seats_per_table[-1] and len(tables) > ideal_number_of_groups:
        if not(any(tables[-1] in group for group in specific_seats)):
            seats_per_table = seats_per_table[:-1]
            tables = tables[:-1]

            total_seats = sum(seats_per_table)
        else:
            break


while(not finished):
    # create seating chart
    seating_chart = []
    for table in range(len(tables)):
        seating_chart.append([])

        for seat in range(seats_per_table[table]):
            seating_chart[table].append(0)


    # assign students who need specific seats
    specific_seats = sorted(specific_seats, key=len)

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
            print('Encountered infinite loop attempting to assign students who need specific seats. Try running again. If error persists, revise specifications.')
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
            print('Encountered infinite loop attempting to assign students who need to sit together. Check specifications and try again.')
            quit()


    # assign remaining students
    for student in students:
        if not any(student in table for table in seating_chart):
            place_student(student, '')


    # print seating chart
    print_seating_chart(seating_chart)

    valid_response = False
    while(not valid_response):
        print('Rerun? Enter yes (or Y) to generate a new seating chart; no (or N) to quit.')
        response = input()
        print()

        if response == 'Yes' or response == 'yes' or response == 'y' or response == 'Y':
            valid_response = True
        elif response == 'No' or response == 'no' or response == 'n' or response == 'N':
            finished = True
            valid_response = True
        else: 
            print('Invalid input. Try again.')
            print()
