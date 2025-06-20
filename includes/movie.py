# Class The Movie

class	Movie:

	def	__init__(self, title:str, genre:str, duration_minutes:int, age_restriction:int) -> None:

		self.title = title
		self.genre = genre
		self.duration_minutes = duration_minutes
		self.age_restriction = age_restriction

	def	get_info(self) -> str:

		return f'Title: {self.title}\nGenre: {self.genre}\nDuration: {self.duration_minutes} minutes\nAge restriction: {self.age_restriction}'

# movie = Movie("Name", "Genre", 120, 16)
# print(movie.get_info())