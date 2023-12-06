#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton,QMessageBox, QGroupBox
from random import shuffle

app = QApplication([])

main = QWidget()
main.resize(400,200)
main.setWindowTitle('- Memory card -')

box_v = QVBoxLayout()

label = QLabel("Какой национальности не существует")
button = QPushButton("Ответить")
button2 = QPushButton("Следующий вопрос")

# Варианты ответа
radio_group = QGroupBox("Варианты ответа")

rb_group = QButtonGroup()
rb_1 = QRadioButton('Энцы')
rb_2 = QRadioButton('Смурфы')
rb_3 = QRadioButton('Чулымцы')
rb_4 = QRadioButton('Алеуты')
rb_group.addButton(rb_1)
rb_group.addButton(rb_2)
rb_group.addButton(rb_3)
rb_group.addButton(rb_4)


layout_h = QHBoxLayout()   
layout_v1 = QVBoxLayout() 
layout_v2 = QVBoxLayout()

layout_v1.addWidget(rb_1)
layout_v1.addWidget(rb_2)

layout_v2.addWidget(rb_3)
layout_v2.addWidget(rb_4)

layout_h.addLayout(layout_v1)
layout_h.addLayout(layout_v2)

radio_group.setLayout(layout_h)

#результаты ответа
answer_group = QGroupBox("Результат теста")
ag_layout = QVBoxLayout()
ag_results_ok = QLabel("Ответ верный")
ag_results_answer = QLabel("Тут будет правильный ответ")

ag_layout.addWidget(ag_results_ok)
ag_layout.addWidget(ag_results_answer, alignment=Qt.AlignHCenter)
answer_group.setLayout(ag_layout)
answer_group.hide()

box_v.addWidget(label, alignment=Qt.AlignHCenter)
box_v.addWidget(radio_group)
box_v.addWidget(answer_group)
box_v.addWidget(button, stretch=2)
box_v.addWidget(button2, stretch=2)
button2.hide()

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
            self.question = question
            self.right_answer = right_answer
            self.wrong1 = wrong1
            self.wrong2 = wrong2
            self.wrong3 = wrong3
            
answers = [rb_1, rb_2, rb_3, rb_4]

# Функция которая устанавливает новый вопрос и варианты ответа
# questuons_and_answers - переменная класса Question
def ask(questuons_and_answers):
    #Усианавливаем новый вопрос
    label.setText(questuons_and_answers.question)
    # Устанавливаем правильный ответ
    ag_results_answer.setText(questuons_and_answers.right_answer)
    # Меняем порядок следования кнопок
    shuffle(answers)
    # Устнавливаем значения кнопока, ответы
    answers[0].setText(questuons_and_answers.right_answer)
    answers[1].setText(questuons_and_answers.wrong1)
    answers[2].setText(questuons_and_answers.wrong2)
    answers[3].setText(questuons_and_answers.wrong3)
    # Сьрасываем все выбранные радиокнопки
    rb_group.setExclusive(False)
    for rb in answers:
        rb.setChecked(False)
    rb_group.setExclusive(True)

def show_result():
    radio_group.hide()
    answer_group.show()
    
  #  ag_results_ok.setText("Верно" if answers[0].isChecked() else "Не верно")
    
    if answers[0].isChecked():
        ag_results_ok.setText("Верно")
    else:
        ag_results_ok.setText("Не верно")
        
    button.hide()
    button2.show()


def show_question():
    answer_group.hide()
    button2.hide()
    
    ask("Государственный язык бразилии", "Португальский", "Итальянский", "Бразильский", "Испанский")
    
    radio_group.show()
    button.show()



button.clicked.connect(show_result)
button2.clicked.connect(show_question)

ask("Какой национальноасти не существует", "Смурфы", "Энци", "Чулымцы", "Алеуты")
   

main.setLayout(box_v)
main.show()

app.exec()
