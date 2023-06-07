import string

class Quiz:
    def __init__(self, questions:tuple):
        self.questions = questions
        self.true_answers = list()
        self.false_answers = list()
    def quiz(self):
        for i in enumerate(self.questions):
            print("Soru {})".format(i[0] + 1), end=' ')
            i[1].print_question()
            if i[1].answer():
                self.true_answers.append(i[0] + 1)
            else:
                self.false_answers.append(i[0] + 1)
            print()

    def print_results(self):
        print("Tüm cevapların:", len(self.questions))
        print("Doğru cevapların: ", end='')
        for trues in self.true_answers:
            print(f"{trues}, ", end='')
        print(f" (Toplam: {len(self.true_answers)})")
        print("Yanlış cevapların: ", end='')
        for falses in self.false_answers:
            print(f"{falses}, ", end='')
        print(f" (Toplam: {len(self.false_answers)})")
        print("Doğru cevapların / Tüm cevapların: ", len(self.true_answers) / len(self.questions))
        print("Yanlış cevapların / Tüm cevapların: ", len(self.false_answers) / len(self.questions))
        print("Testimizi çözdüğünüz için teşekkür ederiz...")

class Question:

    def __init__(self, text:str, choices:tuple, true_answer_index:int):
        self.text = text
        self.choices = enumerate(choices)
        self.trueAnswer = true_answer_index

    def answer(self):
        user_answer = ord(input('> ')) - ord('A')
        return user_answer == self.trueAnswer

    def print_question(self):
        print(self.text)
        for i in self.choices:
            print(f'{string.ascii_uppercase[i[0]]}) {i[1]}')

q1 = Question("Normal bir yılda kaç gün vardır?", ('366', '364', '365', '360', '367'), 2)
q2 = Question("3 düzine + 2 deste kaç yapar?", ('Hocam 4', 'Fatih medreseleri kursunda hocam', '2.5', '56', '55'), 3)
q3 = Question("2 + 2 = ?", ('5', '3', '1', '6', '4'), 4)

quiz = Quiz((q1, q2, q3))
quiz.quiz()
quiz.print_results()