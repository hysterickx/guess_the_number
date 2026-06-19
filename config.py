COLOR_DARK = '#0d0a0c'
COLOR_LIME = '#99ff66'
COLOR_BLACK = '#000000'
COLOR_WHITE = '#ffffff'

FONT_LARGE = ('Constantia', 30)
FONT_MEDIUM = ('Constantia', 25)
FONT_SMALL = ('Constantia', 20)

ENT_PARAMS = {
    "width": 100,
    "height": 30,
    "border_width": 0,
    "corner_radius": 40,
    "justify": 'c',
    "font": FONT_LARGE
}

BTN_PARAMS = {
    "height": 40,
    'width': 50,
    "corner_radius": 50,
    "fg_color": COLOR_LIME,
    "hover_color": COLOR_WHITE,
    "text_color": COLOR_BLACK,
    "font": FONT_SMALL
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
    "width": 300,
    "height": 150,
    "title": 'Ошибочка',
    "icon": 'info',
    "justify": 'center',
    "button_color": COLOR_WHITE,
    "button_hover_color": COLOR_LIME,
    "button_text_color": COLOR_BLACK
}

LOW_WORDS = [
    'Пока что маловато',
    'Маловато, давай еше',
    'Бери выше',
    'Нет, я загадал число побольше'
]

HIGH_WORDS = [
    'Тихо, тихо, не так много',
    'Что-то ты лишканул немножко',
    'Давай-ка поменьше',
    'Многовато',
    'Бери ниже'
]

VERY_NEAR_LOW_WORDS = [
    'Совсем рядом! Возьми выше',
    'Почти у цели! Возьми чуть больше',
    'Почти угадал, чуть выше!'
]

VERY_NEAR_HIGH_WORDS = [
    'Очень близко! Давай ниже',
    'Еще чуть-чуть! Ниже',
    'Горячо! Чуть ниже'
]

GAME_WORDS = {
    'too high': HIGH_WORDS,
    'too low': LOW_WORDS,
    'too near high': VERY_NEAR_HIGH_WORDS,
    'too near low': VERY_NEAR_LOW_WORDS
}

WIN_WORDS = [
    'Красавчик, это оно!',
    'В точку. Ты победил!',
    'Число угадано!',
    'Поздравляю!',
    'Это победа. Ура!'
]

LOSE_WORDS = [
    'Все попытки потрачены!',
    'В этот раз не повезло...',
    'В следующий раз точно получится!',
    'Увы, лимит исчерпан...',
    'Мимо! Число победило...'
]

FINAL_WORDS = {
    'win': WIN_WORDS,
    'lose': LOSE_WORDS
}

STATIC_PAGES_DATA = {
    'GreetingsPage': {
        'labels': [
            ('Привет! Это угадайка чисел', COLOR_LIME, FONT_LARGE, 0.4),
            ('Хочешь сыграть?', COLOR_WHITE, FONT_LARGE, 0.6)
        ],
        'buttons': [
            ('Не хочу', 'exit', 0.35),
            ('Давай!', 'next', 0.65),
        ]
    },
    'RulesPage': {
        'labels': [
            ('Правила очень простые:', COLOR_LIME, FONT_MEDIUM, 0.05),
            ('Я загадываю число от 1 до 100', COLOR_WHITE, FONT_MEDIUM, 0.2),
            ('А ты пытаешься его отгадать,', COLOR_LIME, FONT_MEDIUM, 0.35),
            ('вводя свои варианты чисел', COLOR_WHITE, FONT_MEDIUM, 0.5),
            ('У тебя несколько попыток', COLOR_LIME, FONT_MEDIUM, 0.65),
            ('Начнём?', COLOR_WHITE, FONT_MEDIUM, 0.8)
        ],
        'buttons': [
            ('Отлично', 'start', 0.5)
        ]
    }
}

ACTIVE_MESSAGES = {
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
    'too many': 'Слишком много символов',
    'not a digit': 'Допускаются только цифры',
    'out of range': 'Введите число от 1 до 100 включительно',
    'it was': 'Это число уже вводилось'
}