# Class Cinema

from .movie import Movie
from .showtime import ShowTime

class	Cinema:

	def	__init__(self, movies: list[Movie], showtimes: list[ShowTime]) -> None:
		self.movies = movies
		self.showtimes = showtimes

	def	add_movie(self, movie: Movie) -> bool:
		for mov in self.movies:
			if mov == movie:
				return False

		self.movies.append(movie)
		return True

	def	add_showtime(self, movie: Movie, time: str) -> bool:

		for show in self.showtimes:
			if show.time == time:
				return False

		show = ShowTime(movie, time)
		self.showtimes.append(show)
		return True
	
	def	list_movies(self) -> None:

		print("\033[33m All the movies that are available in our cinema are listed below.\n \033[0m")
		for mov in self.movies:
			print(mov.get_info())
			print()

	def	list_showtimes(self, movie_title: str) -> None:

		print(f"\033[33m Available showtimes for the movie: {movie_title}\n \033[0m")
		for show in self.showtimes:
			if show.movie.title == movie_title:
				print("Title: ", show.movie.title, " Time: ", show.time)

	def	find_showtime(self, movie_title, time) -> ShowTime | bool:
		for show in self.showtimes:
			if show.movie.title == movie_title and show.time == time:
				return show
		return False