class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.attendance = 'A'

students = [
    Student(722001, "Anshika Nagbanshi"),
    Student(722002, "Aisha Sidiqui"),
    Student(722003, "Mahima Manni"),
    Student(722004, "Maalav Whorra"),
    Student(722005, "Saad Malick"),
    Student(722006, "Sparsh Shukla"),
    Student(722007, "Sumati Gaur"),
    Student(722008, "Pratham Gupta"),
    Student(722009, "Pari Gupta"),
    Student(722010, "Aakansha Patel")
]

def match(n):
    for student in students:
        if n == student.id:
            student.attendance = 'P'

def absent():
    for student in students:
        if student.attendance != 'P':
            student.attendance = 'A'

while True:
    print("\n\n\t\t<-------DE-PROX ATTENDANCE------->\n\n")
    print("\tChoose :\n(1).MARK ATTENDANCE\n(2).END ATTENDANCE\n(3).Show Today's Attendance\n(4).Put Attendance\n")
    choose = int(input())
    
    if choose == 1:
      marked_count = 0
      while marked_count < len(students):
        try:
            uid = int(input("\n\nEnter your id to mark attendance:\nPress 0 to Stop attendance\t"))
            if uid == 0:
                break
            if uid < 1 or uid > 10:
                print("\n\t\tALERT!!!\nInvalid Id...you have to enter again!!!\n")
            else:
                match(uid)
                absent()
                marked_count += 1
        except ValueError:
            print("\n\t\tALERT!!!\nInvalid input...you have to enter a valid id!!!\n")

    elif choose == 2:
        print("\n\t\tThank You for Marking Attendance with DE-PROX\n\n")
        print("\t\t       <-----created by Srajan----->")
        break
    elif choose == 3:
        # pc = sum(1 for student in students if student.attendance == 'P')
        # ac = sum(1 for student in students if student.attendance == 'A')
        print("Today's Class Strength:")
        print("ID\t  Name\t    Attendance")
        for student in students:
            if student.attendance == 'P':
                print(f"{student.id}  \t  {student.name}  \t  {student.attendance}")
        print("\nThe List Of Absentees is:")
        print("ID\t  Name\t    Attendance")
        for student in students:
            if student.attendance == 'A':
                print(f"{student.id}  \t  {student.name}  \t  {student.attendance}")
        # print(f"\n\n\t--> Present : {pc}")
        # print(f"\n\n\t--> Absent : {ac}")
    elif choose == 4:
        with open("test1.xls", "w") as fp:
            fp.write("ID\t    Name\t    Attendance\n")
            for student in students:
                fp.write(f"{student.id}    \t    {student.name}  \t     {student.attendance}\n")
        print("\n\n<-----DATA ENTERED----->\n\n")
        print("\n\t\tThank You for Marking Attendance with DE-PROX\n\n")
        break
