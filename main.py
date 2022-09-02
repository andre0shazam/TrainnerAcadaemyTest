import random

cycle1 = {"group1": ["Laura",
                     "Pedro",
                     "João",
                     "Vinicius"],
          "group2": ["Carlos",
                     "Maria",
                     "Leonardo",
                     "Ana"],
          "group3": ["Daniela",
                     "Marcos",
                     "Wesley",
                     "Luiza"],
          "group4": [
              "Daiane",
              "Felipe",
              "Teodoro",
              "Helena"],

          "group5": ["Natalia",
                     "Beatriz",
                     "Eduardo",
                     "Caio"]
          }

cycle2 = {"group1": [
    "Teodoro",
    "Daiane",
    "Luiza"
],
    "group2": [
        "Carlos",
        "João",
        "Helena"
    ],
    "group3": [
        "Daniela",
        "Pedro",
        "Caio"
    ],
    "group4": [
        "Leonardo",
        "Maria",
        "Laura"
    ],
    "group5": [
        "Beatriz",
        "Marcos",
        "Vinicius"
    ],
    "group6": [
        "Natalia",
        "Felipe",
        "Eduardo"
    ],
    "group7": [
        "Ana",
        "Wesley"
    ]}


def drawnStudents():
    """
    This method randomly selects two students from cycle 1.
    The group and the student of this group are randomly selected.
    :return: student1: first student selected, student2: second student selected
    """
    student1 = cycle1["group" + str(random.randint(1, 5))][random.randint(0, 3)]
    student2 = cycle1["group" + str(random.randint(1, 5))][random.randint(0, 3)]
    return student1, student2


def randomStudents(studentsVector):
    """
    This method populates the studentsVector array.
    It is checked if any students will be entered again to avoid repetition.
    When the verification is finished, the candidate students are inserted in the studentsVector vector
    :param studentsVector: vector containing Academy students
    """

    students = drawnStudents()

    if students[0] != students[1]:
        if len(studentsVector) == 0:
            studentsVector.append(students[0])
            studentsVector.append(students[1])

        else:
            if students[0] not in studentsVector and students[1] not in studentsVector:
                studentsVector.append(students[0])
                studentsVector.append(students[1])
            else:
                randomStudents(studentsVector)
    else:
        randomStudents(studentsVector)


def checar_Ciclos(students):
    """
    This method checks if the students selected in the get_two_students() method
    are not together in any group from previous cycles
    :param students: array containing the students candidates for the pair
    :return: check: Boollean with value True if it passes the check and False if it fails
    """
    cycles = [cycle1, cycle2]
    check = True
    for cycle in cycles:
        for group, valor in cycle.items():
            if students[0] in cycle[group] and students[1] in cycle[group]:
                check = False
    return check


def pairChecking(duos, students):
    """
    This method checks if the selected students are not already inside the duos array.
    :param duos: array containing the duos that have already been selected
    :param students: array containing the students candidates for the pair
    :return: True if it passes the check and False if it doesn't
    """
    for pair in duos:
        if students[0] in pair or students[1] in pair:
            return False
    return True


def registerDuo(duos, students):
    """
    Registers the candidate students in the duos array.
    :param duos: array containing the duos that have already been selected
    :param students: array containing the students candidates for the pair
    """
    duos.append(students)


def get_two_students(studentsVector):
    """
    This method selects two random students from the studentsVector vector
    :param studentsVector:
    :return: member1: first candidate student; member2: second candidate student
    """
    member1 = studentsVector[random.randint(0, 19)]
    member2 = studentsVector[random.randint(0, 19)]

    return member1, member2


def defineMembers(studentsVector, duos):
    """
    This method has the function of defining the members of all duos
    :param studentsVector: Vector with each student in the course
    :param duos: array that will hold the duos formed by the method
    """

    students = get_two_students(studentsVector)

    if students[0] != students[1]:
        if len(duos) == 0:
            checkCycle = checar_Ciclos(students)
            if checkCycle:
                registerDuo(duos, students)
            else:
                defineMembers(studentsVector, duos)
        else:
            pairCheck = pairChecking(duos, students)
            if pairCheck:
                checkCycle = checar_Ciclos(students)
                if checkCycle:
                    registerDuo(duos, students)
                else:
                    defineMembers(studentsVector, duos)
            else:
                defineMembers(studentsVector, duos)
    else:
        defineMembers(studentsVector, duos)


def setDoubles():
    """
    Defines the duos that will be formed in cycle 3
    """
    studentsVector = []
    duos = []

    for a in range(10):
        randomStudents(studentsVector)
    for b in range(10):
        defineMembers(studentsVector, duos)

    for pair in duos:
        print(pair)


if __name__ == '__main__':
    print(setDoubles())
