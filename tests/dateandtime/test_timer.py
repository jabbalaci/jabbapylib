import time
from jabbapylib.dateandtime.timer import Timer

class TestTimer:
    
    def test_timer(self):
        timer = Timer()
        with timer:
            # Whatever you want to measure goes here
            time.sleep(0.1)
        
        assert 0.1 < timer.elapsed_time() < 0.2