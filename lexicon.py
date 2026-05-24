FRM_COLOR = '#0d0d0d'
TXT_COLOR_1 = '#99ff66'
TXT_COLOR_2 = '#ffffff'
BTN_COLOR_1 = '#99ff66'
BTN_COLOR_2 = '#ffffff'
BTN_COLOR_3 = '#000000'

BTN_PARAMS = {
    "height": 50,
    "corner_radius": 50,
    "fg_color": BTN_COLOR_1,
    "hover_color": BTN_COLOR_2,
    "text_color": BTN_COLOR_3,
    "font": ('Constantia', 20)
}

MSG_PARAMS = {
    "width": 300,
    "height": 150,
    "title": 'Ошибочка',
    "icon": 'info',
    "justify": 'center',
    "button_color": BTN_COLOR_2,
    "button_hover_color": BTN_COLOR_1,
    "button_text_color": BTN_COLOR_3
}

ERROR_MESSAGES = {
    'empty': 'В поле пусто',
    'too many': 'Слишком много символов',
    'not a digit': 'Допускаются только цифры',
    'out of range': 'Введите число от 1 до 100 включительно',
    'it was': 'Это число уже вводилось'
}

FAREWELL_WORDS = [
    'До новых встреч!',
    'Заглядывай ко мне ещё!',
    'Был рад поработать с тобой!',
    'Ты это, заходи, если что...',
    'Надеюсь, еще увидимся!'
]

LOADING_WORDS = [
    'Генерирую цикл...',
    'Создаю всё с нуля...',
    'Очищаю всё лишнее...',
    'Отлично! Начинаем...',
    'Дай мне пару секундочек!'
]

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