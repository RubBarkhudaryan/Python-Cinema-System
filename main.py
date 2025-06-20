from includes.movie import Movie
from includes.showtime import ShowTime
from includes.cinema import Cinema

import argparse

def	add_movie(args):
	cinema :Cinema = args.data
	movie = Movie(args.title, args.genre, int(args.duration), int(args.age_r))
	cinema.add_movie(movie)

def	list_movies(args):
	cinema :Cinema = args.data
	cinema.list_movies()

def	list_showtimes(args):
	cinema :Cinema = args.data
	cinema.list_showtimes(args.title)

def	add_showtime(args):
	cinema :Cinema = args.data
	movie = Movie(args.title, args.genre, int(args.duration), int(args.age_r))
	cinema.add_showtime(movie, args.time)

def	add_booking(args):

	cinema :Cinema = args.data

	for sh in cinema.showtimes:
		if sh.movie.title == sh.title and sh.time == sh.time:
			break
	id = sh.book_seat(args.seat_pos)
	if id != False:
		print("\033[32m Seat booked successfully! \n\033[0m")
		print(f"Save your booking_id for further actions.\n\033[35mBooking id: {id}\033[0m")

def	cancel_booking(args):

	cinema :Cinema = args.data

	for show in cinema.showtimes:
		if show.title == args.title and show.time == args.time:
			break
	if show.cancel_booking(args.booking_id):
		print("\033[32m Booking canceled successfully! See you next time! \n\033[0m")


def	main():

	cinema = Cinema([], [])

	parser = argparse.ArgumentParser(
		prog="python3 main.py",
		description="Cinema management simple system CLI"
	)
	subs = parser.add_subparsers(dest="cmd", required=True)

	p = subs.add_parser("add-movie", help="Add a movie to a list")
	p.add_argument("--title", required=True, help="Movie title")
	p.add_argument("--genre", required=True, help="Movie genre")
	p.add_argument("--duration", required=True, help="Movie duration in minutes")
	p.add_argument("--age-r", required=True, help="Movie age retsriction")
	p.set_defaults(func=add_movie, data=cinema)

	p = subs.add_parser("add-showtime", help="Add a showtime to list")
	p.add_argument("--title", required=True, help="Movie title")
	p.add_argument("--genre", required=True, help="Movie genre")
	p.add_argument("--duration", required=True, help="Movie duration in minutes")
	p.add_argument("--age-r", required=True, help="Movie age retsriction")
	p.add_argument("--time", required=True, help="Showtime time")
	p.set_defaults(func=add_showtime, data=cinema)

	p = subs.add_parser("view-movies", help="View movies")
	p.set_defaults(func=list_movies, data=cinema)

	p = subs.add_parser("view-showtimes", help="View movie showtimes")
	p.add_argument("--title", required=True, help="Movie title which are looking for")
	p.set_defaults(func=list_showtimes, data=cinema)

	p = subs.add_parser("book-seat", help="Seat booking part - seat numbers consist of 2 parts:\nrow-col => row - row number,\ncol - column number")
	p.add_argument("--title", required=True, help="Movie name which you want to book")
	p.add_argument("--time", required=True, help="Movie session time")
	p.add_argument("--seat-pos", required=True, help="Hall seat position")
	p.set_defaults(func=add_booking, data=cinema)

	p = subs.add_parser("cancel-seat", help="Seat booking part - seat numbers consist of 2 parts:\nrow-col => row - row number,\ncol - column number")
	p.add_argument("--title", required=True, help="Movie name which you want to book")
	p.add_argument("--time", required=True, help="Movie session time")
	p.add_argument("--booking-id", required=True, help="Booking id")
	p.set_defaults(func=cancel_booking, data=cinema)

	args = parser.parse_args()
	args.func(args)

	cinema.list_showtimes("hello")

	# while True:
	# 	True

if __name__ == "__main__":
	main()