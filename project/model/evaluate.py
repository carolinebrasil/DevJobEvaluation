from flask import flash

class Eval(object):

    def show_string(self,info): # Function to select the skill area for the developer candidate
        frontend = 0
        backend = 0
        mobile = 0

        if int(info['htmlskill']) >= 7 <= 10 and int(info['cssskill']) >= 7 <= 10 and int(info['javascriptskill']) >= 7 <= 10:
            frontend = 1
            flash('Você é dev Frontend')

        if int(info['pythonskill']) >= 7 <= 10 and int(info['djangoskill']) >= 7 <= 10:
            backend = 1
            flash('Você é dev Backend')

        if int(info['iosskill']) >= 7 <= 10 and int(info['androidskill']) >= 7 <= 10:
            mobile = 1
            flash('Você é dev Mobile')

        if frontend != 1 and backend != 1 and mobile != 1:
            flash('Você é dev generico')