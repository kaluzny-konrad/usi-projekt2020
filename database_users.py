"""Obsługa bazy użytkowników."""
from database import Database

class DatabaseUsers(Database):
    """Obsługa bazy użytkowników."""
    
    def __init__(self):
        """Inicjowanie wartości domyślnych bazy."""
        Database.__init__(self, 'users.csv', ['userId', 'login', 'password'])

    def show_list(self):
        """Wyświetl listę użytkowników z bazy."""
        if self._get_database():
            print("LISTA UŻYTKOWNIKÓW:\n")
            for row in range(self._base_size()):
                print(self._get_id_from_rownum(row), 
                    ' - ', self._get_user_from_rownum(row))
        else:
            print("Baza nie odpowiada, spróbuj później!")

    def _get_user_from_rownum(self, value):
        """Zwraca nazwę użytkownika dla określonego miejsca w bazie."""
        if self._get_database():
            return self._database.loc[value].values[1]

    def is_correct_login_data(self, username, password):
        if self._get_database():
            try:
                if self._get_password(username) == password:
                    return True
                else:
                    return False
            except IndexError:
                return False
        else:
            print("Baza nie odpowiada, spróbuj później!")

    def _get_password(self, username):
        if self._get_database():
            return self._database.loc[
                self._database['login'] == username]['password'].values[0]

    def get_id_from_username(self, username):
        if self._get_database():
            return self._database.loc[self._database['login'] 
                == username]['userId'].values[0]
