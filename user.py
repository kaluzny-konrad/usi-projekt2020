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
            self._get_username()
    
    def _get_username(self):
        username = input("Podaj login, [z]arejestruj się lub [p]owróć: ")
        if username == 'p' or username == 'P':
            pass
        elif username == 'z' or username == 'z':
            self.create_new_account()
        else:
            self._get_password(username)

    def _get_password(self, username):
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
        """Zwraca nazwę użytkownika z klasy."""
        return self._username

    def get_userid(self):
        """Zwraca userid zalogowanego użytkownika."""
        if self._is_logged == True:
            return self._userid

    def create_new_account(self):
        """Tworzy nowe konto wg danych podanych przez użytkownika."""
        clear_terminal.clear()
        print("-- Tworzenie nowego konta --")
        self._get_new_login()

    def _get_new_login(self):
        """Pobiera unikalny login od użytkownika."""
        print('\nLogin powinien mieć przynajmniej 6 znaków i nie zaczynać się od liczby.')
        username = input("Podaj login lub [p]owróć: ")
        if username == 'p' or username == 'P':
            pass
        else:
            if self._check_new_login(username):
                self._get_new_password(username)
            else:
                self._get_new_login()

    def _check_new_login(self, username):
        """Sprawdza, czy podany login jest unikalny i poprawny."""
        if len(username) >= 6 and username[0].isalpha():
            users = DatabaseUsers()
            if users.get_id_from_username(username):
                print('\nPodany login znajduje się już w bazie.')
                return False
            else:
                return True
        else:
            print('\nPodany login jest błędny.')
            return False

    def _get_new_password(self, username):
        """Pobiera hasło od użytkownika."""
        print('\nHasło powinno mieć przynajmniej 6 znaków i nie zaczynać się od liczby.')
        password = input("Podaj hasło lub [p]owróć: ")
        if password == 'p' or password == 'P':
            self._get_new_login()
        else:
            if self._check_new_password(password):
                users = DatabaseUsers()
                users._get_database()
                if users.add_new(username, password):
                    print('\nUdało się utworzyć nowe konto.')
                else:
                    print('\nTworzenie konta nieudane.')
            else:
                self._get_new_password(username)

    def _check_new_password(self, password):
        """Sprawdza, czy podane hasło jest poprawne."""
        if len(password) >= 6 and password[0].isalpha():
            return True
        else:
            print('\nPodane hasło jest błędne.')
            return False