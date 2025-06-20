# Class The Movie

class	Movie:

	def	__init__(self, title:str, genre:str, duration_minutes:int, age_restriction:int) -> None:

		self.title = title
		self.genre = genre
		self.duration_minutes = duration_minutes
		self.age_restriction = age_restriction

	def	get_info(self) -> str:

		return f'\033[35m Title: \033[0m {self.title} \n\033[35m Genre: \033[0m {self.genre} \n\033[35m Duration: \033[0m {self.duration_minutes} minutes \n\033[35m Age restriction: \033[0m {self.age_restriction}'