from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizBrain: QuizBrain):
        self.quiz = quizBrain

        # The GUI main window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # The Score label
        self.scoreLabel = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.scoreLabel.grid(row=0, column=1)

        # The Question canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.questionText = self.canvas.create_text(
            150, 125,  # Position of questionText
            text="Some Question Text",
            width=280,
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # The True button
        trueImage = PhotoImage(file="images/true.png")
        self.trueButton = Button(image=trueImage, highlightthickness=0, command=self.truePressed)
        self.trueButton.grid(row=2, column=0)

        # The False button
        falseImage = PhotoImage(file="images/false.png")
        self.falseButton = Button(image=falseImage, highlightthickness=0, command=self.falsePressed)
        self.falseButton.grid(row=2, column=1)

        # Present the question
        self.getNextQuestion()

        self.window.mainloop()

    def getNextQuestion(self):
        self.canvas.config(bg="white")  # Make the canvas white
        if self.quiz.still_has_questions():
            self.scoreLabel.config(text=f"Score: {self.quiz.score}")
            qText = self.quiz.next_question()  # Prepare the question text
            self.canvas.itemconfig(self.questionText, text=qText)  # Present the question text
        else:  # No more questions
            self.canvas.itemconfig(self.questionText, text="You've reached the end of the quiz.")
            self.trueButton.config(state="disabled")  # Turn off the True button
            self.falseButton.config(state="disabled")  # TUrn off the False button

    def truePressed(self):
        isRight = self.quiz.check_answer("True")
        self.giveFeedback(isRight)

    def falsePressed(self):
        isRight = self.quiz.check_answer("False")
        self.giveFeedback(isRight)

    def giveFeedback(self, isRight):
        # Shows a color upon user clicking a response button
        if isRight:
            self.canvas.config(bg="green")  # Make canvas green if user got question right
        else:
            self.canvas.config(bg="red")  # Make canvas red if user got question wrong
        self.window.after(1000, self.getNextQuestion)  # Wait 1 second before showing the next question
