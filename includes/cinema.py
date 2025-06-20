# Class Cinema

from movie import Movie
from showtime import ShowTime

class	Cinema:

	def	__init__(self, movies: list[Movie], showtimes: list[ShowTime]) -> None:
		self.movies = movies
		self.showtimes = showtimes

	def	add_movie(self, movie: Movie) -> bool:
		for mov in self.movies:
			if mov == movie:
				return (False)
		
		self.movies.append(movie)
		return (True)

	def	add_showtime(self, movie: Movie, time: str) -> bool:

		for show in self.showtimes:
			if show.time == time:
				return (False)

		show = ShowTime(movie, time, 10)
		self.showtimes.append(show)
		return (True)
	
	def	list_movies(self) -> None:

		print("All the movies that are available in our cinema are listed below.\n")
		for mov in self.movies:
			print(mov.get_info())
			print()

	def	list_showtimes(self, movie_title: str) -> None:

		print(f"Available showtimes for the movie: {movie_title}\n")
		for show in self.showtimes:
			if show.movie.title == movie_title:
				print(show.movie.title)
				print(show.time)

	def	find_showtime(self, movie_title, time) -> ShowTime | bool:
		for show in self.showtimes:
			if show.movie.title == movie_title and show.time == time:
				return show
		return False
