
#imports
import turtle as trtl
import random as rand
import playsound3 as ps
import tkinter as root_tk

# draw screen
wn = trtl.Screen()
Mlist =[]
wn.tracer(0)

# import all the characters and the background pictures
hero_image = "Barbiesaur.gif"
villain_image = "tripleT.gif"
bg_image = "kidsbg.gif"
win_image = "win.gif"

#turn all the images into shapes to call on
wn.addshape(win_image)
wn.addshape(hero_image)
wn.addshape(villain_image)
wn.addshape(bg_image)

# screen setup
wn.title("Fun Kids Entertainment (FKE)")
temp_root = root_tk.Tk()
screen_width = temp_root.winfo_screenwidth()
screen_height = temp_root.winfo_screenheight()
temp_root.destroy()
wn.setup(width=screen_width, height=screen_height)
wn.bgpic(bg_image)

# list of questions
question_list = ["What is your name?", "What is your favorite color?", "What is your favorite food?", "What is your favorite animal?", "What is your favorite thing to do?", "What is your favorite movie/show?", "What is your favorite book?", "What is your favorite sport?", "What is your favorite season?", "What is your favorite holiday?", "Do you like cake?", "What is your favorite icecream flavor?", "What is your favorite game?", "What is your dream vacation?", "What is your favorite fruit?", "Do you like veggies?"]

# list of complitments
compliment_list = ["You are awesome!", "You are amazing!", "You are fantastic!", "You are incredible!", "You are wonderful!", "You are the best!", "You are a superstar!", "You are a genius!", "You are a rockstar!", "You are a champion!", "You got this!", "Treat others well!", "Your so strong!"]

#list of colors
text_color = ["red", "blue", "green", "yellow", "orange", "purple", "pink",
    "cyan", "magenta", "lime", "gold", "silver", "coral", "tomato",
    "salmon", "plum", "violet", "indigo", "navy", "teal", "turquoise",
    "maroon", "olive", "aqua", "brown", "tan", "beige", "khaki",
    "lavender", "orchid", "crimson", "scarlet", "chocolate", "firebrick",
    "darkred", "darkblue", "darkgreen", "darkorange", "darkviolet",
    "deeppink", "deepskyblue", "dodgerblue", "hotpink", "lightblue",
    "lightgreen", "lightpink", "lightyellow", "lightcyan", "lightgray",
    "lightcoral", "lightsalmon", "lightseagreen", "lightskyblue",
    "lightslategray", "lightsteelblue", "mediumblue", "mediumorchid",
    "mediumseagreen", "mediumslateblue", "mediumturquoise",
    "midnightblue", "springgreen", "steelblue", "wheat"]

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
#the writer for the instructions
Ipainter = trtl.Turtle()
Ipainter.penup()
Ipainter.hideturtle()
Ipainter.goto(-350, 250)
Ipainter.write("Press (space) to Answer Questions!", font=("Arial", 30, "bold"))



# functions of the game
#asks the questions and counts until 3 questions have been asked and runs the win function
def ask_question():
    global question_count, Ipainter
    wn.onkeypress(None, "space")
    Ipainter.clear()
    #random questions from list
    while question_count < 3:
        question = rand.choice(question_list)
        answer = wn.textinput("Question", question)
        if answer is None:
            answer = "No answer given."
        Mlist.append((question, answer))
        Barbiedino.forward(230)
        wn.update()
        print(f"Q: {question} A: {answer}")
        question_list.remove(question)
        question_count += 1
    else:
        win()

        
#after 3 questions this is teh celebration screen
def win():
    global question, answer
    wn.clear()
    wn.bgpic(win_image)
    lpainter = trtl.Turtle()
    lpainter.penup()
    lpainter.hideturtle()
    lpainter.goto(65, 250)
    lpainter.color(rand.choice(text_color))
    lpainter.pendown()
    lpainter.write(rand.choice(compliment_list), font=("Arial", 50, "bold"))
    ps.playsound("winsound.mp3", block=False)
    show_answers()
    wn.update()
#display the answers the the questions they answered
def show_answers():
   answer_painter = trtl.Turtle()
   answer_painter.penup()
   answer_painter.hideturtle()
    
 #moves the position of the answers
   x_pos = -235
   y_pos = 100
    
   for item in Mlist:
        answer_painter.goto(x_pos, y_pos)
        answer_painter.color("black")
        answer_painter.write(item, font=("Arial", 17, "bold"))
        
        y_pos -= 50

#count the questions
question_count = 0        
wn.listen()  
     
# press space to ask a question
wn.onkeypress(ask_question, "space")
wn.update()
wn.mainloop()

