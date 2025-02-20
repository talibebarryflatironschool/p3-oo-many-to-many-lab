# class Author:
#     pass


# class Book:
#     pass


# class Contract:
#     pass



class Author:
    # Class variable to track all Author instances.
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Author name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return a list of all contracts where this author is involved."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return a list of books associated with this author via contracts."""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """
        Create a new Contract linking this author and a book.
        Returns the new Contract object.
        """
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Calculate the total royalties earned from all contracts."""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    # Class variable to track all Book instances.
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Book title must be a string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return a list of all contracts associated with this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return a list of all authors for this book via contracts."""
        return [contract.author for contract in self.contracts()]


class Contract:
    # Class variable to track all Contract instances.
    all = []

    def __init__(self, author, book, date, royalties):
        # Validate that the author and book are proper instances.
        if not isinstance(author, Author):
            raise Exception("Contract author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("Contract book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("Contract date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Contract royalties must be an int")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """
        Return all contracts that have the specified date.
        """
        return [contract for contract in cls.all if contract.date == date]
