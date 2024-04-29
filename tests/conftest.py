import pytest

from clients.reqres_client import ReqResClient


@pytest.fixture
def reqres_client():
    return ReqResClient()
