"""Obsługa bazy gwiazdek."""
from database_reviews_and_stars import DatabaseReviewsAndStars

class DatabaseStars(DatabaseReviewsAndStars):
    """Obsługa bazy gwiazdek."""
    
    def __init__(self):
        """Inicjowanie wartości domyślnych bazy."""
        DatabaseReviewsAndStars.__init__(self, 'stars.csv', 
            ['userId', 'movieId', 'stars', 'timestamp'], 'stars')
