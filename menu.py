import sys
import clear_terminal
from user import User
from movies import Movies
from database_reviews import DatabaseReviews
from reviews import Reviews

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
        self.movie.show_list()
        text_info = '\nWpisz ID filmu lub [p]owróć do Menu głównego: '
        movieid = input(text_info)
        if movieid == 'p' or movieid == 'P':
            pass
        elif self.movie.choose(movieid):
            stay_on_site = 'stay'
            while stay_on_site != 'p':
                self.movie.show_choosen_movie()
                if self.user._is_logged == True:
                    self.user_review()
                stay_on_site = input('[p]owróć do listy filmów: ')
            self.movie._movie_selected = False
            self.film_list()
        else:
            clear_terminal.clear(2)
            self.film_list()

    def user_review(self):
        self.revs = Reviews(self.user, self.movie)
        if self.revs.review_exists():
            self.revs.get_review()
        else:
            choice = input("chcesz dodać opinię? [t]ak/[n]ie:")
            if choice == 'n' or choice == 'N':
                pass
            elif choice == 't' or choice == 'T':
                self.revs.add(self.model)