from typing import List
###################################### DATA ##############################################################

class BookLendingData:
    pass

class BookItem:
    book_lending_data: BookLendingData

class Book:
    title: str
    publication_year: str
    ISBN: str
    publisher: str
    book_item_data: List[BookItem]
    author_data: List["Author"]

class Author:
    books: List[Book]

class CatalogData:
    books: List[Book]

class LibrarianData:
    pass

class MemberData:
    book_lending_data: List[BookLendingData]

class UserData:
    librarians: List[LibrarianData]
    members: List[MemberData]

class LibraryData:
    name: str
    address: str
    catalog_data: CatalogData
    user_data: UserData

###################################### CODE ##############################################################

class UserManagement:
    @staticmethod
    def is_librarian(user_data: UserData, user_id: str):
        pass

    @staticmethod
    def is_super_member(user_data: UserData, user_id: str):
        pass

    @staticmethod
    def is_vip_member(user_data: UserData, user_id: str):
        pass

class Catalog:
    @staticmethod
    def get_book_lendings(catalog_data: CatalogData, user_id: str):
        pass

    @staticmethod
    def add_book_item(catalog_data: CatalogData, book_item_info: BookItemInfo):
        pass

class Library:
    @staticmethod
    def get_book_lendings(library_data: LibraryData, user_id: str, member_id: str):
        if UserManagement.is_librarian(library_data.user_data, user_id) or \
           UserManagement.is_super_member(library_data.user_data, user_id):
            return Catalog.get_book_lendings(library_data.catalog_data, member_id)
        else:
            raise Exception("Not allowed to get book lendings")

    @staticmethod
    def search_book(library_data: LibraryData, search_query: str):
        pass

    @staticmethod
    def add_book_item(library_data: LibraryData,
                      user_id: str,
                      book_item_info: BookItemInfo):
        if UserManagement.is_librarian(library_data.user_data, user_id) or \
           UserManagement.is_super_member(library_data.user_data, user_id):
            Catalog.add_book_item(library_data.catalog_data, book_item_info)

# OTHER STUFF
class CatalogCode:
    pass

class MemberCode:
    pass

class BookLendingCode:
    pass

class BookItemCode:
    pass

class UserCode:
    pass
