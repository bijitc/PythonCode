"""
Algoritm

Initialize 'score' to 0
print question
print Question 1 options A, B and C 
read the answer from the input (console)
Logic( if,else) to check answer and increase score by 1

print Question 2 for option A, B and C 
read the answer from the input (console)
Logic( if,else) to check answer and increase score by 1

print the total score
print 'Congratulations for participating!'
"""


score =0 

# Question 1
print('What is the capital of France?')
print('A. Paris')
print('B. Canberra')
print('C. Berlin')

answer = input('Your answer (A/B/C): ')

if answer=='A':
    print('You got it!')
    score = score + 1
else:
    print('Incorrect!')

# Question 2  
print('What is the largest mammal?')
print('A. Whale')
print('B. Monkey')
print('C. Cat')

answer = input(f'Your answer (A/B/C): ')

if answer=='A':
    print('You got it!')
    score = score + 1
else:
    print('Incorrect!')

print(f'Your score: {score}/2') 

print('Congratulations for participating!')
