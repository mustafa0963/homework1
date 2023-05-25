# A

import csv
L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 20, 53]
D1 = dict(zip(L1, L2))
print(D1)

# B


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


l = [x for x in range(2, 1000) if is_prime(x)]
print(l)

# C
L = ['Network', 'Math', 'Programming', 'Physics', 'Music']
L2 = []
for i in range(len(L)):
    if L[i].startswith('Ph'):
        L2.append(L[i])

print(L2)

# D
d = {i: i+1 for i in range(1, 11)}
print(d)

# Question 2
binary = input("Enter a binary number: ")
decimal = 0

for digit in binary:
    decimal = decimal*2 + int(digit)

print("The decimal equivalent of", binary, "is", decimal)

# ََQuestion 3


def read_questions(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        questions = list(reader)
    return questions


def ask_questions(questions):
    score = 0
    for question in questions:
        print(question[0])
        answer = input().strip().lower()
        if answer == question[1].strip().lower():
            score += 1
    return score


def save_result(name, score):
    with open('results.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, score])


filename = input("Enter the filename of the quiz questions: ")
questions = read_questions(filename)

name = input("Enter your name: ")
score = ask_questions(questions)

print("Your score is:", score)
save_result(name, score)
