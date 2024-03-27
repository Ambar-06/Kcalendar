from rest_framework import pagination
from rest_framework.response import Response

"""
This class is used for custom pagination
This class is inherited from PageNumberPagination
Fields:
Methods:
    get_next_link: This method is used to get the next link
    get_previous_link: This method is used to get the previous link
    get_paginated_response: This method is used to get the paginated response
"""


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "perPage"
    max_page_size = 100

    def get_next_link(self):
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()
        return page_number

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()
        return page_number

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )
