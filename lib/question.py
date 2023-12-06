class Question:
    def __init__(self, question_id, text, filename, answers=[], next_questions=[]):
        self.question_id = question_id
        self.text = text
        self.answers = answers
        self.next_questions = next_questions
        self.image = filename

    def is_branch_start(question_id: float) -> bool:
        return int(question_id) == question_id
