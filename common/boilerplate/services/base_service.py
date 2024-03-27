import typing as _

from common.helpers.constants import StatusCodes

T = _.TypeVar("T")


class BaseService:
    def ok(self, data: T, status_code: _.Optional[int] = StatusCodes().SUCCESS):
        return {"response_data": data, "code": status_code}

    def exception(self, errors: T, status_code: int):
        return {"errors": errors, "code": status_code}
