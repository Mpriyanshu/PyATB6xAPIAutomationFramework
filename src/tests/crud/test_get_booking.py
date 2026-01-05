import allure
import pytest
from src.modules.wrapper.api_requests_wrapper import get_booking_request2
from src.endpoints.api_constansts import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import post_payload, create_token
from src.modules.verfication.common_verification import *

class TestGETBooking:

    @pytest.mark.positive
    @allure.title("Verify that the existing booking, which is booking number 1, exists and it gave you status code 200.")
    @allure.description("Valid Booking Id")
    def test_verify_existing_booking_bid_01(self):
        response = get_booking_request2(
            url = APIConstants().get_booking_ID(2),
        )
        verify_status_code(response_ststus_code=response,expected_code=200)
        print(response)

    @pytest.mark.negative
    @allure.title("Negative Value of booking Id")
    @allure.description("Verify that the booking ID does not exist and it will give you an error.")
    def test_verify_invalid_booking_not_exist(self):
        response = get_booking_request2(
            url=APIConstants().get_booking_ID(-2),
        )
        verify_status_code(response_status_code=response, expected_code=404)
        print(response)

    @pytest.mark.negative
    @allure.title("Negative Value of booking Id2")
    @allure.description("Verify that the booking ID does not exist and it will give you an error.")
    def test_verify_invalid_booking_not_exist2(self):
        response = get_booking_request2(
            url=APIConstants().get_booking_ID("test"),
        )
        verify_status_code(response_status_code=response, expected_code=404)
        print(response)