import random



class QuizGame:

    def __init__(self):

        self.score = 0

        self.topics = {"Python": ["What is the capital of Python?", {"options": ["Monty", "IDLE", "PyCharm", "None"], "correct": 1}],

                       "Programming": ["What does 'IDE' stand for?", {"options": ["Integrated Development Environment", "Interactive Development Environment", "Intelligent Development Environment", "Integrated Design Environment"], "correct": 1}],

                       "Mathematics": ["What is the square root of 64?", {"options": ["6", "7", "8", "9"], "correct": 3}

                                       ]}



    def display_question(self, topic, question_data):

        print(f"\n{topic} Quiz:")

        print(question_data[0])

        for i, option in enumerate(question_data[1]["options"], start=1):

            print(f"{i}. {option}")



    def get_user_answer(self, num_options):

        while True:

            try:

                choice = int(input(f"Choose an option (1-{num_options}): "))

                if 1 <= choice <= num_options:

                    return choice

                else:

                    print("Invalid choice. Please enter a number within the specified range.")

            except ValueError:

                print("Invalid input. Please enter a number.")



    def run_quiz(self):

        print("Welcome to the Quiz Game!")

        topic = input("Choose a topic (Python, Programming, Mathematics): ").capitalize()



        if topic not in self.topics:

            print("Invalid topic. Exiting the game.")

            return



        difficulty = input("Choose a difficulty level (Easy, Medium, Hard): ").capitalize()

        questions = self.topics[topic]

        question_data = questions[1]



        if difficulty == "Medium":

            random.shuffle(question_data["options"])



        self.display_question(topic, questions)

        user_choice = self.get_user_answer(len(question_data["options"]))



        if user_choice == question_data["correct"]:

            print("Correct! Well done.")

            self.score += 1

        else:

            print(f"Oops! That's incorrect. The correct answer was {question_data['options'][question_data['correct'] - 1]}.")



        print(f"\nQuiz completed! Your final score: {self.score}/{len(self.topics)}")



if __name__ == "__main__":

    quiz_game = QuizGame()

    quiz_game.run_quiz()
