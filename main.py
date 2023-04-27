# Константа, тому що цей словник не змінюється протягом коду
MISTAKES_MESSAGES = {'big_letter' : "Відсутні великі літери"
                       , 'small_letter' : "Відсутні маленькі літери"
                       , 'number' : "Відсутні числа"
                       , 'special_symbol' : "Відсутні спеціальні символи"
                       , 'no_forbidden_symbol' : "Присутні неприпустимі символи, які важко запам'ятати"}

# Винесла окремою константою для зручності, якщо користувач захоче змінити перелік дозволених символів
# Константа, тому що в коді не зазнає змін
ALLOWED_SYMBOLS = ('*', '-', '#')

'''
Основна функція перевірки паролю
Повідомлення користувачу не стала формувати через новий стрінг та "/n",
тому що у випадках, якщо повідомлення складається з одного рядку, це зайві дії,
а в інших різниця в терміналі не помітна
'''
def check_password(password):
    '''
    Окрема перевірка на довжину,
    як писала в тг, пароль менше 4 символів фізично не може задовольнити всім умовам,
    а в занадто довгому, на кшталт "studentANATOLIY2006#",
    людина може просто видалити вся символи після 12 і отримати "studentANATO",
    і виявиться що перевіряти символи не було сенсу - їх не залишилось
    '''
    if len(password) < 8:
        print("Пароль надто короткий його легко взламати")
    elif len(password) > 12:
        print("Пароль надто довгий його складно запам'ятати")
    else:
        checked_condition = check_symbols(list(password))
        if all(checked_condition.values()):
            print("Пароль ідеальний")
        else:
            for key, value in checked_condition.items():
                if not value:
                    print(MISTAKES_MESSAGES[key])
        
def check_symbols(password_symbols):
    # відстежує виконання умов
    symbol_condition = {'big_letter' : False
                       , 'small_letter' : False
                       , 'number' : False
                       , 'special_symbol' : False
                       , 'no_forbidden_symbol' : False}
    
    for symbol in password_symbols:
        # нічого кращого за перевірку через if-elif-else не змогла придумати
        if symbol.isupper():
            change_symbol_condition(symbol_condition, 'big_letter')
        elif symbol.islower():
            change_symbol_condition(symbol_condition, 'small_letter')
        elif symbol.isdigit():
            change_symbol_condition(symbol_condition, 'number')
        elif symbol in ALLOWED_SYMBOLS:
            change_symbol_condition(symbol_condition, 'special_symbol')
        elif symbol_condition.get('no_forbidden_symbol'):
            # також обрала elif аби не перезаписувати дарма
            symbol_condition['no_forbidden_symbol'] = False
    return symbol_condition

def change_symbol_condition(symbol_condition, key):
    # умови додала аби зайвий раз не перезаписувати значення
    if not symbol_condition.get(key):
        symbol_condition[key] = True
    if not symbol_condition.get('no_forbidden_symbol'):
        symbol_condition['no_forbidden_symbol'] = True

check_password(input("Введіть пароль: "))