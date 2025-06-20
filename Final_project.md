# **Final Project: Cinema Booking System**

## **Project Theme**

You're going to simulate a simple cinema booking system where users can view available movies, showtimes, and seats, and make or cancel bookings.

---

## **Main Requirements (100 points total)**

### **1. Define a class `Movie` (10 points)**

Each `Movie` object should include:

* Attributes: `title`, `genre`, `duration_minutes`, `age_restriction`
* Method: `get_info()` that returns all movie details as a string

### **2. Define a class `Showtime` (15 points)**

Each showtime should represent a movie being shown at a specific time with a set of seats:

* Attributes: `movie`, `time`, `seats` (use a list of booleans or 0/1 for availability)
* Methods:

  * `display_seats()` to print which seats are free/booked
  * `book_seat(seat_number)`
  * `cancel_booking(seat_number)`

### **3. Define a class `Cinema` (20 points)**

Cinema manages all movies and showtimes:

* Attributes: list of `movies`, list of `showtimes`
* Methods:

  * `add_movie(movie)`
  * `add_showtime(movie, time)`
  * `list_movies()`
  * `list_showtimes(movie_title)`
  * `find_showtime(movie_title, time)`

### **4. Command-line interface using `argparse` (15 points)**

Allow the user to:

* Add a new movie or showtime
* View available movies and showtimes
* Book/cancel a seat for a specific showtime
  Example:

```bash
python main.py --add-movie "Inception" --genre "Sci-Fi" --duration 148
python main.py --add-showtime "Inception" --time "19:00"
python main.py --book-seat "Inception" --time "19:00" --seat 5
```

### **5. Use proper class design and OOP features (10 points)**

* Encapsulation: make attributes protected or private where necessary
* Use `@classmethod`, `@staticmethod` where it makes sense
* Example: Static method to generate seat maps

### **6. Add `__str__` or `__repr__` to your classes (5 points)**

* Return clean and informative strings for printing

### **7. Group everything under `main.py` (10 points)**

* Either define all classes in the same file or import from modules
* Use a proper script entry point:

```python
if __name__ == "__main__":
    main()
```

### **8. Add documentation and comments (5 points)**

* Use Python-style docstrings for each class and method
* Comment on complex logic, if any

### **9. Implement a Booking ID system (10 points)**

* When booking a seat, generate a unique booking ID (e.g., using a counter or a timestamp)
* Allow users to cancel booking using this ID

---

## **Total: 100 Points**

| Task                             | Points  |
| -------------------------------- | ------- |
| Movie class                      | 10      |
| Showtime class                   | 15      |
| Cinema class                     | 20      |
| Command-line interface           | 15      |
| OOP best practices               | 10      |
| Dunder methods (`__str__`, etc.) | 5       |
| `main.py` structure              | 10      |
| Docstrings & comments            | 5       |
| Booking ID system                | 10      |
| **Total**                        | **100** |

---

## **Optional Extensions (Bonus)**

**+10 Design Patterns**

* Use the **Factory pattern** to create `Movie` or `Showtime` objects
* Use the **Singleton pattern** for the `Cinema` class (ensure only one cinema instance)

**+10 Data Structures**

* Use a `dict` to manage bookings by booking ID
* Store seats as a 2D list to simulate rows and columns

**+10 Algorithm**

* Add a basic recommendation system:

  * Suggest popular movies (most seats booked)
  * Suggest showtimes with best seat availability

**+10 Accounts**

* Add different types of user accounts:

  * Accounts with different access control (premium, standart, e.t.c)
  * Accounts with different age access control (adult, child)

**Optionally use VCS(github) if you can and add UI as well.**
