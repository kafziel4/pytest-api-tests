from assertpy import assert_that, soft_assertions

from helpers.constants import (
    CONTENT_TYPE,
    APPLICATION_JSON,
    IGNORED,
    ONE_TO_THREE_DIGITS,
    DATE_IN_ISO_FORMAT,
    CONTENT_LENGTH
)
from helpers.users import USERS


def test_get_users_should_return_200_and_list_of_users(reqres_client):
    # Arrange
    page = 2
    expected_response = USERS

    # Act
    response = reqres_client.get_users(page)

    # Assert
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.headers[CONTENT_TYPE]).is_equal_to(APPLICATION_JSON)

    content = response.json()
    assert_that(content).is_equal_to(expected_response, ignore=IGNORED)


def test_get_user_for_existing_user_should_return_200_and_user_data(reqres_client):
    # Arrange
    expected_user = {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg",
    }

    # Act
    response = reqres_client.get_single_user(expected_user["id"])

    # Assert
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.headers[CONTENT_TYPE]).is_equal_to(APPLICATION_JSON)

    content = response.json()
    assert_that(content["data"]).is_equal_to(expected_user)


def test_get_user_for_nonexistent_user_should_return_404(reqres_client):
    # Arrange
    nonexistent_id = 23

    # Act
    response = reqres_client.get_single_user(nonexistent_id)

    # Assert
    assert_that(response.status_code).is_equal_to(404)
    assert_that(response.headers[CONTENT_TYPE]).is_equal_to(APPLICATION_JSON)

    content = response.json()
    assert_that(content).is_empty()


def test_post_user_with_valid_data_should_return_201_and_user_data(reqres_client):
    # Arrange
    request_body = {
        "name": "morpheus",
        "job": "leader",
    }

    # Act
    response = reqres_client.post_user(request_body)

    # Assert
    assert_that(response.status_code).is_equal_to(201)
    assert_that(response.headers[CONTENT_TYPE]).is_equal_to(APPLICATION_JSON)

    with soft_assertions():
        content = response.json()
        assert_that(request_body).is_subset_of(content)
        assert_that(content["id"]).matches(ONE_TO_THREE_DIGITS)
        assert_that(content["createdAt"]).matches(DATE_IN_ISO_FORMAT)


def test_put_user_for_existing_user_with_valid_data_should_return_200_and_user_data(reqres_client):
    # Arrange
    user_id = 2
    request_body = {
        "name": "morpheus",
        "job": "zion resident",
    }

    # Act
    response = reqres_client.put_user(user_id, request_body)

    # Assert
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.headers[CONTENT_TYPE]).is_equal_to(APPLICATION_JSON)

    with soft_assertions():
        content = response.json()
        assert_that(request_body).is_subset_of(content)
        assert_that(content["updatedAt"]).matches(DATE_IN_ISO_FORMAT)


def test_patch_user_for_existing_user_with_valid_data_should_return_200_and_user_data(reqres_client):
    # Arrange
    user_id = 2
    request_body = {
        "name": "morpheus",
        "job": "zion resident",
    }

    # Act
    response = reqres_client.patch_user(user_id, request_body)

    # Assert
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.headers[CONTENT_TYPE]).is_equal_to(APPLICATION_JSON)

    with soft_assertions():
        content = response.json()
        assert_that(request_body).is_subset_of(content)
        assert_that(content["updatedAt"]).matches(DATE_IN_ISO_FORMAT)


def test_delete_user_for_existing_user_should_return_204(reqres_client):
    # Arrange
    user_id = 2

    # Act
    response = reqres_client.delete_user(user_id)

    # Assert
    assert_that(response.status_code).is_equal_to(204)
    assert_that(response.headers[CONTENT_LENGTH]).is_equal_to("0")
