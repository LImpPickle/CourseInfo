def create_room_number_dict():
    room_numbers = {'CS101': '3004', 'CS102': '4501', 'CS103': "6755", 'NT110': '1244', 'CM241': '1441'}
    return room_numbers


def create_instructor_dict():
    instructors = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
    return instructors


def create_time_dict():
    times = {'CS101': '8:00 A.M', 'CS102': '9:00 A.M.', 'CS103': '10:00 A.M.', 'NT110': '11:00 A.M.', 'CM241': '1:00 P.M.'}
    return times

def main():
    room = create_room_number_dict();
    instructor = create_instructor_dict();
    time = create_time_dict();
    course = input('Enter in a course number: ')
    place = room[course]
    teacher = instructor[course]
    class_time = time[course]
    print("The course", course, "is at",class_time, "in room", place, "and is taught by", teacher)

main()

