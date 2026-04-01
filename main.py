import json

sessions = []

while True:
    print("\n1. Add Study Session")
    print("2. View Sessions")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        subject = input("Enter subject: ")
        hours = float(input("Enter hours: "))

        sessions.append({"subject": subject, "hours": hours})
        print("✅ Session added!")

    elif choice == "2":
        print("\n📚 Your Study Sessions:")
        for s in sessions:
            print(s["subject"], "-", s["hours"], "hours")

    elif choice == "3":
        print("Goodbye!")
        break