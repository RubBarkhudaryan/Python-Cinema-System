# Class Show Time

import datetime

from .movie import Movie
from utils.utils import print_seat

class	ShowTime:

	def	__init__(self, movie: Movie, time: str, row_count:int = 10) -> None:

		self.movie = movie
		self.time = time
		self.seats = []
		self.booked = dict()

		for i in range (row_count):
			self.seats.append([])
			for j in range (15):
				self.seats[i].append(1)
	
	@staticmethod
	def	display_seats(self) -> None:
		print("\033[32mAvailable, \033[31m Unavailable\n\033[0m")
		for i in range (len(self.seats)):
			for j in range (len(self.seats[i])):
				print_seat(i, j, self.seats[i][j])
			print()
		print()

	def	book_seat(self, seat: str) -> str | bool:

		splitted = seat.split("-")
		row = int(splitted[0])
		col = int(splitted[1])

		if self.seats[row - 1][col - 1] == 1:
			self.seats[row - 1][col - 1] = 0
			booking_id = seat + " " + datetime.datetime.now().date()
			self.booked[booking_id] = seat
			return booking_id
		return False

	def	cancel_booking(self, booking_id: str) -> bool:
		splited = booking_id.split(" ")
		seat = splited[0].split("-")
		row = int(seat[0])
		col = int(seat[1])
		if self.booked.pop(booking_id):
			self.seats[row - 1][col - 1] = 1
			return True
		return False