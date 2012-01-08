import time
from jabbapylib.dateandtime.timer import Timer

class TestTimer:
    
    def test_timer(self):
        timer = Timer()
        print '# testing timer, takes 1 sec.'
        with timer:
            # Whatever you want to measure goes here
            time.sleep(1)
        
        assert 1.0 < timer.elapsed_time() < 1.1