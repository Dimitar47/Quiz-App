import sys
from User import User
from Question import Question
from Answer import Answer
from Game import Game


# Firstly, we are reading from file called Testfile.txt which contains the questions and answers for the game. Then,
# we are making instances of the Question class and instances of the User class, and we add the questions with their
# answers to a list of questions. We are asking then the users to enter their usernames and the quiz starts. All the
# actions are executed on the console and the users are asked to type their answer for each question. The users have
# to type what the correct answer according to them is, and they receive points if they answer correctly. If their
# answer isn't correct, however, they do not receive any points and the correct answer for the question is displayed.
# So, in short, the users accumulate points for answering correctly and receive no points for a wrong answer. After
# the users answer all the questions, the winner's final score together with their username is displayed and the game
# ends. The  winner's result are then sent and kept in a separate file called RankList.txt.

def main():
    numberOfPlayers = int(input('How many people are playing the game? '))
    questions = []
    question = None
    with open("Testfile.txt", "r") as infile:
        try:
            filtered = (line.replace('\n', '') for line in infile)
            for line in filtered:
                spl = get_non_empty_list(line, ' ')

                if int_try_parse(line[0]):
                    description = line[2:len(line) - 2]
                    question = Question(description)
                    if question not in questions:
                        questions.append(question)
                else:
                    length = len(line) - (len(spl[-1]) + 1)
                    description = line[0:length]
                    is_correct = spl[-1]
                    answer = Answer(description, eval(is_correct))
                    if answer not in question.answers:
                        question.answers.append(answer)
        except FileNotFoundError:
            print("File does not exist!")
    while numberOfPlayers > 0:
        username = input('Please enter your username: ')

        user1 = User()
        user1.name = username
        game = Game(user1.name)
        game.questions = questions
        print(len(game.questions))
        score = 0
        for question in game.questions:
            print(question.description)
            for answer in question.answers:
                print(answer.description)
            answer_user = input('Please enter your answer: ')
            for an in question.answers:
                if answer_user == an.description:
                    if an.is_correct:
                        score += 1
                        print("Correct!")
                        print(f"Your current score is {score}.")

                    else:
                        print("Wrong!")
                        #     new_list = [i.description for i in question.answers if i.is_correct]
                        lst = list(filter(lambda x: x.description if x.is_correct else None, question.answers))
                        print(f"The correct answer is {lst[0].description}!")
                        print(f"Your current score is {score}.")

        with open('RankList.txt', 'w') as output_file:
            output_file.write(f'Username: {user1.name}. Max score: {score}')
        numberOfPlayers -= 1
    with open('RankList.txt') as input_file:
        max_score = -sys.maxsize
        winners = User()
        for line in input_file:
            index = line.rfind(':')
            print(index)
            current_score_per_user = int(line[index + 2].strip())
            print(current_score_per_user)
            if current_score_per_user > max_score:
                max_score = current_score_per_user
                start_index_name = line.find(':')
                end_index_name = line.find('.')
                name = line[start_index_name + 2:end_index_name]
                winners.name = name
        print(numberOfPlayers)
    if numberOfPlayers == 0:
        print(f'The winner is {winners.name} with a final score of {max_score}.')


def get_non_empty_list(s, delimiter):
    return list(filter(str.strip, s.split(delimiter)))


def int_try_parse(value):
    try:
        return int(value), True
    except ValueError:
        return False


if __name__ == '__main__':
    main()
