import pytest
from jabbapylib.process.timeout import Timeout
from jabbapylib.process.timeout import test_request

def test_timeout():
    with Timeout(3):
        test_request("OK")
    with Timeout(1):
        with pytest.raises(Timeout.Timeout):
            test_request("timeout occurs")