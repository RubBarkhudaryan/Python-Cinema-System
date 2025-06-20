import argparse
import shlex
import sys

from cinema import Cinema
from utils import add_booking, add_showtime, add_movie, cancel_booking, list_movies, list_showtimes

def	init_parser(cinema: Cinema) -> None:
	parser = argparse.ArgumentParser(
		prog="python3 main.py",
		description="Cinema management simple system CLI"
	)
	subs = parser.add_subparsers(dest="cmd", required=True)

	p = subs.add_parser("add-movie", help="Add a movie to a list")
	p.add_argument("--title", required=True, help="Movie title")
	p.add_argument("--genre", required=True, help="Movie genre")
	p.add_argument("--duration", required=True, type=int, help="Movie duration in minutes")
	p.add_argument("--age-r", required=True, type=int, help="Movie age retsriction")
	p.set_defaults(func=add_movie, data=cinema)

	p = subs.add_parser("add-showtime", help="Add a showtime to list")
	p.add_argument("--title", required=True, help="Movie title")
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

	parser.add_argument("-h", "--help", action="help")
	return parser


def	main():

	cinema = Cinema([],[])

	parser = init_parser(cinema)

	# if invoked with arguments, just run once
	if len(sys.argv) > 1:
		args = parser.parse_args()
		args.func(args)
		return

	# otherwise enter REPL
	print("Enter commands (type 'exit' or 'quit' to leave).")
	while True:
		try:
			line = input("cinema> ").strip()
		except EOFError:
			break
		if not line or line in ("exit", "quit"):
			break

		# split into argv list, respecting quotes
		try:
			argv = shlex.split(line)
		except ValueError as e:
			print("Parse error:", e)
			continue

		# inject the sub‑parser name if missing?
		# (only necessary if you want to allow bare flags)
		try:
			args = parser.parse_args(argv)
			if not hasattr(args, "func"):
				print("Unknown command. Try 'view-movies', 'add-movie', etc.")
				continue
			args.func(args)
		except SystemExit:
			# argparse throws this on parse errors or `--help`
			continue

	print("Goodbye. 👋")

if __name__ == "__main__":
	main()