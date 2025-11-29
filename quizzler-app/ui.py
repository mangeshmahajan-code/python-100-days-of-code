from tkinter import *
from quiz_brain import QuizBrain
 
 # UI setup using tkinter and give user feedback interms of flashing green or red on canvas 
THEME_COLOR = "#375362"

class QuizeInterface ():

    def __init__(self,quizbrain :QuizBrain):
        self.quiz = quizbrain
        self.window =Tk()
        self.window.title("Quizzle")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.canvas = Canvas(width= 300,height=250)
        self.score_text = Label(text=f"score : 0",bg=THEME_COLOR ,fg="white",padx=20,pady=10)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.score_text.grid(row= 0,column=1)
        
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=200,
            text="some question",
            fill=THEME_COLOR,
            font=("Arial",20,"italic")
            )
        right_image = PhotoImage(file="D:/my_python_learning/udemy_projects/day_34/quizzler-app-start/images/true.png")
        false_image= PhotoImage(file="D:/my_python_learning/udemy_projects/day_34/quizzler-app-start/images/false.png")

        self.right_button = Button(image=right_image,bg=THEME_COLOR,highlightthickness=0,command=self.check_answer_for_true)   
        self.false_button = Button(image=false_image,bg=THEME_COLOR,highlightthickness=0,command=self.check_answer_for_false) 
        self.right_button.grid(row=2 ,column=0)  
        self.false_button.grid(row=2 ,column=1)  
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):

        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score : {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text = q_text)
        
        else :
            self.canvas.itemconfig(self.question_text,text = f"You've reached the end of quize.\nYOU'R SCORE : {self.quiz.score}")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def check_answer_for_true(self):
        self.feedback(self.quiz.check_answer("True"))
        
    def check_answer_for_false(self):
        self.feedback(self.quiz.check_answer("False"))
        

    def feedback (self,is_right):
        self.count = 1
        if is_right:
        
            self.canvas.config(bg="green")
            
        else :
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
        