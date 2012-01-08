import re
from datetime import datetime 
from jabbapylib.dateandtime import dateandtime as dat

class TestDateAndTime:
    
    def setup_method(self, method):
        self.ts = 1111111111
        self.dt = datetime.fromtimestamp(self.ts)
        
    ##########
    
    def test_get_timestamp_from_year_to_second_01(self): 
        res = dat.get_timestamp_from_year_to_second()
        assert re.search('^\d{8}_\d{6}$', res)
        
    def test_get_timestamp_from_year_to_second_02(self): 
        res = dat.get_timestamp_from_year_to_second(separator=True)
        assert re.search('^\d{4}_\d\d_\d\d_\d{6}$', res)
        
    def test_get_timestamp_from_year_to_second_03(self): 
        res = dat.get_timestamp_from_year_to_second(date=self.dt)
        assert res == '20050318_025831'
        
    def test_get_timestamp_from_year_to_second_04(self):
        res = dat.get_timestamp_from_year_to_second(separator=True, date=self.dt)
        assert res == '2005_03_18_025831'
        
    ##########
    
    def test_get_date_from_year_to_day(self):
        res = dat.get_date_from_year_to_day()
        assert re.search('^\d{4}_\d\d_\d\d$', res)
        
    ##########
    
    def test_datetime_to_unix_timestamp(self):
        res = dat.datetime_to_unix_timestamp(self.dt)
        assert res == 1111111111
        
    ##########
    
    def test_unix_timestamp_to_datetime(self):
        res = dat.unix_timestamp_to_datetime(self.ts)
        assert res.__str__() == '2005-03-18 02:58:31'
