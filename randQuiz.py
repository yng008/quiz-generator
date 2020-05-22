#! python3
# randQuiz.py - create quizzes with qn and ans in rand order along with ans key

import random
import sys
import csv


def main():

    # exits programme if qn bank not specified
    if len(sys.argv) != 2:
        print("Usage: python randQuiz.py [question bank].csv")
        sys.exit(1)

    # sets of test papers
    print("How many sets of tests do you need?")
    n = input()

    # validate n is an integer
    if validate(n) is False:
        print("Key in a positive whole number, teacher")
        sys.exit(1)

    # no of options per qn
    print("How many options should there be for each question?")
    options = input()

    # validate n is an integer
    if validate(options) is False:
        print("Key in a positive whole number, teacher")
        sys.exit(1)

    # convert numbers to int
    n = int(n)
    options = int(options) - 1  # since one option will def be right ans

    # open qn bank csv and store as dict
    qn = {}
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        keyword = next(reader)
        for row in reader:
            qn[row[0]] = row[1]

    # create name of quiz
    quiz = (sys.argv[1])[5:-4]

    # generate n sets of tests and answers
    for i in range(n):
        with open(f'{quiz}_quiz_{i:03d}.txt', 'w') as tests:
            with open(f'{quiz}_answer_{i:03d}.txt', 'w') as answers:
                # name, class and date
                tests.write('Name:\nClass:\nDate:\n\n')
                # name of quiz and set no.
                tests.write(f'{quiz.title()} {i:03d}\n\n')
                answers.write(f'Answer key for {quiz.title()} {i:03d}\n')

                # converts states to a list so that can use random (req ordered)
                states = list(qn.keys())

                # shuffle order of states
                random.shuffle(states)

                # loop through all qns and make a question for each
                for qnNum in range(len(qn)):
                    # generate right and wrong options
                    rightAns = qn[states[qnNum]]
                    wrongAns = list(qn.values())

                    # remove right ans from wrongAns list
                    del wrongAns[wrongAns.index(rightAns)]

                    # select options for questions
                    wrongAns = random.sample(wrongAns, options)
                    ansOptions = wrongAns + [rightAns]
                    random.shuffle(ansOptions)

                    # writes qn to tests
                    tests.write(f'{qnNum + 1}. What is the {keyword[1]} of {states[qnNum]}?')
                    tests.write('\n')

                    # writes options to tests
                    for j in range(options + 1):
                        tests.write(f'\t{j + 1}. {ansOptions[j]}\n')
                        tests.write('\n')   # spacing between qns

                    # writes ans to ans key
                    answers.write(f'{qnNum + 1}. {ansOptions.index(rightAns) + 1}')
                    answers.write('\n')


def validate(n):
    if n.isdigit() is True:
        if n != 0:
            return True
    return False


main()
