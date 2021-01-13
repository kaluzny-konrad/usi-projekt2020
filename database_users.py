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
        """Zwraca True, jeżeli dane logowania podane przez użytkownika są poprawne."""
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
        """Pobiera hasło użytkownika z bazy."""
        if self._get_database():
            return self._database.loc[
                self._database['login'] == username]['password'].values[0]

    def get_id_from_username(self, username):
        """Pobiera id użytkownika o podanym username."""
        if self._get_database():
            try:
                userid = self._database.loc[self._database['login'] 
                    == username]['userId'].values[0]
            except IndexError:
                return False
            return userid

    def add_new(self, username, password):
        """Tworzy nowe konto użytkownika wg loginu i hasła."""
        userid_int = self._get_last_id()
        userid = self._build_userid_from_int(userid_int+1)
        new_string = (str(userid) + ',' + str(username) 
            + ',' + str(password) + '\n')
        try:
            with open(self._full_database_path, mode='a') as database:
                database.writelines(new_string) 
        except FileNotFoundError:
            return False
        except ValueError:
            return False
        return True

    def _get_last_id(self):
        """Zwraca ostatnie userid w postaci INTa."""
        return self._database.loc[self._base_size()-1].values[0]
    
    def _build_userid_from_int(self, userid_int):
        """Zamienia INT na poprawny format userid."""
        lenght_of_zeros = 5-len(str(userid_int))
        zeros = '0' * lenght_of_zeros
        return zeros + str(userid_int)