class Question:
    def __init__(self, question_id, text, answers=[], next_questions=[], answer_effects=[]):
        self.question_id = question_id
        self.text = text
        self.answers = answers
        self.next_questions = next_questions
        self.answer_effects = answer_effects  # This is a new list containing the effects of each answer

    def is_branch_start(question_id: str) -> bool:
        return "." not in question_id
