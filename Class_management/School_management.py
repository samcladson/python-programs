school = {
        "Class_A" :{
                        "Sam":{

                            "Eng":80,
                            "Tam":85,
                            "Maths":90
                        },
                        "Jeevan":{

                            "Eng":90,
                            "Tam":85,
                            "Maths":89
                        },
                        "Raghul":{

                            "Eng":90,
                            "Tam":100,
                            "Maths":95
                        }
                    },
        "Class_B" :{
                        "Rupesh":{

                            "Eng":70,
                            "Tam":85,
                            "Maths":95
                        },
                        "Suhail":{

                            "Eng":95,
                            "Tam":85,
                            "Maths":99
                        },
                        "Siju":{

                            "Eng":70,
                            "Tam":100,
                            "Maths":95
                        }
                    }
}
option = 0
while(option != 4):
    print("What do you need to do? \n"
            "1) Display the students list \n"
            "2) Display the school topper \n" 
            "3) Display The class toppers \n" 
            "4) Exit")

    option = int(input())
    if option == 1:
        for k,v in school.items():
            sno = 1
            print(k)
            for key,value in v.items():
                print("{} : {}".format(sno,key))
                sno += 1
            print()