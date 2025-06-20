from movie import Movie
from cinema import Cinema

def	print_seat(i, j, seat):
	if seat:
		if (i >= 9 and j < 9):
			print(f"\033[32m| {i + 1}-{j + 1}|\033[0m", end="  ")
		elif i >= 9 and j >= 9:
			print(f"\033[32m| {i + 1}-{j + 1}|\033[0m", end="  ")
		else:
			print(f"\033[32m| {i + 1}-{j + 1} |\033[0m", end="  ")
	else:
		if (i >= 9 or j >= 9):
			print(f"\033[31m| {i + 1}-{j + 1}|\033[0m", end="  ")
		elif i >= 9 and j >= 9:
			print(f"\033[31m| {i + 1}-{j + 1}|\033[0m", end="  ")
		else:
			print(f"\033[31m| {i + 1}-{j + 1} |\033[0m", end="  ")


def	add_movie(args):
	cinema :Cinema = args.data

	mov = cinema.find_movie(args.title)

	if not movie:
		movie = Movie(args.title, args.genre, int(args.duration), int(args.age_r))
		cinema.add_movie(movie)
		print("Movie added successfully")
		return
	else:
		print("Movie already exists")

def	list_movies(args):
	cinema :Cinema = args.data
	cinema.list_movies()

def	list_showtimes(args):
	cinema :Cinema = args.data
	cinema.list_showtimes(args.title)

def	add_showtime(args):
	cinema :Cinema = args.data

	movie = cinema.find_movie(args.title)
	if not movie:
		print(f"\033[31m No movie called {args.title} — add it first please. \033[0m")
		return
	cinema.add_showtime(movie, args.time)
	print("\033[32m Showtime added successfully. \033[0m")

def	add_booking(args):

	cinema :Cinema = args.data

	for sh in cinema.showtimes:
		if sh.movie.title == args.title and sh.time == args.time:
			id = sh.book_seat(args.seat_pos)
			if id != False:
				print("\033[32m Seat booked successfully! \n\033[0m")
				print(f"Save your booking_id for further actions.\n\033[35mBooking id: {id}\033[0m")
			return
	print(f"\033[31m Sorry but there is no showtime for {args.title} at {args.time} \n\033[0m")

def cancel_booking(args):
	cinema: Cinema = args.data
	for sh in cinema.showtimes:
		if sh.movie.title == args.title and sh.time == args.time:
			ok = sh.cancel_booking(args.booking_id)
			print("\033[32m Canceled \n\033[0m" if ok else "\033[31m Booking not found.\n \033[0m")
			return
	print("\033[31mShowtime not found.\n\033[0m")