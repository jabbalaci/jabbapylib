from jabbapylib.web.scraper import scraper

def test_sleep():
    sleep_time = scraper.sleep(fix=5, plus=5, test=True)
    assert 5.0 <= sleep_time <= 10.0