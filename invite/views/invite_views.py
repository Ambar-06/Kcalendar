from common.boilerplate.api.base_api_view import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from invite.serializers.invitation_serializers import InvitationFilterSerializer, InviteViewSerializer
from invite.services.invite_services import InviteService


class InviteViews(BaseAPIView):
    def __init__(self):
        self.service = InviteService()

    @validate_request(InvitationFilterSerializer)
    @auth_guard()
    def post(self, request, data, *args):
        service_data = self.service.post_service(request, data)
        response = service_data.get("response_data")
        status_code = service_data.get("code")
        return self.success(InviteViewSerializer(response).data, status_code)