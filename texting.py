import easygui
name = easygui.enterbox("Hello! What's your name?")
mood = easygui.buttonbox("Hello, " + name + ", how are you?",
                         choices = ['Great!', 'Fine, thanks.', 'Not bad.', 'Horrible!'])
if (mood == 'Great!'):
    easygui.msgbox("Well then keep doing what you're doing! Good luck!")
elif (mood == 'Fine, thanks.'):
    easygui.msgbox("I have nothing to do either so let's just sit and get bored.")
elif (mood == 'Not bad.'):
    plan = easygui.buttonbox("Do you have any plans for today?",
                      choices = ['Yes', 'No'])
    if (plan == 'Yes'):
        easygui.enterbox("What is it then?")
        easygui.msgbox("That's really interesing! I hope everything will go well.")
    else:
        easygui.msgbox("Then do something. You can go and read some books. Books are fun.")
else:
    easygui.msgbox("Well, I have nothing comforting to offer.")
    easygui.msgbox("Oh, wait. You can buy and/or read books. It can be really cheering up.")
