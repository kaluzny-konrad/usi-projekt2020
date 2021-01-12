import clear_terminal
from database_reviews import DatabaseReviews
from database_stars import DatabaseStars

class Reviews:
    """Zarządzanie recenzjami w serwisie."""

    def __init__(self, user, movie):
        """Inicjalizacja obsługi recenzji."""
        self._userid = user.get_userid()
        self._movieid = movie.get_movieid()
    
    def add(self):#, model): - BLOKADA MODELU
        """Dodawanie opinii i punktów do filmu."""
        if self.review_exists() == True:
            print("Opinia jest już dodana do tego filmu.")
        else:
            self._get_new_review()
            self._get_new_stars()
            #self._compare_value_of_review(model) - BLOKADA MODELU
            if self._user_wants_to_add_review():
                self._add_review_and_stars_to_base()

    def review_exists(self):
        """Zwraca True, jeżeli istnieje recenzja użytkownika do filmu."""
        self._get_rev_and_stars()
        if self._review or self._stars:
            return True
        else:
            return False

    def _get_rev_and_stars(self):
        databaseR = DatabaseReviews()
        databaseS = DatabaseStars()
        self._review = databaseR.get_for_user_movie(self._userid, self._movieid)
        self._stars = databaseS.get_for_user_movie(self._userid, self._movieid)

    def _get_new_review(self):
        """Odebranie opinii od użytkownika."""
        text_info = "Twoja opinia na temat filmu w języku angielskim: \n"
        self._new_review = input(text_info)

    def _get_new_stars(self):
        """Odebranie punktów od użytkownika."""
        text_info = "\nWprowadź ocenę filmu od 1 do 5:\n"
        try:
            self._new_stars = int(input(text_info))
            if self._new_stars > 5 or self._new_stars < 1:
                raise ValueError
        except ValueError:
            print("\nNależy podać liczbę od 1 do 5!")
            self._get_new_stars()

    #def _compare_value_of_review(self): - BLOKADA MODELU
    #    """Informacja z ML na temat punktacji.""" - BLOKADA MODELU
    #    predict = model.predict(self._new_review) - BLOKADA MODELU
    #    if predict < 0 and self._new_stars > 3: - BLOKADA MODELU
    #        print(f'Uwaga: Przyznano ponad 3 gwiazdki a opinia wygląda na negatywną.') - BLOKADA MODELU
    #    elif predict > 0 and self._new_stars < 3: - BLOKADA MODELU
    #        print(f'Uwaga: Przyznano mniej niż 3 gwiazdki a opinia wygląda na pozytywną.') - BLOKADA MODELU
        
    def _user_wants_to_add_review(self):
        """Decyzja czy dodać opinię."""
        text_info = "\nCzy chcesz dodać opinię? [t]ak / [n]ie:\n"
        user_decision = input(text_info).lower()
        if user_decision == 't':
            return True
        elif user_decision == 'n':
            return False
        else:
            "Podany został błędny znak!\n"
            return self._user_wants_to_add_review()

    def _add_review_and_stars_to_base(self):
        """Dodanie recenzji i gwiazdek do bazy."""
        if self._add_review_to_base():
            if self._add_stars_to_base():
                self._review_added()
            else:
                self._remove_added_review()
                self._review_not_added()

    def _add_review_to_base(self):
        """Dodanie recenzji filmowi z obsługą błędów."""
        databaseR = DatabaseReviews()
        if databaseR.add_new(self._userid, self._movieid, self._new_review):
            return True
        else:
            return False

    def _add_stars_to_base(self):
        """Dodanie przyznanych gwiazdek filmowi z obsługą błędów."""
        databaseS = DatabaseStars()
        if databaseS.add_new(self._userid, self._movieid, self._new_stars):
            return True 
        else:
            return False

    def _review_added(self):
        print('Recenzja została poprawnie dodana do bazy.')

    def _review_not_added(self):
        print('Baza nie odpowiada, spróbuj później.')

    def _remove_added_review(self):
        databaseR = DatabaseReviews()
        databaseR.remove(self._userid, self._movieid)

    def _remove_added_stars(self):
        databaseS = DatabaseStars()
        databaseS.remove(self._userid, self._movieid)

    def get_review(self):
        """Zwraca recenzję użytkownika do filmu."""
        self._get_rev_and_stars()
        print(f'\nTwoja recenzja: {self._review}')
        print(f'Przyznana ilość gwiazdek: {self._stars}\n')

    def drop(self):
        """Usuwa recencję użytkownika do filmu."""
        if self.review_exists() == True:
            self._drop_review_and_stars_from_base()
        else:
            print("Brak opinii do tego filmu.")

    def _drop_review_and_stars_from_base(self):
        """Usuwanie recenzji i gwiazdek z bazy."""
        self._remove_added_review()
        self._remove_added_stars()
