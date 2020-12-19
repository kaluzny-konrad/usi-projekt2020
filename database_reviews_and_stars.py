"""Obsługa bazy punktów i recenzji."""
from database import Database
from datetime import timezone, datetime

class DatabaseReviewsAndStars(Database):
    """Obsługa bazy recenzji i gwiazdek."""

    def __init__(self, database_name, database_columns, main_column):
        Database.__init__(self, database_name, database_columns)
        self.main_column = main_column

    def get_for_user_movie(self, userid, movieid):
        """Zwraca wartość przyznaną przez określonego użytkownika filmowi."""
        if self._get_database():
            try:
                return self._database.loc[
                        self._database['userId'] == userid
                    ].loc[
                        self._database['movieId'] == movieid
                    ][self.main_column].values[0]
            except IndexError:
                return False

    def add_new(self, userid, movieid, value):
        """Dodaje do bazy wartości. Zwraca True gdy operacja się powiedzie."""
        time_stamp = int(datetime.now(tz=timezone.utc).timestamp())
        new_review_string = (str(userid) + ',' + str(movieid) 
            + ',' + str(value) + ',' + str(time_stamp))
        try:
            with open(self._full_database_path, mode='a') as database_reviews:
                database_reviews.writelines(new_review_string) 
        except FileNotFoundError:
            return False
        except ValueError:
            return False
        return True

    def remove(self, userid, movieid):
        """Usuwa wartość z bazy."""
        pass