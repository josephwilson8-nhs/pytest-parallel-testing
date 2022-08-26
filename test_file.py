'''
Testing suite with tests which take 5 seconds to complete
'''
import pytest
from time import sleep

sleep_times = [5] * 12

@pytest.mark.parametrize('sleep_time', sleep_times)
def test_sleep(sleep_time):
    '''
    Sleep then pass
    '''
    sleep(sleep_time)
    assert True
