import os

# Initialize UI settings based on terminal size (width)

UI_fill_width = os.get_terminal_size()[0]
# UI_fill_width = 74
UI_user_menu_fill_char = '#'

# Initialize UI settings (for prompts) based on terminal size (width)

UI_input_fill_width = int(int(os.get_terminal_size()[0]) / 2) + 5
# UI_input_fill_width = 54
UI_input_fill_char = ' '

class User:
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password
        pass

    def get_username(self):
        return self._username

def print_user_menu(user: User) -> None:
    print()
    print(f" [ USER: {user.get_username()} ] ".center(UI_fill_width, UI_user_menu_fill_char))

def init_user_program(username: str, password: str) -> None:
    __logged_user = User(username=username, password=password)

    os.system("clear")
    print_user_menu(user=__logged_user)

    input("System ready ...".center(UI_fill_width, " "))
