school = {
    "Class_A": {
        "Sam": {"Eng": 100, "Tam": 95, "Maths": 90},
        "Jeevan": {"Eng": 90, "Tam": 85, "Maths": 89},
        "Raghul": {"Eng": 90, "Tam": 100, "Maths": 95}
    },
    "Class_B": {
        "Rupesh": {"Eng": 70, "Tam": 85, "Maths": 95},
        "Suhail": {"Eng": 95, "Tam": 85, "Maths": 99},
        "Siju": {"Eng": 70, "Tam": 100, "Maths": 95}
    },
    "Class_c": {
        "Rajesh": {"Eng": 71, "Tam": 83, "Maths": 55},
        "Ram": {"Eng": 90, "Tam": 85, "Maths": 79},
        "Geetha": {"Eng": 100, "Tam": 100, "Maths": 95}
    }
}
option = 0
while(option != 4):
    print("\nWhat do you need to do? \n"
          "1) Display the students list \n"
          "2) Display the school topper \n"
          "3) Display The class toppers \n"
          "4) Exit")

    option = int(input("Enter your option : "))

    # Display/ view students list and display student mark and his/her average

    if option == 1:
        for k, v in school.items():
            sno = 1
            print(k)
            for key, value in v.items():
                print("{} : {}".format(sno, key))
                sno += 1
            print()
        std_loop = "yes"
        while(std_loop != "no"):
            std_loop = input("Continue to see students detail : yes/no \n")
            if std_loop == "yes":
                # display mark and average of students
                view_mark_option = input(
                    "Do you need to see the marks of the student? yes/no \n")
                if view_mark_option == "Yes" or view_mark_option == "yes":
                    std_name = input("Enter student name :")

# dictionary comprehension to get students name and their details (as dict)

                    d = {
                        name_k: name_v
                        for class_k, class_v in school.items()
                        for name_k, name_v in class_v.items()
                        for sub_k, sub_v in name_v.items()
                    }
# dictionary comprehension ends

                    info = d[std_name]
                    mark_sum_list = []
                    print("\n{:<10} ===> {:>8}".format("Subject", "Marks"))

                    for k, v in info.items():
                        print("{:<10} ===> {:>5}".format(k, v))
                        mark_sum_list.append(v)

                    avg = (sum(mark_sum_list)//len(mark_sum_list))

                    print("\nTotal of {} is {} \n".format(std_name, sum(mark_sum_list)))
                    mark_sum_list = []
                    print("Average of {} is {} \n".format(std_name, avg))
                else:
                    print("Back to main menu :) \n")
                    break
            else:
                print("Back to main menu :) \n")
                std_loop = "no"

    if option == 2:

        toppers_list = {nk: sum(nv.values()) for ck, cv in school.items() for nk, nv in cv.items()}
        topers = {k: v for k, v in sorted(toppers_list.items(), key=lambda x: x[1], reverse=True)}
        print("{:<10}{:>12} \n".format("Name","Total"))
        for k,v in topers.items():
            print("{:<10} ==> {:>5} ".format(k,v))
        print("\nSchool topper is : {} \n".format(max(topers.items(), key=lambda x: x[1])))

    if option == 3:

        toppers_list_in_class = {ck:{nk:sum(nv.values()) for nk, nv in cv.items()} for ck, cv in school.items()}
        class_toper = {k:max(v.items(),key = lambda x:x[1]) for k,v in toppers_list_in_class.items()}
        for key,value in toppers_list_in_class.items():
            print("\n{}\n".format(key))
            for k,v in sorted(value.items(),reverse = True):
                print("{:<10}==>{:>10}".format(k,v))
            print("\n{} topper is {}".format(key,class_toper[key]))
