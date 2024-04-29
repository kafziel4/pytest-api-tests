from assertpy import assert_that

from helpers.constants import CONTENT_TYPE, APPLICATION_JSON, MISSING_PASSWORD


def test_post_login_with_valid_data_should_return_200_and_login_token(reqres_client):
    # Arrange
    request_body = {
        "email": "eve.holt@reqres.in",
        "password": "pistol",
    }

    expected_response = {
        "token": "QpwL5tke4Pnpja7X4",
    }

    # Act
    response = reqres_client.post_login(request_body)

    # Assert
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.headers[CONTENT_TYPE]).is_equal_to(APPLICATION_JSON)

    content = response.json()
    assert_that(content).is_equal_to(expected_response)


def test_post_login_with_missing_password_should_return_400_and_validation_error(reqres_client):
    # Arrange
    request_body = {
        "email": "peter@klaven",
    }

    expected_response = {
        "error": MISSING_PASSWORD,
    }

    # Act
    response = reqres_client.post_login(request_body)

    # Assert
    assert_that(response.status_code).is_equal_to(400)
    assert_that(response.headers[CONTENT_TYPE]).is_equal_to(APPLICATION_JSON)

    content = response.json()
    assert_that(content).is_equal_to(expected_response)
