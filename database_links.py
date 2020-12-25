"""Obsługa bazy linków do IMDb."""
from database import Database
from datetime import timezone, datetime
import csv

class DatabaseLinks(Database):
    """Obsługa bazy linków do IMDb."""

    def __init__(self):
        """Inicjowanie bazy linków do IMDb"""
        Database.__init__(self, 'links.csv', 
            ['movieId','imdbId','tmdbId'])

    def get_real_id(self, movieid):
        """Zwraca id filmu w bazie IMDb."""
        if self._get_database():
            return self._database.loc[self._database['movieId'] 
                == movieid]['imdbId'].values[0]
