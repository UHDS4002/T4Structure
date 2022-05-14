from typing import List


class Book:
    def __init__(self,
                 name: str,
                 writer: str,
                 info: str,
                 priority: int = 20,
                 count: int = 1):
        pass

    def add(self, amount: int = 1):
        pass

    def rent(self, amount: int = 1):
        pass

    def timeout(self) -> int:
        # int( (priority * 14 ) / 100)
        pass

    def penalty(self) -> int:
        # int( (priority * 1000) / 100) + 1000
        pass


class Customer:
    def __init__(self,
                 name: str,
                 username: str,
                 password: str,
                 contact: str):
        pass


class Rent:
    def __init__(self, book: Book, customer: Customer):
        pass


class Request:
    def __init__(self, book: Book, customer: Customer, code: int):
        pass


class Core:
    def __init__(self):
        pass

    def add_book(self, name: str, writer: str, info: str, priority: int = 20) -> Book:
        pass

    def find_book(self, query: str) -> List[Book]:
        # returns 20 Books in an Array or less if not found
        # page number from 1 to n may be passed as query
        pass

    def edit_book(self):
        # you can do this in view part or change the method signature
        pass

    def request_book(self, customer: Customer, book: Book) -> int:
        # returns request code which is used when delivering book
        pass

    def requested_books(self) -> List[Book]:
        # returns all requested books in an Array
        pass

    def deliver_book(self, request_code: int) -> Rent:
        # confirm that customer took the requested book from employee
        pass

    def add_customer(self, name: str, username: str, password: str, contact: str) -> Customer:
        # also check for duplicate usernames and assign an id
        pass

    def edit_customer(self):
        # just like edit book
        pass

    def find_customer(self, query: str) -> List[Customer]:
        # query can be username or page number, returns an Array of found customer
        # this method is also used for login, check if first found object has exact entered username
        pass

    def today_deliveries(self) -> List[Rent]:
        # returns all books which are waiting for delivery today,
        pass

    def confirm_delivery(self, rent: Rent):
        # confirms that a rented book is delivered now
        # removes the rent from lists and adds one to books amount
        pass

    def expired_deliveries(self) -> List[Rent]:
        # sorted by penalty amount
        pass
