# Class Show Time

from movie import Movie
from utils.utils import print_seat

class	ShowTime:

	def	__init__(self, movie: Movie, time: str, row_count:int) -> None:

		self.movie = movie
		self.time = time
		self.seats = []

		for i in range (row_count):
			self.seats.append([])
			for j in range (15):
				self.seats[i].append(1)
	
	def	display_seats(self) -> None:
		print("\033[32mAvailable, \033[31m Unavailable\n \033[0m")
		for i in range (len(self.seats)):
			for j in range (len(self.seats[i])):
				print_seat(i, j, self.seats[i][j])
			print()
		print()

	def	book_seat(self, seat: str) -> bool:

		splitted = seat.split("-")
		row = int(splitted[0])
		col = int(splitted[1])

		if self.seats[row - 1][col - 1] == 1:
			self.seats[row - 1][col - 1] = 0
			return (True)
		else:
			return (False)

	def	cancel_booking(self, seat: str) -> bool:

		splitted = seat.split("-")
		row = int(splitted[0])
		col = int(splitted[1])

		if self.seats[row - 1][col - 1] == 0:
			self.seats[row - 1][col - 1] = 1
			return (True)
		else:
			return (False)
		

# movie = Movie("Name", "Genre", 120, 16)
# show = ShowTime(movie, "15:45", 10)

# if show.book_seat("1-1"):
# 	print("Booked successfully")
# 	show.display_seats()

# if show.cancel_booking("1-1"):
# 	print("Booking cancelled")
# 	show.display_seats()