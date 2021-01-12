import sys
import clear_terminal
from user import User
from movies import Movies
from database_reviews import DatabaseReviews
from reviews import Reviews
import settings

class Menu:
    """Klasa obsługująca działania użytkownika."""

    def __init__(self, model):
        """Inicjalizacja menu głównego."""
        self.user = User()
        self.movie = Movies()
        self.model = model
        self.choices = {
            "1": self.login_logout,
            "2": self.film_list,
        }

    def run(self):
        """Wyświetl opcje wyboru i odpowiedz na wybór."""
        try:
            while True:
                self.display_menu()
                choice = input("\nWybierz opcję: ")
                if choice == '0':
                    sys.exit(0)
                action = self.choices.get(choice)
                if action:
                    action()
                else:
                    print(f'{format(choice)} - nie ma takiej opcji.')
        except KeyboardInterrupt:
            sys.exit(0)

    def display_menu(self):
        """Wydrukuj opcje wyboru na ekranie."""
        clear_terminal.clear()
        print("##PORTAL IMDB - OCENIAJ FILMY!##")
        print("\n")
        if self.user._is_logged == True:
            print("1. Wyloguj się.")
        else:
            print("1. Zaloguj się.")
        print("2. Lista filmów.")
        print("0. Wyjdź z programu.")

    def login_logout(self):
        if self.user._is_logged == True:
            self.user.logout()
        else:
            self.user.login()

    def film_list(self):
        rows_in_list = settings.rows_in_list_movies
        first_row = 0
        last_row = first_row + rows_in_list
        base_size = self.movie.base_size()
        
        while True:
            self.movie.show_list_range(first_row, last_row)
            text_info = '\nWpisz ID filmu, przejdź do [n]astępnej lub p[o]przedniej strony lub [p]owróć do Menu głównego: '
            movieid = input(text_info)
            if movieid == 'p' or movieid == 'P':
                break
            elif  movieid == 'n' or movieid == 'N':
                if last_row + rows_in_list < base_size:
                    first_row = first_row + rows_in_list
                    last_row = last_row + rows_in_list
                else:
                    last_row = base_size
                    first_row = last_row - rows_in_list
            elif  movieid == 'o' or movieid == 'O':
                if first_row >= rows_in_list:
                    first_row = first_row - rows_in_list
                    last_row = last_row - rows_in_list
                else:
                    first_row = 0
                    last_row = first_row + rows_in_list
            elif self.movie.choose(movieid):
                self.movie.show_choosen_movie()
                if self.user._is_logged == True:
                    self.user_review()
                self.wait_for_exit()
                self.movie._movie_selected = False
            else:
                print('\nPodano błędną informację.')
                clear_terminal.clear(2)

    def user_review(self):
        """Sprawdzenie, czy użytkownik dodał już opinię do filmu."""
        self.revs = Reviews(self.user, self.movie)
        if self.revs.review_exists():
            self.revs.get_review()
            self.user_review_ask_for_delete()
        else:
            self.user_review_ask_for_add()

    def user_review_ask_for_delete(self):
        """Pozwala usunąć opinię użytkownikowi."""
        choice = input("Chcesz usunąć opinię? [t]ak/[n]ie: ")
        if choice == 'n' or choice == 'N':
            pass
        elif choice == 't' or choice == 'T':
            self.revs.drop()

    def user_review_ask_for_add(self):
        """Pozwala dodać opinię użytkownikowi."""
        choice = input("Chcesz dodać opinię? [t]ak/[n]ie: ")
        if choice == 'n' or choice == 'N':
            pass
        elif choice == 't' or choice == 'T':
            self.revs.add(self.model)
    
    def wait_for_exit(self):
        """Oczekuje na wyjście usera z danej karty."""
        text_info = '\nWpisz "p" aby powrócić: '
        while True:
            movieid = input(text_info)
            if movieid == 'p' or movieid == 'P':
                break