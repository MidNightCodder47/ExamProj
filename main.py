import classes

# создание 1 вопроса с вводом задания и нужного ответа
quest1 = classes.exercise(question_text=input("Enter ur question \n"), 
                          question_answer= input("Enter correct answer\n"))

print(quest1.question_text) # Показ вопроса
print(quest1.correctness(input("Ur answer \n"))) # проверка вводимого ответа заданному