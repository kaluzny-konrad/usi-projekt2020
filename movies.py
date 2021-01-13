from database_movies import DatabaseMovies
import clear_terminal
from imdb import IMDb
from database_links import DatabaseLinks
class Movies:
    """Klasa do obsługi karty filmu."""
    def __init__(self):
        """Inicjowanie wartości domyślnych karty filmu."""
        self._movie_selected = False

    def show_list_range(self, first_row, last_row):
        """Drukuje listę filmów z bazy."""
        movies = DatabaseMovies()
        clear_terminal.clear()
        print("## Lista filmów ##\n")
        movies.show_list_range(first_row, last_row)

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
            self.show_movie_info()

    def get_title(self):
        """Zwraca tytuł wybranego filmu."""
        if self._movie_selected == True:
            movies = DatabaseMovies()
            return movies.get_title_from_id(self._movieid)

    def show_movie_info(self):
        """Wyświetla listę informacji o filmie."""
        movie_links = DatabaseLinks()
        real_imdb_id = movie_links.get_real_id(self._movieid)
        imdb_connect = IMDb()
        movie_info = imdb_connect.get_movie(real_imdb_id)
        
        if movie_info['plot'][0] != None:
            print('Fabuła:', movie_info['plot'][0])

        print('Reżyserzy:')
        for director in movie_info['directors']:
            print(director['name'])

        print('Gatunek:',movie_info['genres'][0])
        print()

    def get_movieid(self):
        """Zwraca id wybranego filmu."""
        if self._movie_selected == True:
           return self._movieid

    def base_size(self):
        """Zwraca wielkość bazy filmów."""
        movies = DatabaseMovies()
        movies._get_database()
        return movies.base_size()