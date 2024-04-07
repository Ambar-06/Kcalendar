from common.boilerplate.api.base_api_view import BaseAPIView
from common.boilerplate.decorators.validate_request import validate_request
from user.serializers.auth_serializers import GenerateAuthTokenSerializer
from user.services.auth_services import GenerateAuthTokenService


class GenerateAuthTokenViews(BaseAPIView):
    def __init__(self):
        self.service = GenerateAuthTokenService()

    @validate_request(GenerateAuthTokenSerializer)
    def get(self, request, data):
        service_data = self.service.get_service(request, data)
        response = service_data.get("response_data")
        status_code = service_data.get("code")
        return self.success(response, status_code)