questions = [
    ["Q1:- The language of Lakshadweep, a Union Territory of India, is - ",
     "Tamil", "Hindi", "Malayalam", "Telugu", 3],
    ["Q2:- The International Literacy Day is observed on - ",
     "Sep 8", "Nov 28", "May 2", "Sep 22", 1],
    ["Q3:- Bahubali festival is related to - ",
     "Islam", "Hinduism", "Buddhism", "Jainism", 4],
    ["Q4:- Which day is observed as the World Standards Day?",
     "June 26", "Oct 14", "Nov 15", "Dec 2", 2],
    ["Q5:- September 27 is celebrated every year as - ",
     "Teachers' Day", "National Integration Day", "World Tourism Day", "International Literacy Day", 3],
    ["Q6:- Which city is home to the Brandenburg Gate?",
     "Vienna", "Zurich", "Berlin", "Rome", 3],
    ["Q7:- Which flies a green, white, and orange (in that order) tricolor flag?",
     "Ireland", "Ivory Coast", "Italy", "India", 4],
    ["Q8:- Which city is home to the Brandenburg Gate? ",
     "Vienna","Zurich","Berlin","London",3],
    ["Q9:- Who is generally considered the inventor of the motor car? ",
     "Henry Ford","Karl Benz","Henry M. Leland","None of these",2],
    ["Q10:- Where was the first example of paper money used",
     "China","Turkey","Greece","None of these",1],
    ["Q11:- What number was the Apollo mission that successfully put a man on the moon for the first time in human history? ",
     "Apollo 11","Apollo 12","Apollo 13","Apollo 14",1],
    ["Q12:- Which of the following languages has the longest alphabet?",
     "Greek","Russia","Arabic","India",2],
    ["Q13:- What was the name of the Franco-British supersonic commercial plane that operated from 1976-2003?",
     "Accord","Concorde","Mirage","None of these",2],
    ["Q14:- What is the largest US state (by landmass)?",
     "Texas","Alaska","California","None of these",2],
    ["Q15:- Which Game of Thrones character is known as the Young Wolf? ",
     "Robb Stark","Robb Stark","Sansa Stark","None of these",1],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"\n\nQuestions for Rs. {levels[i]}")
    print(f"{question[0]}")
    print(f"a. {question[1]}            b. {question[2]}")
    print(f"c. {question[3]}            d. {question[4]}")
    
    reply = input("Enter your answer (a/b/c/d), or type 'quit' to exit: ")
    
    if reply.lower() == 'quit':
        break
    
    options = ['a', 'b', 'c', 'd']
    if reply in options:
        if reply == options[question[-1] - 1]:
            print(f"Correct answer! You have won Rs. {levels[i]}")
            money = levels[i]
            if i == 5:
                print("You can quit with Rs. 10,000")
            elif i == 10:
                print("You can quit with Rs. 320,000")
            elif i == 14:
                print("You can quit with Rs. 10,000,000")
        else:
            print("Wrong answer. Game over.")
            break
    else:
        print("Invalid input. Please enter 'a', 'b', 'c', 'd', or 'quit'.")

print(f"You won money Rs. {money}")
