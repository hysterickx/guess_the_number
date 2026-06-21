COLOR_DARK = '#0d0a0c'
COLOR_LIME = '#99ff66'
COLOR_BLACK = '#000000'
COLOR_WHITE = '#ffffff'

FONT_LARGE = ('Constantia', 30)
FONT_MEDIUM = ('Constantia', 25)
FONT_SMALL = ('Constantia', 20)

ENT_PARAMS = {
    'width': 100,
    'height': 30,
    'border_width': 0,
    'corner_radius': 40,
    'justify': 'c',
    'font': FONT_LARGE
}

ENT_PLACE = {
    'relx': 0.5,
    'rely': 0.4,
    'anchor': 'c'
}

BTN_PARAMS = {
    'height': 40,
    'width': 50,
    'corner_radius': 50,
    'fg_color': COLOR_LIME,
    'hover_color': COLOR_WHITE,
    'text_color': COLOR_BLACK,
    'font': FONT_SMALL
}

LONG_BTN_PARAMS = {
    'height': 30,
    'width': 120,
    'corner_radius': 15,
    'fg_color': COLOR_LIME,
    'hover_color': COLOR_WHITE,
    'text_color': COLOR_BLACK,
    'font': FONT_SMALL
}

MSG_PARAMS = {
    'width': 300,
    'height': 150,
    'title': 'Ошибочка',
    'icon': 'info',
    'justify': 'center',
    'button_color': COLOR_WHITE,
    'button_hover_color': COLOR_LIME,
    'button_text_color': COLOR_BLACK
}

STATIC_PAGES_DATA = {
    'GreetingsPage': {
        'labels': [
            ('Привет! Это угадайка чисел', COLOR_LIME, FONT_LARGE, 0.5, 0.3),
            ('Хочешь сыграть?', COLOR_WHITE, FONT_LARGE, 0.5, 0.5)
        ],
        'buttons': [
            ('Не хочу', 'exit_app', 0.35, 0.7),
            ('Давай!', 'RulesPage', 0.65, 0.7),
        ]
    },
    'RulesPage': {
        'labels': [
            ('Правила очень простые:', COLOR_LIME, FONT_MEDIUM, 0.5, 0.05),
            ('Я загадываю число от 1 до 100', COLOR_WHITE, FONT_MEDIUM, 0.5, 0.2),
            ('А ты пытаешься его отгадать,', COLOR_LIME, FONT_MEDIUM, 0.5, 0.35),
            ('вводя свои варианты чисел', COLOR_WHITE, FONT_MEDIUM, 0.5, 0.5),
            ('У тебя несколько попыток', COLOR_LIME, FONT_MEDIUM, 0.5, 0.65),
            ('Начнём?', COLOR_WHITE, FONT_MEDIUM, 0.5, 0.8)
        ],
        'buttons': [
            ('Отлично', 'create_app', 0.5, 0.9)
        ]
    }
}

GAME_PAGE_DATA = {
    'labels': [
        (None, 'Введи любое число', COLOR_LIME, FONT_LARGE, 0.5, 0.1),
        (None, 'от 1 до 100', COLOR_WHITE, FONT_LARGE, 0.5, 0.25),
        ('step_lbl', '', COLOR_LIME, FONT_LARGE, 0.5, 0.55),
        ('comment_lbl', '', COLOR_WHITE, FONT_LARGE, 0.5, 0.7),
        ('used_lbl', '', COLOR_LIME, FONT_LARGE, 0.5, 0.85)
    ],
    'buttons': [
        ('←', 'delete_last_char', 0.25, 0.4),
        ('→', 'send_input', 0.75, 0.4)
    ],
    'static_txt': 'Осталось попыток:'
}


FINAL_PAGE_DATA = {
    'labels': [
        ('comment_lbl', '', COLOR_LIME, FONT_LARGE, 0.5, 0.1),
        ('text_lbl', 'Искомое число:', COLOR_WHITE, FONT_LARGE, 0.5, 0.24),
        ('num_lbl', '', COLOR_LIME, FONT_LARGE, 0.5, 0.38),
        ('used_lbl', '', COLOR_WHITE, FONT_LARGE, 0.5, 0.52),
        ('count_lbl', '', COLOR_LIME, FONT_LARGE, 0.5, 0.66),
        ('again_lbl', 'Хотите повторить?', COLOR_WHITE, FONT_LARGE, 0.5, 0.8)
    ],
    'buttons': [
        ('Не хочу', 'exit_app', 0.35, 0.9),
        ('Давай!', 'create_app', 0.65, 0.9)
    ],
    'used_numbers': 'Использованные числа:',
    'spent_steps': 'Потрачено попыток:'
}

MESSAGE_PAGE_DATA = {
    'text': '',
    'text_color': COLOR_LIME,
    'font': FONT_MEDIUM
}

MESSAGE_PAGE_PLACE = {
    'relx': 0.5,
    'rely': 0.5,
    'anchor': 'c'
}

DELAY_MESSAGES = {
    'waiting': [
        'Жду ответа от сервера...', 'Посылаю запрос...',
        'Нужно немного подождать...', 'Дай-ка подумать...',
        'Получаю твой ответ...'
    ],
    'loading': [
        'Генерирую цикл...',
        'Создаю всё с нуля...',
        'Очищаю всё лишнее...',
        'Отлично! Начинаем...',
        'Дай мне пару секундочек!'
    ],
    'farewell': [
        'До новых встреч!',
        'Заглядывай ко мне ещё!',
        'Был рад поработать с тобой!',
        'Ты это, заходи, если что...',
        'Надеюсь, еще увидимся!'
    ]
}

ERROR_MESSAGES = {
    'empty': 'В поле пусто',
    'too_many': 'Слишком много символов',
    'not_a_digit': 'Допускаются только цифры',
    'out_of_range': 'Введите число от 1 до 100 включительно',
    'it_was': 'Это число уже вводилось'
}

GAME_MESSAGES = {
    'too_low': [
        'Пока что маловато',
        'Маловато, давай еше',
        'Бери выше',
        'Нет, я загадал число побольше'
    ],
    'too_high': [
        'Тихо, тихо, не так много',
        'Что-то ты лишканул немножко',
        'Давай-ка поменьше',
        'Многовато',
        'Бери ниже'
    ],
    'near_low': [
        'Совсем рядом! Возьми выше',
        'Почти у цели! Возьми чуть больше',
        'Почти угадал, чуть выше!'
    ],
    'near_high': [
        'Очень близко! Давай ниже',
        'Еще чуть-чуть! Ниже',
        'Горячо! Чуть ниже'
    ],
    'win': [
        'Красавчик, это оно!',
        'В точку. Ты победил!',
        'Число угадано!',
        'Поздравляю!',
        'Это победа. Ура!'
    ],
    'lose': [
        'Все попытки потрачены!',
        'В этот раз не повезло...',
        'В следующий раз точно получится!',
        'Увы, лимит исчерпан...',
        'Мимо! Число победило...'
    ]
}