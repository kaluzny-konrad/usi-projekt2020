"""Obsługa bazy filmów."""
from database import Database

class DatabaseMovies(Database):
    """Obsługa bazy filmów."""

    def __init__(self):
        """Inicjowanie wartości domyślnych bazy."""
        Database.__init__(self, 'movies.csv', ['movieId', 'title'])

    def show_list(self):
        """Wyświetl listę wszystkich filmów z bazy."""
        if self._get_database():
            for row in range(self._base_size()):
                print(self._get_id_from_rownum(row), 
                    ' - ', self._get_title_from_rownum(row))
        else:
            print("Baza nie odpowiada, spróbuj później!")

    def _get_title_from_rownum(self, value):
        """Zwraca tytuł filmu dla określonego miejsca w bazie."""
        if self._get_database():
            return self._database.loc[value].values[1]

    def get_title_from_id(self, received_id):
        """Zwraca tytuł filmu dla określonego id w bazie."""
        if self._get_database():
            for row in range(self._base_size()):
                if self._get_id_from_rownum(row) == received_id:
                    return self._get_title_from_rownum(row)