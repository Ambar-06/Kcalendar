from common.boilerplate.api.base_api_view import BaseAPIView
from common.boilerplate.decorators.validate_request import validate_request
from user.serializers.register_serializers import RegistrationSerializer, UserViewSerializer
from user.services.register_services import RegisterService


class RegisterViews(BaseAPIView):
    def __init__(self):
        self.service = RegisterService()


    @validate_request(RegistrationSerializer)
    def post(self, request, data):
        service_data = self.service.post_service(request, data)
        response = service_data.get("response_data")
        status_code = service_data.get("code")
        return self.success(UserViewSerializer(response).data, status_code)
