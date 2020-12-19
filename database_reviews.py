"""Obsługa bazy recenzji."""
from database_reviews_and_stars import DatabaseReviewsAndStars

class DatabaseReviews(DatabaseReviewsAndStars):
    """Obsługa bazy recenzji."""
    
    def __init__(self):
        """Inicjowanie wartości domyślnych bazy."""
        DatabaseReviewsAndStars.__init__(self, 'reviews.csv', 
            ['userId', 'movieId', 'review', 'timestamp'], 'review')
