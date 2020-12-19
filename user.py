from database_users import DatabaseUsers
import clear_terminal
import time
class User:
    """Zarządzanie użytkownikiem serwisu."""

    def __init__(self):
        """Inicjalizacja obsługi użytkownika."""
        self._is_logged = False
        self._username = 'anonim'
        self._userid = None

    def login(self):
        """Logowanie użytkownika do serwisu."""
        if self._is_logged == False:
            clear_terminal.clear()
            print("\n## Logowanie do serwisu ##\n")
            self._get_new_username()
    
    def _get_new_username(self):
        username = input("Podaj login lub [p]owróć: ")
        if username == 'p' or username == 'P':
            pass
        else:
            self._get_new_password(username)

    def _get_new_password(self, username):
        password = input("Podaj hasło lub [p]owróć: ")
        if password == 'p' or password == 'P':
            self.login()
        else:
            self._try_login(username, password)
    
    def _try_login(self, username, password):
        users = DatabaseUsers()
        if users.is_correct_login_data(username, password):
            self._userid = users.get_id_from_username(username)
            self._is_logged = True
            self._username = username
            print(f'Witaj {self._username}!')
            time.sleep(1)
            clear_terminal.clear()
        else:
            print("Podano błędne dane logowania.\n")
            time.sleep(2)
            self.login()
            
    def logout(self):
        """Wylogowywanie użytkownika z systemu."""
        if self._is_logged == True:
            self._is_logged = False
            self._username = 'anonim'
            self._userid = None

    def get_username(self):
        return self._username

    def get_userid(self):
        """Zwraca userid zalogowanego użytkownika."""
        if self._is_logged == True:
            return self._userid