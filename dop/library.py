from typing import List

class BookLendingData:
    pass

class CatalogData:
    pass

class LibrarianData:
    pass

class MemberData:
    book_lending_data: List[BookLendingData]

class LibraryData:
    librarian_data: List[LibrarianData]
    member_data: List[MemberData]
    catalog_data: CatalogData
