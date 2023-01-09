# a quiz of 10 queestions

#the questions and their answers to the quiz
q_and_a = {
    "question1": {
        "question": "What is the capital city of France?",
        "answer": "paris"
    },
    "question2": {
        "question": "In what country is the Chernobyl nuclear plant located?",
        "answer": "ukraine"
    },
    "question3": {
        "question": "How many bones do we have in an ear?",
        "answer": "3"
    },
    "question4": {
        "question": "Which planet has the most moons?",
        "answer": "saturn"
    },
    "question5": {
        "question": "What company was initially known as 'Blue Ribbon Sports'?",
        "answer": "nike"
    },
    "question6": {
        "question": "What game studio makes the Red Dead Redemption series?",
        "answer": "rockstar games"
    },
    "question7": {
        "question": "How many dots appear on a pair of dice?",
        "answer": "42"
    },
    "question8": {
        "question": "How many hearts does an octopus have?",
        "answer": "3"
    },
    "question9": {
        "question": "What is the only continent with land in all four hemispheres?",
        "answer": "africa"
    },
    "question10": {
        "question": "Where did sushi originate?",
        "answer": "china"
    }
}
# function for the quiz
def main():
    # set initial score
    score = 0
    # connote begining of quiz
    print('\n The quiz consists of 10 questions. Each correct answer is awarded 1 point.\n')
    # run a loop across all the questions and asnwers
    for key, value in q_and_a.items():
        print(f'{key}:')
        print(f'{value["question"]}')
        answer = input('Please enter your answer.\n')
        answer_lower = answer.lower()
        # if answer matches
        if (answer_lower == value['answer']):
            score += 1
            print(f'You have provided the correct answer and your current score is {score}\n')
        # if not match
        else:
            print(f'That is incorrect and the correct answer is {value["answer"]}\n')
    # Ouput the result at the end
    print(f'That is the end of the quiz. You scored {score} out of {len(q_and_a)} points.\n')
    
# run main
main()
        
        


