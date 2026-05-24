import customtkinter as ctk
from random import randint, choice
from CTkMessagebox import CTkMessagebox
import lexicon as lex


class GreetingsPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=lex.FRM_COLOR)
        self.controller = controller

        label_data = [
            ('Привет! Это угадайка чисел', lex.TXT_COLOR_1),
            ('Хочешь сыграть?', lex.TXT_COLOR_2)
        ]

        for idx, (text, color) in enumerate (label_data):
            label = ctk.CTkLabel (
                self,
                text = text,
                text_color = color,
                font = ('Constantia', 27)
            )
            label.place(relx = 0.5, rely = 0.35 + (idx * 0.2), anchor = 'c')

        button_data = [
            ('Не хочу', self.controller.end_game),
            ('Давай!', lambda: self.controller.switch_to('RulesPage'))
        ]

        for idx, (text, command) in enumerate (button_data):
            button = ctk.CTkButton (
                self,
                text = text,
                command = command,
                **lex.BTN_PARAMS
            )
            button.place(relx = 0.35 + (idx * 0.3), rely = 0.8, anchor = 'c')

class RulesPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = lex.FRM_COLOR)
        self.controller = controller

        label_data = [
            ('Правила очень простые:', lex.TXT_COLOR_1),
            ('Я загадываю число от 1 до 100', lex.TXT_COLOR_2),
            ('А ты пытаешься его отгадать,', lex.TXT_COLOR_1),
            ('вводя свои варианты чисел', lex.TXT_COLOR_2),
            ('У тебя несколько попыток', lex.TXT_COLOR_1),
            ('Начнём?', lex.TXT_COLOR_2)
        ]

        for idx, (text, color) in enumerate (label_data):
            label = ctk.CTkLabel (
                self,
                text = text,
                text_color = color,
                font = ('Constantia', 27)
            )
            label.place(relx = 0.5, rely = 0.1 + (idx * 0.13), anchor = 'c')

        button_data = [
            ('Не сейчас', self.controller.end_game),
            ('Поехали', self.controller.create_game)
        ]

        for idx, (text, command) in enumerate (button_data):
            button = ctk.CTkButton (
                self,
                text = text,
                command = command,
                **lex.BTN_PARAMS
            )
            button.place(relx = 0.35 + (idx * 0.3), rely = 0.9, anchor = 'c')

class FarewellPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = lex.FRM_COLOR)
        self.controller = controller

        label = ctk.CTkLabel(
            self,
            text = choice(lex.FAREWELL_WORDS),
            text_color = lex.TXT_COLOR_1,
            font = ('Constantia', 27)
        )
        label.place(relx = 0.5, rely = 0.5, anchor = 'c')

class LoadingPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = lex.FRM_COLOR)
        self.controller = controller

        self.label = ctk.CTkLabel(
            self,
            text = '',
            text_color = lex.TXT_COLOR_1,
            font = ('Constantia', 27)
        )
        self.label.place(relx = 0.5, rely = 0.5, anchor = 'c')

    def update_loading_words(self):
        self.label.configure(text = choice(lex.LOADING_WORDS))

class GamePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = lex.FRM_COLOR)
        self.controller = controller

        self.labels = {}

        label_data = [
            (None, 'Введи любое число', lex.TXT_COLOR_1, 0.1),
            (None, 'от 1 до 100', lex.TXT_COLOR_2, 0.25),
            ('step_label', '', lex.TXT_COLOR_1, 0.55),
            ('comment_label', '', lex.TXT_COLOR_2, 0.7),
            ('used_label', '', lex.TXT_COLOR_1, 0.85)
        ]

        for idx, (name, text, color, rely) in enumerate (label_data):
            label = ctk.CTkLabel(
                self,
                text = text,
                text_color = color,
                font = ('Constantia', 30)
            )
            label.place(relx = 0.5, rely = rely, anchor = 'c')
            if name: self.labels[name] = label

        self.entry = ctk.CTkEntry(
            self,
            width = 100,
            height = 30,
            corner_radius = 40,
            justify = 'c',
            text_color = '#66ff33',
            font = ('Cambria', 27)
        )
        self.entry.place(relx = 0.5, rely = 0.4, anchor = 'c')

        button_data = [('←', self.clear_input), ('→', self.send_input)]

        for idx, (text, command) in enumerate (button_data):
            button = ctk.CTkButton(
                self,
                text = text,
                command = command,
                height = 30,
                width = 120,
                corner_radius = 15,
                fg_color = lex.BTN_COLOR_1,
                hover_color = lex.BTN_COLOR_2,
                text_color = lex.BTN_COLOR_3,
                font = ('Constantia', 20)
            )
            button.place(relx = 0.25 + (idx * 0.5), rely = 0.4, anchor = 'c')

    def send_input(self):
        self.controller.transfer_data(self.entry.get())

    def get_status(self, status, info):
        if status in lex.ERROR_MESSAGES:
            error_message = CTkMessagebox (
                app,
                **lex.MSG_PARAMS,
                message = lex.ERROR_MESSAGES[status]
            )
            app.wait_window(error_message)
            self.clear_entry()
            return

        if status == 'win' or status == 'lose':
            self.controller.transfer_final_data(status, info)
            self.controller.switch_to('FinalPage')
            return

        self.labels['comment_label'].configure(text=choice(lex.GAME_WORDS[status]))
        self.labels['step_label'].configure(text=f'Осталось попыток: {info["step"]}')
        self.labels['used_label'].configure(text=info['used'])
        self.clear_entry()

    def update_ui(self, step):
        self.clear_entry()
        self.labels['step_label'].configure(text=f'Осталось попыток: {step}')
        self.labels['comment_label'].configure(text='')
        self.labels['used_label'].configure(text='')

    def clear_entry(self):
        self.entry.delete (0, 'end')
        self.entry.focus_set()

    def clear_input(self):
        self.entry.delete (len(self.entry.get()) - 1)

class FinalPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = lex.FRM_COLOR)
        self.controller = controller

        self.labels = {}

        label_data = [
            ('comment_label', "", lex.TXT_COLOR_1),
            ('text_label', "Искомое число:", lex.TXT_COLOR_2),
            ('num_label', "", lex.TXT_COLOR_1),
            ('used_label', "", lex.TXT_COLOR_2),
            ('count_label', "", lex.TXT_COLOR_1),
            ('again_label', "Хотите повторить?", lex.TXT_COLOR_2)
        ]

        for idx, (name, text, color) in enumerate(label_data):
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color = color,
                font= ('Constantia', 27)
            )
            label.place(relx = 0.5, rely = 0.1 + (idx * 0.14), anchor = 'c')
            self.labels[name] = label

        button_data = [
            ('Не хочу', self.controller.end_game),
            ('Давай!', self.controller.create_game)
        ]

        for idx, (text, command) in enumerate (button_data):
            button = ctk.CTkButton (
                self,
                text = text,
                command = command,
                **lex.BTN_PARAMS
            )
            button.place(relx = 0.35 + (idx * 0.3), rely = 0.9, anchor = 'c')

    def get_result(self, status, info):
        labels = self.labels
        comment_text = choice(lex.FINAL_WORDS[status])
        used_text = f'Использованные числа:\n{info["used"]}'
        count_text = f'Потрачено попыток: {info["spent_steps"]}'

        labels['comment_label'].configure(text=comment_text)
        labels['num_label'].configure(text=info['num'])
        labels['used_label'].configure(text = used_text)
        labels['count_label'].configure(text = count_text)

class MainLogic():
    def __init__(self):
        self.max_steps = 8
        self.update_variables()

    def check_input(self, user_input):
        if not user_input:
            return 'empty'
        if len(user_input) > 3:
            return 'too many'
        if not user_input.isdigit():
            return 'not a digit'

        val = int(user_input)

        if val < 1 or val > 100:
            return 'out of range'
        if val in self.used_digits:
            return 'it was'

        return None

    def analyze_the_number(self, user_input):
        error_status = self.check_input(user_input)
        if error_status:
            return error_status, {}

        user_num = int(user_input)
        self.used_digits.append(user_num)
        self.step -= 1

        info = {
            'step': self.step,
            'used': ", ".join(map(str, self.used_digits)),
            'num': self.num,
            'spent_steps': self.max_steps - self.step
        }

        if user_num == self.num:
            return 'win', info
        if self.step == 0:
            return 'lose', info
        if user_num > self.num:
            status = 'too near high' if (user_num - self.num) <= 5 else 'too high'
        else:
            status = 'too near low' if (self.num - user_num) <= 5 else 'too low'

        return status, info

    def update_variables(self):
        self.step = self.max_steps
        self.num = randint(1, 100)
        self.used_digits = []

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Угадай число')
        self.geometry ('600x500+800+450')
        self.resizable (False, False)
        self.attributes ('-alpha', 0.8)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill = 'both', expand = True)

        self.main_logic = MainLogic()

        self.pages = {}
        self.current_frame = None
        for F in (
            GreetingsPage, RulesPage, GamePage,
            FinalPage, FarewellPage, LoadingPage
        ):
            page_name = F.__name__
            self.pages[page_name] = F(master = self.main_frame, controller=self)
        self.switch_to("GreetingsPage")

    def switch_to(self, page_name):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.pages[page_name]
        self.current_frame.pack(fill="both", expand=True)

    def transfer_data(self, user_input):
        status, info = self.main_logic.analyze_the_number(user_input)
        self.pages['GamePage'].get_status(status, info)

    def transfer_final_data(self, status, info):
        self.pages['FinalPage'].get_result(status, info)

    def create_game(self):
        self.pages['LoadingPage'].update_loading_words()
        self.switch_to('LoadingPage')
        self.main_logic.update_variables()
        self.pages['GamePage'].update_ui(self.main_logic.step)
        self.after(3000, lambda: (self.switch_to('GamePage')))

    def end_game(self):
        self.switch_to('FarewellPage')
        self.after(3000, self.destroy)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

    #testing