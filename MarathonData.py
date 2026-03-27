## marathon runners names and time record

def main():
    keep_running = True
    test_subjects = []
    while keep_running:
        print_menu()
        choice = input("Your Choice:  ")
        if choice == "a":
            test_subjects.append(new_test_subject())
        elif choice == "s":
            print_test_subjects(test_subjects)
        elif choice == "r":
            filename = input("Filename: ")
            test_subjects = read_data(filename)
        elif choice == "w":
            filename = input("Filename: ") 
            write_data(test_subjects, filename)
        elif choice == "q":
            keep_running = False
        elif choice == "T":
            min = int(input("Enter min value"))
            max = int(input("enter max value"))
            filtered_range = filter_range(test_subjects, min, max)
            for Number, Time in filtered_range:
                print(f"Number :{Number:>5}")
                print(f"Time   :{Time:>5}")
                print()


def print_menu():
    print("--------- Menu ----------")
    print("a) Add a new test subject")
    print("s) Show all information")
    print("r) Read from file")
    print("w) Write to file")
    print("T) Test subjects in range")
    print("q) Quit")
    print("-------------------------")

def filter_range(test_subjects, min, max):
    filter_range = []
    for number, time in test_subjects:
        if min <= time <= max:
            filter_range.append((number,time))
    return filter_range



def new_test_subject():
    print("---- New Test Subject ----")
    Number = input("Number :  ")
    Time = int(input("Time   :  "))
    return (Number, Time)

def print_test_subjects(test_subjects):
    print("---- Registered test subjects ----")
    for Number, Time in test_subjects:
        print(f"Number :{Number:>5}")
        print(f"Time   :{Time:>5}")
        print()


def read_data(filename):
    test_subjects = []
    with open(filename, 'r') as file:
        while True:
            Number = file.readline().strip()
            Time = file.readline().strip()
            if not Number or not Time:
                break
            else:
                Time = int(Time)
                test_subjects.append((Number,Time))
        print("*** Data read from file ***")
        return test_subjects

def write_data(test_subjects, filename):
    with open(filename, "w") as file:
        for Number, Time in test_subjects:
            file.write(f"{Number}" + '\n')
            file.write(f"{Time}"+ '\n')
        print("*** Data written to file ***")



if __name__ == '__main__':
    main()
