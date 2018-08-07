import pytest

from getv.main import GetVersion


@pytest.fixture
def get_v():
    get_v = GetVersion()
    return get_v
