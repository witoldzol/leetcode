from typing import List

class CatalogData:
    pass

class LibrarianData:
    pass

class MemberData:
    pass

class LibraryData:
    librarian_data: List[LibrarianData]
    member_data: List[MemberData]
    catalog_data: CatalogData
