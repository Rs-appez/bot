from models.games.answer import Answer


class Question():

    def __init__(self, question, answers, level , cat) -> None:
        self.question = question
        self.answers = answers
        self.level = level
        self.cat = cat

    @staticmethod
    def get_questions(level = None, cat = None):

        return Question("pourquoi",Answer("42",["21","la reponse D","parceque"]),0,"test")
