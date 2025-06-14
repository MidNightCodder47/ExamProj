class exercise:
    def __init__(self,question_text,question_answer): # Инициализация класса задание
        self.question_text = question_text
        self.question_answer = question_answer
    
    def correctness(self,user_answer): # проверка является ли ответ верным
        return str(user_answer).strip().lower() == str(self.question_answer).strip().lower()
    
class test:
    # инициализация теста
    def __init__(self,test_name,exr_num_max):
        self.test_name = test_name
        self.exr_num_max = exr_num_max

    exercises = [] # массив заданий

    # добавление заданий в тест
    def test_add_exr(self):
        for i in range(0,self.exr_num_max): # перебор ячеек теста

            # заполнение их шаблонами заданий
            exr = exercise(input("Enter your question \n"), 
                           input("Enter correct answer \n"))
            self.exercises.append(exr)


    # запуск теста
    def test_start(self):

        # перебор заданий теста по их заданному кол-ву
        for i in range(0,self.exr_num_max):
            # переменная текущего задания
            cur_quest = self.exercises[i]
            
            print(cur_quest.question_text) # вывод текста задания

            # ответ + проверка правильности
            print(cur_quest.correctness(input("Enter your answer \n"))) 

