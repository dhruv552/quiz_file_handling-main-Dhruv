login_status = False
usid = []
pa = []
uid_pwd = {}
uid_marks = {}
user_name = ""
marks = 0

# Attempt Quiz
def attempt_quiz():
    if login_status:
        global marks
        while True:
            print("\nChoose a quiz topic:\n 1. DBMS\n 2. DSA\n 3. Python\n 0. Exit")
            ch = int(input("Enter your choice for quiz: "))

            if ch == 1:
                with open("dbms.txt", 'r') as file:
                    data = file.readlines()
            elif ch == 2:
                with open("dsa.txt", 'r') as file:
                    data = file.readlines()
            elif ch == 3:
                with open("python.txt", 'r') as file:
                    data = file.readlines()
            elif ch == 0:
                print("\nYour Total Marks =", marks)
                break
            else:
                print("Invalid choice, please select again.")
                continue

            questions = []
            parsed_data = []
            answers = {}
            for line in data:
                questions.append(line.strip())
            for question in questions:
                parts = question.split(",")
                parsed_data.append(parts)
                answers[parts[0]] = parts[-1]

            for i, question in enumerate(parsed_data):
                print(f"\nQuestion {i + 1}: {question[0]}")
                for j, option in enumerate(question[1:-1], start=1):
                    print(f"{j}: {option}")
                user_answer = int(input("Enter the option number: "))
                if answers[question[0]] == question[user_answer]:
                    marks += 1
                    print("Correct!\n")
                else:
                    print("Incorrect.\n")

            print("Want to try another quiz? Select an option from the menu above.")

        if user_name not in usid:
            with open("marks.txt", 'a') as file:
                file.write(f"{user_name},{marks}\n")
        else:
            marks_dict = {}
            with open("marks.txt", 'r') as file:
                existing_data = file.readlines()

            for line in existing_data:
                user, score = line.strip().split(",")
                if user == user_name:
                    marks_dict[user] = marks
                else:
                    marks_dict[user] = int(score)

            with open("marks.txt", "w") as file:
                for user, score in marks_dict.items():
                    file.write(f"{user},{score}\n")
    else:
        print("\nPlease login or register first.\n")


# Register
def register():
    print("\n------- Registration -------")
    name = input("Enter your name: ")
    uid = input("Create a username: ").lower()
    if uid in usid:
        print("\nUsername already exists. Please choose a different username or log in.")
    else:
        pwd = input("Create your password: ").lower()
        enroll = input("Enter your enrollment number: ").lower()
        with open("registration.txt", "a") as reg_file:
            reg_file.write(f"{name},{enroll},{uid},{pwd}\n")
        with open("id-pass.txt", 'a') as cred_file:
            cred_file.write(f"{uid},{pwd}\n")


# Login
def login():
    global login_status
    global user_name
    is_authenticated = False

    with open("id-pass.txt", 'r') as file:
        credentials = file.readlines()

    while not is_authenticated:
        user_id = input("Enter your username: ").lower()
        if not credentials:
            print("\nNo users registered yet. Please register first.")
            break
        else:
            for line in credentials:
                uid, pwd = line.strip().split(",")
                usid.append(uid)
                pa.append(pwd)
                uid_pwd[uid] = pwd

            if user_id in usid:
                user_name = user_id
                while not is_authenticated:
                    password = input("Enter your password: ").lower()
                    if uid_pwd[user_id] == password:
                        login_status = True
                        is_authenticated = True
                    else:
                        print("Incorrect password. Try again.")
            else:
                print("\nUsername not found. Please register first.")
                break


# Profile
def profile():
    if login_status:
        print("\nUser Information:")
        with open("registration.txt", "r") as file:
            data = file.readlines()

        for line in data:
            name, enrollment, uid, _ = line.strip().split(",")
            if uid == user_name:
                print(f"Name: {name}")
                print(f"Enrollment Number: {enrollment}")
                print(f"Username: {uid}")
                print("Password: ****")

        with open("marks.txt", 'r') as file:
            scores = file.readlines()

        for line in scores:
            uid, score = line.strip().split(",")
            if uid == user_name:
                print(f"Marks: {score}")
    else:
        print("\nPlease login or register first.\n")


# Exit
def exit_program():
    print("Logging out... Goodbye!")


# Main
def main():
    print("--------- Welcome to the Quiz Application ---------")
    while True:
        if login_status:
            print("\nChoose an option:\n 1. Profile\n 2. Attempt Quiz\n 3. Logout")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                profile()
            elif choice == 2:
                attempt_quiz()
            elif choice == 3:
                exit_program()
                break
            else:
                print("Invalid choice, please try again.")
        else:
            print("\n--- Welcome ---")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                register()
            elif choice == 2:
                login()
            elif choice == 3:
                exit_program()
                break
            else:
                print("Invalid choice, please try again.")


# Run the program
main()
