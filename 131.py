

import turtle as trtl
# draw screen
wn = trtl.Screen()
Mlist = []
wn.tracer(0)

# import shapes
hero_image = "Barbiesaur.gif"
villain_image = "tripleT.gif"
bg_image = "kidsbg.gif"

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


#importing barbiedino turtle
Barbiedino = trtl.Turtle()
Barbiedino.shape(hero_image)
Barbiedino.penup()
Barbiedino.goto(-500,-200)
Barbiedino.stamp()

#importing tripleT turtle
tripleT = trtl.Turtle()
tripleT.shape(villain_image)
tripleT.penup()
tripleT.goto(500,-100)
tripleT.stamp()
wn.update()











# press space for questions

































wn.mainloop()