questions = [
    {
        'q_id':'Q1',
        'q_description':'Author of Python',
        'q_options':['Gudio van Rossum','Steve Jobs','James Gosling','Patric Naughton'],
        'q_answer':'Gudio van Rossum'
    },
    {
        'q_id':'Q2',
        'q_description':'Which function is used to display the user content',
        'q_options':['print()','input()','format()','eval()'],  
        'q_answer':'print()',
    },
    {
        'q_id':'Q3',
        'q_description':'Which function is used to get data from user',
        'q_options':['print()','input()','format()','eval()'],  
        'q_answer':'input()',
    }
]
score = 0
choice = 0
print("***********Welcome to Python Quiz*************")
while( choice!=2):
    choice = int(input("Enter 1 to start the quiz \n"))
    if choice == 1:
        for i in range(len(questions)):
            print("Your question {} \n\n Description {} \n\n options {} \n\n"
            .format(questions[i]['q_id'],questions[i]['q_description'],questions[i]['q_options']))
            answer = input()
            if answer == questions[i]['q_answer']:
                score += 1
            elif answer != questions[i]['q_answer'] and score > 0:
                score -= 1
        if i == 3:
            print(score)
