from database_movies import DatabaseMovies
import clear_terminal

class Movies:
    def __init__(self):
        """Inicjowanie wartości domyślnych."""
        self._movie_selected = False

    def show_list(self):
        """Drukuje listę filmów z bazy."""
        movies = DatabaseMovies()
        clear_terminal.clear()
        print("## Lista filmów ##\n")
        movies.show_list()

    def choose(self, movieid):
        """Pozwala wybrać użytkownikowi film z listy. True: film wybrany. False: powrót."""
        if self._movie_selected == False:
            movies = DatabaseMovies()
            try:
                movieid = int(movieid)
            except ValueError:
                print("\nPodano błędne ID!\n")
                self._movie_selected = False
                return False

            if movieid in movies._get_id_list():
                self._movieid = movieid
                self._movie_selected = True
                return True
            else:
                print("\nPodano błędne ID!\n")
                self._movie_selected = False
                return False

    def show_choosen_movie(self):
        """Pokazuje stronę na podstawie posiadanego id filmu."""
        if self._movie_selected == True:
            clear_terminal.clear()
            print(self.get_title())

    def get_title(self):
        """Zwraca tytuł wybranego filmu."""
        if self._movie_selected == True:
            movies = DatabaseMovies()
            return movies.get_title_from_id(self._movieid)

    def get_movieid(self):
        """Zwraca id wybranego filmu."""
        if self._movie_selected == True:
           return self._movieid