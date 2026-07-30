import os

while True:
    print("\n========== FILE OPERATOR PROJECT ==========")
    print("1. Create File")
    print("2. Write File")
    print("3. Read File")
    print("4. Append Data")
    print("5. Rename File")
    print("6. Delete File")
    print("7. Exit")
    print("==========================================")

    choice = int(input("Enter your choice: "))

    # 1. Create File
    if choice == 1:
        filename = input("Enter file name: ")

        with open(filename, "w") as file:
            pass

        print("File created successfully!")

    # 2. Write File
    elif choice == 2:
        filename = input("Enter file name: ")
        data = input("Enter data to write: ")

        with open(filename, "w") as file:
            file.write(data)

        print("Data written successfully!")

    # 3. Read File
    elif choice == 3:
        filename = input("Enter file name: ")

        if os.path.exists(filename):
            with open(filename, "r") as file:
                data = file.read()

            print("\n----- File Data -----")
            print(data)
            print("---------------------")
        else:
            print("File does not exist!")

    # 4. Append Data
    elif choice == 4:
        filename = input("Enter file name: ")
        data = input("Enter data to append: ")

        with open(filename, "a") as file:
            file.write("\n" + data)

        print("Data appended successfully!")

    # 5. Rename File
    elif choice == 5:
        old_name = input("Enter old file name: ")
        new_name = input("Enter new file name: ")

        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            print("File renamed successfully!")
        else:
            print("File does not exist!")

    # 6. Delete File
    elif choice == 6:
        filename = input("Enter file name: ")

        if os.path.exists(filename):
            os.remove(filename)
            print("File deleted successfully!")
        else:
            print("File does not exist!")


    # 7. Exit
    elif choice == 7:
        print("Thank you for using File Operator Project!")
        break

    else:
        print("Invalid choice! Please enter 1 to 7.")


