class exercise:
    def __init__(self,question_text,question_answer): # Инициализация класса задание
        self.question_text = question_text
        self.question_answer = question_answer
    
    def correctness(self,user_answer): # проверка является ли ответ верным
        return str(user_answer).strip().lower() == str(self.question_answer).strip().lower()
    

    