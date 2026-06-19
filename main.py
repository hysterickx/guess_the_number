import customtkinter as ctk
from random import randint, choice
from CTkMessagebox import CTkMessagebox
import config as cfg


class StaticPages(ctk.CTkFrame):
    def __init__(self, master, controller, page_name):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

        page_config = cfg.STATIC_PAGES_DATA[page_name]
        label_data = page_config['labels']
        button_data = page_config['buttons']

        for text, color, font, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=font
            )
            label.place(relx=0.5, rely=rely, anchor='c')

        command_data = {
            'exit': controller.exit_app,
            'next': lambda: controller.switch_to('RulesPage'),
            'start': controller.create_app
        }

        for text, command_key, relx in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=command_data[command_key],
                **cfg.BTN_PARAMS
            )
            button.place(relx=relx, rely=0.9, anchor='c')


class GamePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.COLOR_DARK)
        self.controller = controller

        self.labels = {}

        label_data = [
            (None, 'Введи любое число', cfg.COLOR_LIME, 0.1),
            (None, 'от 1 до 100', cfg.COLOR_WHITE, 0.25),
            ('step_label', '', cfg.COLOR_LIME, 0.55),
            ('comment_label', '', cfg.COLOR_WHITE, 0.7),
            ('used_label', '', cfg.COLOR_LIME, 0.85)
        ]

        for idx, (name, text, color, rely) in enumerate(label_data):
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=cfg.FONT_LARGE
            )
            label.place(relx=0.5, rely=rely, anchor='c')
            if name: self.labels[name] = label

        self.entry = ctk.CTkEntry(
            self,
            **cfg.ENT_PARAMS
        )
        self.entry.place(relx=0.5, rely=0.4, anchor='c')

        button_data = [
            ('←', self.clear_input),
            ('→', self.send_input)
        ]

        for idx, (text, command) in enumerate(button_data):
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **cfg.LONG_BTN_PARAMS
            )
            button.place(
                relx=0.25 + (idx * 0.5),
                rely=0.4,
                anchor='c'
            )

    def send_input(self):
        self.controller.transfer_data(self.entry.get())

    def get_status(self, status, info):
        if status in cfg.ERROR_MESSAGES:
            error_message = CTkMessagebox(
                app,
                **cfg.MSG_PARAMS,
                message=cfg.ERROR_MESSAGES[status]
            )
            app.wait_window(error_message)
            self.clear_entry()
            return

        if status == 'win' or status == 'lose':
            self.controller.transfer_final_data(status, info)
            self.controller.switch_to('FinalPage')
            return


        comment_lbl = self.labels['comment_label']
        step_lbl = self.labels['step_label']
        used_lbl = self.labels['used_label']

        comment_lbl.configure(text=choice(cfg.GAME_WORDS[status]))
        step_lbl.configure(text=f'Осталось попыток: {info["step"]}')
        used_lbl.configure(text=info['used'])
        self.clear_entry()

    def update_ui(self, step):
        self.clear_entry()
        step_lbl = self.labels['step_label']
        step_lbl.configure(text=f'Осталось попыток: {step}')
        self.labels['comment_label'].configure(text='')
        self.labels['used_label'].configure(text='')

    def clear_entry(self):
        self.entry.delete(0, 'end')
        self.entry.focus_set()

    def clear_input(self):
        self.entry.delete(len(self.entry.get()) - 1)

class FinalPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.COLOR_DARK)
        self.controller = controller

        self.labels = {}

        label_data = [
            ('comment_label', "", cfg.COLOR_LIME),
            ('text_label', "Искомое число:", cfg.COLOR_WHITE),
            ('num_label', "", cfg.COLOR_LIME),
            ('used_label', "", cfg.COLOR_WHITE),
            ('count_label', "", cfg.COLOR_LIME),
            ('again_label', "Хотите повторить?", cfg.COLOR_WHITE)
        ]

        for idx, (name, text, color) in enumerate(label_data):
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=cfg.FONT_LARGE
            )
            label.place(
                relx=0.5,
                rely=0.1 + (idx * 0.14),
                anchor='c'
            )
            self.labels[name] = label

        button_data = [
            ('Не хочу', self.controller.exit_app),
            ('Давай!', self.controller.create_app)
        ]

        for idx, (text, command) in enumerate(button_data):
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **cfg.BTN_PARAMS
            )
            button.place(
                relx=0.35 + (idx * 0.3),
                rely=0.9,
                anchor='c'
            )

    def get_result(self, status, info):
        labels = self.labels
        comment_text = choice(cfg.FINAL_WORDS[status])
        used_text = f'Использованные числа:\n{info["used"]}'
        count_text = f'Потрачено попыток: {info["spent_steps"]}'

        labels['comment_label'].configure(text=comment_text)
        labels['num_label'].configure(text=info['num'])
        labels['used_label'].configure(text=used_text)
        labels['count_label'].configure(text=count_text)


class MessagePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.COLOR_DARK)
        self.controller = controller

        self.label = ctk.CTkLabel(
            self,
            text='',
            text_color=cfg.COLOR_LIME,
            font=cfg.FONT_MEDIUM
        )
        self.label.place(relx=0.5, rely=0.5, anchor='c')

    def change_message(self, status):
        self.label.configure(
            text=choice(cfg.ACTIVE_MESSAGES[status])
        )


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
            if (user_num - self.num) <= 5:
                status = 'too near high'
            else:
                status = 'too high'
        else:
            if (self.num - user_num) <= 5:
                status = 'too near low'
            else:
                status = 'too low'

        return status, info

    def update_variables(self):
        self.step = self.max_steps
        self.num = randint(1, 100)
        self.used_digits = []

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Угадай число')
        self.geometry('600x500+800+450')
        self.resizable(False, False)
        self.attributes('-alpha', 0.8)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True)

        self.main_logic = MainLogic()

        self.pages = {}
        self.current_frame = None
        page_types = [
            (cfg.STATIC_PAGES_DATA, StaticPages),
            (None, GamePage),
            (None, FinalPage),
            (None, MessagePage),
        ]

        for config_dict, page_class in page_types:
            if config_dict is not None:
                for page_name in config_dict.keys():
                    self.pages[page_name] = page_class(
                        master=self.main_frame,
                        controller=self,
                        page_name=page_name
                    )
            else:
                page_name = page_class.__name__
                self.pages[page_name] = page_class(
                    master=self.main_frame,
                    controller=self
                )
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

    def create_app(self):
        self.pages['MessagePage'].change_message('loading')
        self.switch_to('MessagePage')
        self.main_logic.update_variables()
        self.pages['GamePage'].update_ui(self.main_logic.step)
        self.after(3000, lambda: (self.switch_to('GamePage')))

    def exit_app(self):
        self.pages['MessagePage'].change_message('farewell')
        self.switch_to('MessagePage')
        self.after(3000, self.destroy)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()