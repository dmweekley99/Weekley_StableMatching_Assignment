student_choices = {
    "Cedric Diggory": ["Hufflepuff", "Ravenclaw", "Slytherin", "Gryfindor"],
    "Draco Malfoy": ["Slytherin", "Ravenclaw", "Hufflepuff", "Gryfindor"],
    "Harry Potter": ["Hufflepuff", "Ravenclaw", "Gryfindor", "Slytherin"],
    "Luna Lovegood": ["Hufflepuff", "Ravenclaw", "Slytherin", "Gryfindor"],
}

house_choices = {
    "Gryfindor": ["Harry Potter", "Cedric Diggory", "Luna Lovegood", "Draco Malfoy"],
    "Hufflepuff": ["Cedric Diggory", "Luna Lovegood", "Harry Potter", "Draco Malfoy"],
    "Ravenclaw": ["Luna Lovegood", "Harry Potter", "Cedric Diggory", "Draco Malfoy"],
    "Slytherin": ["Draco Malfoy", "Harry Potter", "Luna Lovegood", "Cedric Diggory"],
}

# Hold potential matches
possible_house = []

# Holds students that are not matched
students_unmatched = []

def initial_students_list():
    # Initialize the list of unmatched students
    for student in student_choices:
        students_unmatched.append(student)

def stable_matching():
    # While there are unmatched students
    while len(students_unmatched) > 0:
        student = students_unmatched[0]  # Take the first unmatched student
        for house in student_choices[student]:
            # Check if the house is already matched
            already_matched = [match for match in possible_house if house in match]
            
            if len(already_matched) == 0:
                # House is free, match the student
                possible_house.append([student, house])
                students_unmatched.remove(student)
                break  # Stop further proposals for this student
            else:
                # House already has a match, check preferences
                current_student = already_matched[0][0]
                # Get house's preference index
                current_student_index = house_choices[house].index(current_student)
                potential_student_index = house_choices[house].index(student)
                
                # If the house prefers the new student
                if potential_student_index < current_student_index:
                    # Replace the current student with the new student
                    already_matched[0][0] = student
                    students_unmatched.remove(student)
                    # The current student becomes unmatched
                    students_unmatched.append(current_student)
                    break


def main():
    initial_students_list()
    stable_matching()

    # Output the results with style changes to make output more readable
    print("\nSTUDENTS WITH HOUSING PREFERENCES:")
    for student in student_choices:
        print(f'    {student}: {student_choices[student]}')

    print("\nHOUSES WITH STUDENT RANKING:")
    for house in house_choices:
        print(f'    {house}: {house_choices[house]}')

    
    print("\nCOMPLETE LIST OF HOUSING ASSIGNMENTS:")
    for match in possible_house:
        print(f"    {match[0]} matched with {match[1]}")

if __name__ == "__main__":
    main()
