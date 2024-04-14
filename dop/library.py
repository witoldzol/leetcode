from typing import List, Dict
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
    authors: List[str]

class Author:
    books: List[str]

class LibrarianData:
    email: str
    password: str

class MemberData:
    email: str
    password: str
    book_lending_data: List[BookLendingData]

class CatalogData:
    books_by_isbn: Dict[str, Book]
    authors_by_id: Dict[str, Author]

class UserManagementData:
    librarians_by_email: Dict[str, LibrarianData]
    members_by_email: Dict[str, MemberData]

class LibraryData:
    name: str
    address: str
    catalog_data: CatalogData
    user_management_data: UserManagementData

###################################### CODE ##############################################################

class UserManagement:
    @staticmethod
    def is_librarian(user_data: UserManagementData, user_id: str):
        pass

    @staticmethod
    def is_super_member(user_data: UserManagementData, user_id: str):
        pass

    @staticmethod
    def is_vip_member(user_data: UserManagementData, user_id: str):
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
        if UserManagement.is_librarian(library_data.user_management_data, user_id) or \
           UserManagement.is_super_member(library_data.user_management_data, user_id):
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
        if UserManagement.is_librarian(library_data.user_management_data, user_id) or \
           UserManagement.is_super_member(library_data.user_management_data, user_id):
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
