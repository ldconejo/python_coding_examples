def process_questions(filename="questions.csv"):
    """
    1. Open questions.csv.
    2. Return all questions.
    """
    pass


def display_answers(all_questions, filename="answers.csv"):
    """
    1. For each question:
        - Get the question ID.
        - Get the actual question.
        - Print the question.
        - Open the answers file.
        - Read all answers.
        - For each answer:
            - Get the answer ID.
            - Check if the answer ID matches the question ID:
                - If yes:
                    - Get the user name from the answer.
                    - Get the answer itself.
                    - Print the user name and their answer.
    """
    pass


if __name__ == "__main__":
    all_questions = process_questions()
    display_answers(all_questions)

    sample_list = [
        "element 1",
        2,
        2.4,
        "Another string",
    ]
