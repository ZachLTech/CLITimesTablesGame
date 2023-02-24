import random
from TimesTables import MultiplesQsAndAs

def refresh():
    randomqanda = random.randrange(0,104,2)
    question = input(MultiplesQsAndAs[randomqanda])
    question = int(question)
    if(question == MultiplesQsAndAs[randomqanda +1]):
        print("Correct\n\n")
    elif(question == 0):
        print("Thanks for playing. Goodbye!")
    else:
        print(f"Incorrect\nThe Correct answer is: {MultiplesQsAndAs[randomqanda +1]}\n\n")
    return question
def Natural():
    randomqanda = random.randrange(0,234,2)
    question = input(MultiplesQsAndAs[randomqanda])
    question = int(question)
    if(question == MultiplesQsAndAs[randomqanda +1]):
        print("Correct\n\n")
    elif(question == 0):
        print("Thanks for playing. Goodbye!")
    else:
        print(f"Incorrect\nThe Correct answer is: {MultiplesQsAndAs[randomqanda +1]}\n\n")
    return question
def All():
    randomqanda = random.randrange(0,363,2)
    question = input(MultiplesQsAndAs[randomqanda])
    question = int(question)
    if(question == MultiplesQsAndAs[randomqanda +1]):
        print("Correct\n\n")
    elif(question == 0):
        print("Thanks for playing. Goodbye!")
    else:
        print(f"Incorrect\nThe Correct answer is: {MultiplesQsAndAs[randomqanda +1]}\n\n")
    return question