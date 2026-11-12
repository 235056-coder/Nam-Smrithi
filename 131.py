
#imports
import turtle as trtl
import random as rand

# draw screen
wn = trtl.Screen()
Mlist =[]
wn.tracer(0)

# import shapes
hero_image = "Barbiesaur.gif"
villain_image = "tripleT.gif"
bg_image = "kidsbg.gif"
win_image = "win.gif"


wn.addshape(win_image)
wn.addshape(hero_image)
wn.addshape(villain_image)
wn.addshape(bg_image)

# screen setup
wn.title("Fun Kids Entertainment (FKE)")

screen_width = 2500
screen_height = 2000
wn.setup(width=screen_width, height=screen_height)
wn.bgpic(bg_image)

# list of questions
question_list = ["What is your name?", "What is your favorite color?", "What is your favorite food?", "What is your favorite animal?", "What is your favorite thing to do?", "What is your favorite movie/show?", "What is your favorite book?", "What is your favorite sport?", "What is your favorite season?", "What is your favorite holiday?", "Do you like cake?", "What is your favorite icecream flavor?", "What is your favorite game?", "What is your dream vacation?", "What is your favorite fruit?", "Do you like veggies?"]

# list of complitments
compliment_list = ["You are awesome!", "You are amazing!", "You are fantastic!", "You are incredible!", "You are wonderful!", "You are the best!", "You are a superstar!", "You are a genius!", "You are a rockstar!", "You are a champion!", "You got this!", "Treat others well!", "Your so strong!"]


#importing barbiedino turtle
Barbiedino = trtl.Turtle()
Barbiedino.shape(hero_image)
Barbiedino.penup()
Barbiedino.goto(-500,-200)

#importing tripleT turtle
tripleT = trtl.Turtle()
tripleT.shape(villain_image)
tripleT.penup()
tripleT.goto(500,-100)
wn.update()


# functions



def ask_question():
    global question_count
    wn.onkeypress(None, "space")
    
    while question_count < 3:
        question = rand.choice(question_list)
        answer = wn.textinput("Question", question)
        if answer is None:
            answer = "No answer given."
        Barbiedino.forward(230)
        wn.update()
        print(f"Q: {question} A: {answer}")
        question_count += 1
    else:
        win()
        


def win():
    global question, answer
    wn.clear()
    wn.bgpic(win_image)
    lpainter = trtl.Turtle()
    lpainter.penup()
    lpainter.hideturtle()
    lpainter.goto(85, 250)
    lpainter.color("blue")
    lpainter.pendown()
    lpainter.write(rand.choice(compliment_list), font=("Arial", 50, "bold"))
    wn.update()

#count the questions
question_count = 0        
wn.listen()       
# press space to ask a question
wn.onkeypress(ask_question, "space")
    

wn.update()

wn.mainloop()

