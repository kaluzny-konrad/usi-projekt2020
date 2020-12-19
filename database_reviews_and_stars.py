"""Obsługa bazy punktów i recenzji."""
from database import Database
from datetime import timezone, datetime
import csv

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
            + ',' + str(value) + ',' + str(time_stamp)) + '\n'
        try:
            with open(self._full_database_path, mode='a') as database_reviews:
                database_reviews.writelines(new_review_string) 
        except FileNotFoundError:
            return False
        except ValueError:
            return False
        return True

    def remove(self, userid, movieid):
        """Usuwa wartość z bazy, zwraca True jeżeli operacja się udała."""
        row_to_drop = self._row_of_review(userid, movieid)
        if row_to_drop == False:
            return False
            
        lines = list()
        try:
            with open(self._full_database_path, mode='r') as database_reviews:
                reader = csv.reader(database_reviews)
                for row in reader:
                    lines.append(row)
                    if row == row_to_drop:
                        lines.remove(row)

            with open(self._full_database_path, mode='w') as database_reviews:
                writer = csv.writer(database_reviews)
                writer.writerows(lines)

        except FileNotFoundError:
            return False
        except ValueError:
            return False
        return True

    def _row_of_review(self, userid, movieid):
        """Zwraca przygotowany wiersz dla określonego userid, movieid."""
        if self._get_database():
            try:
                review = self._database.loc[
                    self._database['userId'] == userid].loc[
                    self._database['movieId'] == movieid]
            except IndexError:
                return False

        prepared_row = []
        for row in review.values:
            for value in row:
                prepared_row.append(str(value))
        
        return prepared_row
