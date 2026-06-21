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

        for text, color, font, relx, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=font
            )
            label.place(relx=relx, rely=rely, anchor='c')

        for text, command_key, relx, rely in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=lambda cmd=command_key: \
                    controller.handle_command(cmd),
                **cfg.BTN_PARAMS
            )
            button.place(relx=relx, rely=rely, anchor='c')


class GamePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.COLOR_DARK)
        self.controller = controller

        labels = {}

        label_data = cfg.GAME_PAGE_DATA['labels']

        for name, text, color, font, relx, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=font
            )
            label.place(relx=relx, rely=rely, anchor='c')
            if name: labels[name] = label

        self.comment_lbl = labels['comment_label']
        self.step_lbl = labels['step_label']
        self.used_lbl = labels['used_label']
        self.static_txt = cfg.GAME_PAGE_DATA['static_text']

        self.entry = ctk.CTkEntry(
            self,
            **cfg.ENT_PARAMS
        )
        self.entry.place(**cfg.ENT_PLACE)

        command_map = {
            'clear': self.delete_last_char,
            'enter': self.send_input
        }

        button_data = cfg.GAME_PAGE_DATA['buttons']

        for text, command_key, relx, rely in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=command_map[command_key],
                **cfg.LONG_BTN_PARAMS
            )
            button.place(
                relx=relx,
                rely=rely,
                anchor='c'
            )

    def send_input(self):
        self.controller.handle_command(
            'transfer_data',
            self.entry.get()
        )

    def get_status(self, status, info):
        if status in cfg.ERROR_MESSAGES:
            error_message = CTkMessagebox(
                self.controller,
                **cfg.MSG_PARAMS,
                message=cfg.ERROR_MESSAGES[status]
            )
            self.controller.wait_window(error_message)
            self.clear_entry()
            return

        if status in ('win', 'lose'):
            self.controller.handle_command(
                'transfer_final_data',
                status, info
            )
            return

        self.comment_lbl.configure(
            text=choice(cfg.GAME_MESSAGES[status])
        )
        self.step_lbl.configure(
            text=f'{self.static_txt} {info["step"]}'
        )
        self.used_lbl.configure(text=info['used'])
        self.clear_entry()

    def update_ui(self, step):
        self.clear_entry()
        self.step_lbl.configure(
            text=f'{self.static_txt} {step}'
        )
        self.comment_lbl.configure(text='')
        self.used_lbl.configure(text='')

    def clear_entry(self):
        self.entry.delete(0, 'end')
        self.entry.focus_set()

    def delete_last_char(self):
        self.entry.delete(len(self.entry.get()) - 1)


class FinalPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.COLOR_DARK)
        self.controller = controller

        labels = {}

        label_data = cfg.FINAL_PAGE_DATA['labels']

        for name, text, color, font, relx, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=font
            )
            label.place(
                relx=relx,
                rely=rely,
                anchor='c'
            )
            labels[name] = label

        self.comment_lbl = labels['comment_label']
        self.num_lbl = labels['num_label']
        self.used_lbl = labels['used_label']
        self.count_lbl = labels['count_label']
        self.used_numbers_txt = cfg.FINAL_PAGE_DATA['used_numbers']
        self.spent_steps_txt = cfg.FINAL_PAGE_DATA['spent_steps']
        button_data = cfg.FINAL_PAGE_DATA['buttons']

        for text, command_key, relx, rely in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=lambda cmd=command_key: \
                    controller.handle_command(cmd),
                **cfg.BTN_PARAMS
            )
            button.place(
                relx=relx,
                rely=rely,
                anchor='c'
            )

    def get_result(self, status, info):
        num_txt = info['num']
        comment_txt = choice(cfg.GAME_MESSAGES[status])
        used_numbers = ", ".join(map(str, info['used']))
        used_txt = f'{self.used_numbers_txt}\n{used_numbers}'
        count_txt = f'{self.spent_steps_txt}{info["spent_steps"]}'

        self.comment_lbl.configure(text=comment_txt)
        self.num_lbl.configure(text=num_txt)
        self.used_lbl.configure(text=used_txt)
        self.count_lbl.configure(text=count_txt)


class MessagePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.COLOR_DARK)
        self.controller = controller

        self.label = ctk.CTkLabel(
            self,
            **cfg.MESSAGE_PAGE_DATA
        )
        self.label.place(**cfg.MESSAGE_PAGE_PLACE)

    def change_message(self, status):
        self.label.configure(
            text=choice(cfg.DELAY_MESSAGES[status])
        )


class MainLogic():
    def __init__(self):
        self.max_steps = 8
        self.update_variables()

    def check_input(self, user_input):
        if not user_input:
            return 'empty'
        if len(user_input) > 3:
            return 'too_many'
        if not user_input.isdigit():
            return 'not_a_digit'

        val = int(user_input)

        if val < 1 or val > 100:
            return 'out_of_range'
        if val in self.used_digits:
            return 'it_was'

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
            'used': self.used_digits,
            'num': self.num,
            'spent_steps': self.max_steps - self.step
        }

        if user_num == self.num:
            return 'win', info
        if self.step == 0:
            return 'lose', info
        if user_num > self.num:
            if (user_num - self.num) <= 5:
                status = 'near_high'
            else:
                status = 'too_high'
        else:
            if (self.num - user_num) <= 5:
                status = 'near_low'
            else:
                status = 'too_low'

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

    def handle_command(self, target, *args):
        if hasattr(self, target):
            method = getattr(self, target)
            if callable(method):
                method(*args)
                return

        self.switch_to(target)

    def transfer_data(self, user_input):
        status, info = self.main_logic.analyze_the_number(
            user_input
        )
        self.pages['GamePage'].get_status(status, info)

    def transfer_final_data(self, status, info):
        self.pages['FinalPage'].get_result(status, info)
        self.switch_to('FinalPage')

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