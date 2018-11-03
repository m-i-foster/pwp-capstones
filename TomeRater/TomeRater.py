# User Class
class User(object):
    """
    User class.
    """
    def __init__(self, name, email):
        """
        The constructor for the User class

        Parameters:
        :param name:
        :param email:
        """
        self.name = name
        self.email = email
        self.books = {}

    def get_name(self):
        """
        Get and return a user name.

        :return: User name.
        """
        return self.name

    def get_email(self, email):
        """
        Returns an email with a email check for valid format.

        :param email:

        :return: Error message if email is not in a valid format, or return email if valid.
        """
        try:
            email_parts = email.split('@')
            if len(email_parts) != 2 or not email_parts[0] or not email_parts[1]:
                raise InvalidEmailError()
        except InvalidEmailError:
            print("'%s' is not a valid email address." % email)
        else:
            return self.email

    def change_email(self, address):
        """
        Checks if email exists and updates.

        :param address:

        :return: Message that email does not exist or the email was updated.
        """
        if self.email != address:
            return self.email + " does not exist"
        else:
            self.email = address
            return "Email has been updated"

    def __repr__(self):
        """
        Displays an easy to read string of user, email and books read.

        :return: Formatted string.
        """
        return "User: " + self.name + ", email: " + self.email + ", books read: " + str(self.books)

    def __eq__(self, other):
        """
        Build in method to check for equality of user name and email address.

        :param other:

        :return: Comparison passes if True.
        """
        if self.name is other.name and self.email is other.email:
            return True
        elif type(self.name) != type(other.name) and type(self.email) != type(other.email):
            return False
        else:
            return self.name == other.name

    def read_book(self, book, rating=0):
        """
        Function to take in books that have been read by a user with rating.

        :param book:
        :param rating: Defaults to 0 is no rating is given

        :return: Books read, plus rating and stored in dictionary
        """
        results = self.books[book] = rating
        return results

    def get_average_rating(self):
        """
        Calculates the average of existing ratings.

        :return: Average of all ratings.
        """
        return sum(self.books.values()) / len(self.books.values())


class InvalidEmailError(Exception):
    """
    InvalidEmailError class.
    """
    pass


class Book(object):
    """
    Book class
    """
    def __init__(self, title, isbn):
        """
        The constructor for the book class.

        :param title:
        :param isbn:
        """
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __eq__(self, other):
        """
        Build in method to check for equality of isbn numbers.

        :param other:

        :return: Comparison passes if True
        """
        if self.isbn is other.isbn:
            return True
        elif type(self.isbn) != type(other.isbn):
            return False
        else:
            return self.isbn == other.isbn

    def get_title(self):
        """
        Get and return the title of a book.

        :return: Book title.
        """
        return self.title

    def get_isbn(self):
        """
        Get and return an isbn number.

        :return: Isbn number.
        """
        return self.isbn

    def set_isbn(self, new_isbn):
        """
        Sets a new isbn number on a book.

        :param new_isbn:

        :return: New isbn number.
        """
        self.isbn = new_isbn
        return self.isbn

    def add_rating(self, new_rating):
        """
        Checks for a valid rating between 0 - 4 and adds if valid.

        :param new_rating:

        :return: Message to user if rating is invalid, else thanks for the rating.
        """
        if 0 <= new_rating <= 4:
            self.ratings.append(new_rating)
            return "Thanks for New Rating " + str(self.ratings)
        else:
            return "Invalid Rating"

    def get_average_rating(self):
        """
        Completes a calculation to find the average of existing ratings.

        :return: The average of ratings.
        """
        return sum(self.ratings) / len(self.ratings)

    def __hash__(self):
        """
        Added to make a book hashable.

        :return: Return a consistent hash for a book object.
        """
        return hash((self.title, self.isbn))


class Fiction(Book):
    """
    Fiction subclass of Book class
    """
    def __init__(self, title, author, isbn):
        """
        Constructor of the Fiction class.

        :param title:
        :param author:
        :param isbn:
        """
        self.author = author
        super().__init__(title, isbn)

    def get_author(self):
        """
        Gets the author of a book existing in the fiction class.

        :return: Returns the author name.
        """
        return self.author

    def __repr__(self):
        """
        Prints out an easy to read string of book title and author.

        :return: Formatted string.
        """
        return "{} by {}".format(self.title, self.author)


class NonFiction(Book):
    """
    NonFiction subclass of the Book class.
    """
    def __init__(self, title, subject, level, isbn):
        """
        The constructor of the NonFiction class.

        :param title:
        :param subject:
        :param level:
        :param isbn:
        """
        self.subject = subject
        self.level = level
        super().__init__(title, isbn)

    def get_subject(self):
        """
        Gets the subject associated with a NonFiction book.

        :return: Subject of a NonFiction Book.
        """
        return self.subject

    def get_level(self):
        """
        The level associated with a NonFiction Book.

        :return: Level associated with nonfiction book
        """
        return self.level

    def __repr__(self):
        """
        Prints out an easy to read string of book title, level and subject.

        :return: Formatted string.
        """
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)


class TomeRater:
    """
    TomeRater Class
    """
    def __init__(self):
        """
        The constructor of the TomeRater class.
        """
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        """
        Creates/ adds a book to a dictionary.

        :param title:
        :param isbn:

        :return: Book with isbn.
        """
        result = self.books[title] = isbn
        return result

    def create_novel(self, title, author, isbn):
        """
        Creates/adds a novel(book) to a dictionary.

        :param title:
        :param author:
        :param isbn:

        :return: Returns novel: title, author and isbn.
        """
        result = self.books[title] = author, isbn
        return result

    def create_non_fiction(self, title, subject, level, isbn):
        """
        Creates/adds a nonfiction (book) to a dictionary.

        :param title:
        :param subject:
        :param level:
        :param isbn:

        :return: Returns nonfiction: title, subject, level and isbn.
        """
        result = self.books[title] = subject, level, isbn
        return result

    def add_book_to_user(self, book, email, rating=None):
        """
        Associates a book and rating with a user/email, increments number times the book has been read.

        :param book:
        :param email:
        :param rating:

        :return:
        """
        if hasattr(book, email) in User:
            User.read_book(book, rating)
            Book.add_rating(book, rating)
            book += 1
        else:
            print("No user with email {}".format(email))

    def add_user(self, name, email, user_books=None):
        """
        Associate user, email with books read.

        :param name:
        :param email:
        :param user_books:
        :return:
        """
        while self.add_book_to_user is not None:
            result = self.users[name] = email, user_books
            return result

    def print_catalog(self):
        """
        Gets all the books stored in the dictionary.

        :return: Prints the books.
        """
        catalog = self.books.keys
        print(catalog)

    def print_users(self):
        """
        Gets all the users in the dictionary.

        :return: Prints the users.
        """
        all_users = self.users.values
        print(all_users)

    def most_read_book(self):
        """
        Find the books that has been read the greatest number of times.

        :return: Book that has been read the most.
        """
        pass

    def highest_rated_book(self):
        """
        Find the book with the highest rating.

        :return: Book with the highest rating.
        """
        for i in self.books:
            return Book.get_average_rating(i)

    def get_n_most_read_books(self, n):
        """
        Sort the book items in the the dictionary.

        :param n:

        :return: Return the books in reversed order
        """
        result = sorted(dict.items(n), key=lambda kv: kv[1], reverse=True)
        return result

    def get_n_most_prolific_readers(self, n):
        """
        Find the users that have read the most books.

        :param n:

        :return: Return the users in reversed order.
        """
        result = sorted(dict.items(n), key=lambda kv: kv[1], reverse=True)
        return result

