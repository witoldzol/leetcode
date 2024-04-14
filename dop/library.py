from typing import List
###################################### DATA ##############################################################

class BookLendingData:
    pass

class BookItemData:
    book_lending_data: BookLendingData

class BookData:
    book_item_data: List[BookItemData]
    author_data: List["AuthorData"]

class AuthorData:
    book_data: List[BookData]

class CatalogData:
    book_data: List[BookData]

class LibrarianData:
    pass

class MemberData:
    book_lending_data: List[BookLendingData]

class UserData:
    pass

class LibraryData:
    librarian_data: List[LibrarianData]
    member_data: List[MemberData]
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


class Catalog:
    @staticmethod
    def get_book_lendings(catalog_data: CatalogData, user_id: str):
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

class BookItem:
    pass
