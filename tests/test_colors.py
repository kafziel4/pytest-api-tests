from assertpy import assert_that

from helpers.colors import COLORS
from helpers.constants import CONTENT_TYPE, APPLICATION_JSON, IGNORED


def test_get_colors_should_return_200_and_list_of_colors(reqres_client):
    # Arrange
    expected_response = COLORS

    # Act
    response = reqres_client.get_colors()

    # Assert
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.headers[CONTENT_TYPE]).is_equal_to(APPLICATION_JSON)

    content = response.json()
    assert_that(content).is_equal_to(expected_response, ignore=IGNORED)


def test_get_color_for_existing_color_should_return_200_and_color_data(reqres_client):
    # Arrange
    expected_color = {
        "id": 2,
        "name": "fuchsia rose",
        "year": 2001,
        "color": "#C74375",
        "pantone_value": "17-2031",
    }

    # Act
    response = reqres_client.get_single_color(expected_color["id"])

    # Assert
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.headers[CONTENT_TYPE]).is_equal_to(APPLICATION_JSON)

    content = response.json()
    assert_that(content["data"]).is_equal_to(expected_color)


def test_get_color_for_nonexistent_color_should_return_404(reqres_client):
    # Arrange
    nonexistent_id = 23

    # Act
    response = reqres_client.get_single_color(nonexistent_id)

    # Assert
    assert_that(response.status_code).is_equal_to(404)
    assert_that(response.headers[CONTENT_TYPE]).is_equal_to(APPLICATION_JSON)

    content = response.json()
    assert_that(content).is_empty()
