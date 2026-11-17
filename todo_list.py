tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Task Add cheyali")
    print("2. Tasks chudali")
    print("3. Task Delete cheyali")
    print("4. Exit")
    
    choice = input("Nee choice (1-4): ")

    if choice == "1":
        task = input("Task enti? ")
        tasks.append(task)
        print("Task add ayindhi!")

    elif choice == "2":
        if len(tasks) == 0:
            print("Inka em tasks levu.")
        else:
            print("Nee Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        num = int(input("Ye number task delete cheyali? "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)
            print("Task delete ayindhi!")
        else:
            print("Wrong number!")

    elif choice == "4":
        print("Bye Swetha!")
        break

    else:
        print("1 nundi 4 varaku ivvu.")
