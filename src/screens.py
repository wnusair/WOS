from wissampy import cprint, clear_screen, register_user, login_user, create_db

class Screen:
    def __init__(self, title: str, options: list) -> None:
        self.title = title
        self.options = options
    
    def display(self) -> str:
        clear_screen()
        cprint(self.title, "green")
        for option in self.options:
            cprint(option, "blue")
        
        choice = input("Enter your choice: ")
        return choice
        