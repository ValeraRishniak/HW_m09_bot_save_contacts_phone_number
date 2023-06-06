# словник що зберігає номери телефонів 
contacts = {"cat": '342',
            'dog': '098098'}


# Декоратор
def input_error(some_func):
    def wrapper(*args):
        try:
            result = some_func(*args)
            return result
        except KeyError:
            return('Wrong name. Please, try again. ')
        except ValueError:
            return('Phone\'s number is not correct! Please, try again. ')
        except IndexError:
            return("I don\'t understand. Please, give me name and phone please. ")
    return wrapper


# Основна функція
@input_error
def main():
    while True:
        command = input('Please, enter command: ')
        if command in (".", ):
            break
        command = command.lower().split()
        for key in commands:
            if command[0] in key:
                print(commands[key](command[0:]))


# Функції що обробляють запити користувача
@input_error
def hello(*args):
    return 'Hello! How can I help you? '

@input_error
def add_name_and_phone(command):
    name = command[-2]
    phone = command[-1]
    contacts[name] = phone
    result = f"Contact {name} with tel.number {phone} added to your contacts."

    return result

@input_error
def change_phone(command):
    name = command[-2]
    phone = command[-1]
    if name in contacts:
        contacts[name] = phone
        result = f'Phone number for contact {name} was changed to: {contacts[name]}'
        return result
    else:
        raise KeyError


@input_error
def get_phone(command):
    name = command[1]
    result = f'{name}: {contacts[name]}'
    return result


@input_error
def show_all(*args):
    if len(contacts) == 0:
        return 'Your contacts book is empty'
    text_to_return = 'These are all your contacts: \n'
    for name, phone in contacts.items():
        text_to_return += f'{name} - {phone}\n'
    return text_to_return

@input_error
def close_bot(*args):
    print("Good bye!")
    quit()

# словник із командами
commands = {'hello':    hello,
            'add':      add_name_and_phone,
            'change':   change_phone,
            'phone':    get_phone,
            'show all': show_all,
            'all':      show_all,                      
            'good bye': close_bot,
            'bye':      close_bot,
            'close':    close_bot,
            'exit':     close_bot 
            }





# Запуск бота-помічника
if __name__ == "__main__":
    main()