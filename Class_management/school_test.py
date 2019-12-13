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

print(school)

for k,v in school.items():
	for k,v in v.items():
		print(k,v)

# Output :  

# Sam {'Eng': 100, 'Tam': 95, 'Maths': 90}
# Jeevan {'Eng': 90, 'Tam': 85, 'Maths': 89}
# Raghul {'Eng': 90, 'Tam': 100, 'Maths': 95}

# Rupesh {'Eng': 70, 'Tam': 85, 'Maths': 95}
# Suhail {'Eng': 95, 'Tam': 85, 'Maths': 99}
# Siju {'Eng': 70, 'Tam': 100, 'Maths': 95}

# Rajesh {'Eng': 71, 'Tam': 83, 'Maths': 55}
# Ram {'Eng': 90, 'Tam': 85, 'Maths': 79}
# Geetha {'Eng': 100, 'Tam': 100, 'Maths': 95}



for k,v in school.items():
	for k,v in v.items():
        for k,v in v.items():
			 print(k,v)

# Output :
""" fitst iteration"""
# Eng 100
# Tam 95
# Maths 90
""" second iteration"""
# Eng 90
# Tam 85
# Maths 89

"""  Goes on for the length of the dict """


# Accessing a specific value 

# Raghul {'Eng': 90, 'Tam': 100, 'Maths': 95}
