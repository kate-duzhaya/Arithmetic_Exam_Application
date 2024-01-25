import random
import datetime


class Exam:
    difficulty_levels = {"1": "simple operations with numbers 2-9",
                         "2": "integral squares of 11-29"}

    def __init__(self):
        self.level = self.get_difficulty_level()
        self.tasks_num = 5
        self.answers = []
        self.mark = 0
        self.student_name = ""
        self.result_file = "results.txt"

    def get_difficulty_level(self):
        error_msg = "Incorrect format."
        while True:
            print("Which level do you want? Enter a number:")
            for level in self.difficulty_levels:
                print(f"{level} - {self.difficulty_levels[level]}")
            try:
                level = int(input())
                if level in [1, 2]:
                    break
                else:
                    raise ValueError
            except ValueError:
                print(error_msg)
        return level

    def generate_task(self):
        if self.level == 1:
            n1 = random.randint(2, 9)
            operation = random.choice("+-*")
            n2 = random.randint(2, 9)
            return f"{n1} {operation} {n2}"
        elif self.level == 2:
            return random.randint(11, 29)

    def get_user_answer(self) -> int:
        error_msg = "Wrong format! Try again."
        while True:
            try:
                answ = int(input())
                break
            except ValueError:
                print(error_msg)
        return answ

    def check_user_answer(self, expr, answ: int) -> str:
        correct_answ = int
        if self.level == 1:
            correct_answ = eval(expr)
        elif self.level == 2:
            correct_answ = expr ** 2
        return "Right!" if answ == correct_answ else "Wrong!"

    def get_mark(self) -> int:
        for answer in self.answers:
            if answer == "Right!":
                self.mark += 1
        return self.mark

    def save_results_to_file(self):
        save_to_file = input("Would you like to save your result to the file? Enter yes or no.\n")
        if save_to_file.lower() in ["y", "yes"]:
            self.student_name = input("What is your name?\n")
            with open(self.result_file, "a") as file:
                file.write(f"{datetime.datetime.now()} {self.student_name}: {self.mark}/5 in level {self.level} "
                           f"({self.difficulty_levels[str(self.level)]})\n")
            print(f"The results are saved to {self.result_file}.")
        else:
            exit()

    def execute_exam(self):
        for task_no in range(self.tasks_num):
            task = self.generate_task()
            print(task)
            user_answer = self.get_user_answer()
            result = self.check_user_answer(task, user_answer)
            self.answers.append(result)
            print(result)
        print(f"Your mark is {self.get_mark()}/5.")
        self.save_results_to_file()


if __name__ == "__main__":
    exam_Kate = Exam()
    exam_Kate.execute_exam()
