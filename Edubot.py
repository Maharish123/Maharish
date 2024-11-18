import random

# Simulating student data (score and learning progress)
class Student:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.level = 1  # Student's current difficulty level (1 - Easy, 2 - Medium, 3 - Hard)

    def update_score(self, points):
        self.score += points

    def promote_level(self):
        if self.level < 3:
            self.level += 1
        print(f"{self.name} is now at difficulty level {self.level}")

    def demote_level(self):
        if self.level > 1:
            self.level -= 1
        print(f"{self.name} is now at difficulty level {self.level}")


# AI-powered tutor that adapts based on performance
class AITutor:
    def __init__(self):
        self.questions = {
            1: [("What is 2 + 2?", 4), ("What is 3 + 1?", 4)],
            2: [("What is 12 + 8?", 20), ("What is 15 + 7?", 22)],
            3: [("What is 45 + 33?", 78), ("What is 78 + 56?", 134)]
        }

    def get_question(self, level):
        question = random.choice(self.questions[level])
        return question

    def ask_question(self, student):
        question = self.get_question(student.level)
        print(f"Question: {question[0]}")
        answer = int(input("Your answer: "))
       
        # Check if the answer is correct
        if answer == question[1]:
            student.update_score(10)
            print("Correct! Well done.")
        else:
            student.update_score(-5)
            print("Incorrect! Keep trying.")

        self.provide_feedback(student)

    def provide_feedback(self, student):
        if student.score > 30:
            student.promote_level()
        elif student.score < -10:
            student.demote_level()

    def run_tutor_session(self, student):
        print(f"\nWelcome to your personalized learning session, {student.name}!\n")
        for _ in range(5):  # Run 5 rounds of questions
            self.ask_question(student)
        print(f"\n{student.name}'s Final Score: {student.score}")
        print(f"Final Difficulty Level: {student.level}")


# Main function to simulate the learning session
def main():
    student_name = input("Enter your name: ")
    student = Student(student_name)
    tutor = AITutor()
   
    tutor.run_tutor_session(student)

if __name__ == "__main__":
    main()

