import typing as _
from rest_framework.response import Response
from rest_framework import generics

from common.helpers.constants import StatusCodes

T = _.TypeVar("T")

"""
This class is used for base paginated api view
This class is inherited from ListAPIView
Fields:
Methods:
    success: This method is used to return success response
    error: This method is used to return error response
    success_paginated: This method is used to return paginated success response
    success_not_paginated: This method is used to return not paginated success response
"""


class PaginatedBaseApiView(generics.ListAPIView):
    def __init__(self, serializer_class, pagination_class) -> None:
        super().__init__(
            serializer_class=serializer_class,
            pagination_class=pagination_class,
        )

    def success(self, data: T, code=StatusCodes().SUCCESS) -> Response:
        return Response(
            {
                "success": True,
                "code": code,
                "data": data,
            },
            status=code,
        )

    def success_paginated(self, page=1, perPage=10) -> Response:
        queryset = self.get_queryset()
        values = self.paginate_queryset(queryset)
        if "context" in self.__dict__:
            context_data = self.context
        else:
            context_data = {}
        serializer = self.get_serializer_class()(
            values, many=True, context=context_data
        )
        response = self.get_paginated_response(serializer.data)

        response.data = {
            "success": True,
            "code": StatusCodes().SUCCESS,
            "data": response.data.get("results", []),
            "meta": {
                "pagination": {
                    "count": response.data.get("count", 0),
                    "page": page,
                    "perPage": perPage,
                    "totalPages": response.data.get("total_pages", 0),
                }
            },
        }
        return response

    def error(self, errors, status_code: int) -> Response:
        return Response(
            {"success": False, "code": status_code, "errors": errors},
            status=status_code,
        )

    def success_not_paginated(self) -> Response:
        queryset = self.get_queryset()
        values = queryset
        if "context" in self.__dict__:
            context_data = self.context
        else:
            context_data = {}
        serializer = self.get_serializer_class()(
            values, many=True, context=context_data
        )
        response = serializer.data
        return Response(
            {
                "data": response,
            }
        )
