import allure
import pytest

from src.modules.wrapper.api_requests_wrapper import post_request, put_requests, delete_requests
from src.endpoints.api_constansts import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import payload_update_booking
from src.modules.verfication.common_verification import *



# FLOW of the E2E
# Create a token
# Create a booking ID.
# We need to update the booking ID. With token
# We are going to delete the booking ID.
# We are going to verify that booking ID does not exist after delete.

# confest


class TestCRUDBooking(object):

    @allure.title("Test CRUD operation Update(PUT).")
    @allure.description(
        "Verify that Full Update with the booking ID and Token is working.")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        put_url = APIConstants().url_patch_put_delete(booking_id=get_booking_id)
        print(put_url)
        print(create_token)
        response = put_requests(
            url=put_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=create_token),
            payload=payload_update_booking(),
            auth=None,
            in_json=False

        )
        # Verify
        verify_http_status_code(response_data_status=response.status_code, expected_data=200)
        verify_response_key(response.json()["firstname"], expected_data="Amit")
        verify_response_key(response.json()["lastname"], expected_data="Brown")

    def test_delete_booking_id(self, create_token, get_booking_id):
        delete_url = APIConstants().url_patch_put_delete(booking_id=get_booking_id)
        response = delete_requests(
            url=delete_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=create_token),
            auth=None,
            in_json=False
        )
        verify_response_delete(response=response.text)
        verify_http_status_code(response_data_status=response.status_code, expected_data=201)

