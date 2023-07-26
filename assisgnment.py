nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1





   def print_star_pattern(name):
    characters = {
        'A': ["  *  ", " * * ", "*   *", "*****", "*   *", "*   *"],
        'B': ["**** ", "*   *", "**** ", "*   *", "**** "],
        'C': [" ****", "*    ", "*    ", "*    ", " ****"],
        'D': ["**** ", "*   *", "*   *", "*   *", "**** "],
        'E': ["*****", "*    ", "**** ", "*    ", "*****"],
        'F': ["*****", "*    ", "**** ", "*    ", "*    "],
        'G': [" ****", "*    ", "*  **", "*   *", " ****"],
        'H': ["*   *", "*   *", "*****", "*   *", "*   *"],
        'I': ["*****", "  *  ", "  *  ", "  *  ", "*****"],
        'J': ["  ***", "   * ", "   * ", "*  * ", " **  "],
        'K': ["*  * ", "* *  ", "**   ", "* *  ", "*  * "],
        'L': ["*    ", "*    ", "*    ", "*    ", "*****"],
        'M': ["*   *", "** **", "* * *", "*   *", "*   *"],
        'N': ["*   *", "**  *", "* * *", "*  **", "*   *"],
        'O': [" *** ", "*   *", "*   *", "*   *", " *** "],
        'P': ["**** ", "*   *", "**** ", "*    ", "*    "],
        'Q': [" *** ", "*   *", "*   *", "*  **", " ****"],
        'R': ["**** ", "*   *", "**** ", "* *  ", "*  * "],
        'S': [" ****", "*    ", " *** ", "    *", "**** "],
        'T': ["*****", "  *  ", "  *  ", "  *  ", "  *  "],
        'U': ["*   *", "*   *", "*   *", "*   *", " *** "],
        'V': ["*   *", "*   *", " * * ", " * * ", "  *  "],
        'W': ["*   *", "*   *", "* * *", "** **", "*   *"],
        'X': ["*   *", " * * ", "  *  ", " * * ", "*   *"],
        'Y': ["*   *", " * * ", "  *  ", "  *  ", "  *  "],
        'Z': ["*****", "   * ", "  *  ", " *   ", "*****"],
        ' ': ["     ", "     ", "     ", "     ", "     "],
    }

    for row in range(5):
        for char in name.upper():
            print(characters.get(char, characters[' '])[row], end="  ")
        print()

if __name__ == "__main__":
    name = "ChatGPT"
    print_star_pattern(name)  
        
    
    
    def add_student(database):
     roll_number = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")
    database[roll_number] = {"Name": name, "Age": age, "Department": department}
    print("Student data added successfully!")

def get_student(database):
    roll_number = input("Enter Roll Number to retrieve student data: ")
    student = database.get(roll_number)
    if student:
        print("Student Information:")
        print(f"Roll Number: {roll_number}")
        print(f"Name: {student['Name']}")
        print(f"Age: {student['Age']}")
        print(f"Department: {student['Department']}")
    else:
        print("Student not found in the database.")

def main():
    database = {}
    while True:
        print("\n1. Add Student")
        print("2. Retrieve Student Information")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_student(database)
        elif choice == '2':
            get_student(database)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 