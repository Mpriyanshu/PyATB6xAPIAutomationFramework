import pytest
import allure
import requests
from src.modules.wrapper.api_requests_wrapper import put_request
from src.endpoints.api_constants import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import create_token, put_payload
from src.modules.verifications.common_verification import *

class TestUpdateBooking:

    @pytest.mark.positive
    @allure.title("Update Booking")
    @allure.description("Update Booking for particular booking id")
    def test_verify_update_booking_TC1(self):
        response = put_request(
            url=APIConstants().get_booking_ID(booking_ID=2),
            auth=create_token(),
            headers=Utils().common_headers_put_patch_delete_cookie_auth(token=create_token()),
            payload= put_payload(),
            in_json= False
        )
        # verify_status_code(response_status_code=response,expected_code=200)
        print(response)