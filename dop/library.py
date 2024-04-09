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

class LibraryData:
    librarian_data: List[LibrarianData]
    member_data: List[MemberData]
    catalog_data: CatalogData

###################################### CODE ##############################################################
