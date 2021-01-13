from pathlib import Path
import pandas as pd
import settings

class Database:
    """Klasa nadrzędna obsługująca wszystkie bazy plików."""

    def __init__(self, database_name, database_columns):
        """Inicjalizacja lokalizacji i kolumn bazy danych."""
        self._path_database = Path(settings.database_dir)
        self._database_name = database_name
        self._full_database_path = self._path_database/self._database_name
        self._database_columns = database_columns
    
    def _get_database(self):
        """Pobiera bazę w formacie Pandas. Zwraca True gdy operacja udana."""
        try:
            self._database = pd.read_csv(
                    self._full_database_path, sep=',',
                    usecols=self._database_columns)
        except FileNotFoundError:
            return False
        except ValueError:
            return False
        else:
            return True

    def _base_size(self):
        """Zwraca wielkość bazy."""
        try:
            return int(self._database.size / self._database.loc[0].size)
        except ValueError:
            return 0

    def _get_id_from_rownum(self, value):
        """Zwraca id dla określonego miejsca w bazie."""
        return self._database.loc[value].values[0]

    def _get_id_list(self):
        """Zwaraca listę id w bazie."""
        id_list = []
        if self._get_database():
            for row in range(self._base_size()):
                id_list.append(self._get_id_from_rownum(row))
        return id_list