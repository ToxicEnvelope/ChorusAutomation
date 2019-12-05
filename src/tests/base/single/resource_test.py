import unittest
from src.tests.base.base_test import BaseTest
from src.core.pageobjects.login_page import LoginPage
from src.core.pageobjects.meeting_page import MeetingPage


class PageResourceTest(BaseTest, unittest.TestCase):
    class Fixture:
        credentils = ('yahav.hoffmann@chorus-auto.com', '{RkVC4mPU6S**axv')
        _not = '0:00 / 1:15'
        _fifth = '0:05 / 1:15'
        _fifthteenth = '0:15 / 1:15'
        _thirtieth = '0:30 / 1:15'
    fixture = Fixture()
    
    def test_duration_text_calidation(self):
        lp = LoginPage(self.driver)
        lp.makeLogin(self.fixture.credentils)

        mp = MeetingPage(self.driver)
        mp.click_play()
        mp.wait(5)
        first_dur = mp.get_durations()
        self.assertEqual(first_dur, self.fixture._fifth)

        mp.jump15Forward()
        mp.wait(10)
        second_dur = mp.get_durations()
        self.assertEqual(second_dur, self.fixture._thirtieth)

        mp.jump15Backwards()
        third_dur = mp.get_durations()
        self.assertEqual(third_dur, self.fixture._fifthteenth)

    def test_duration_text_boundaries_validation(self):
        lp = LoginPage(self.driver)
        lp.makeLogin(self.fixture.credentils)

        mp = MeetingPage(self.driver)
        mp.click_play()
        mp.wait(5)
        first_dur = mp.get_durations()
        self.assertEqual(first_dur, self.fixture._fifth)

        mp.jump15Backwards()
        first_dur = mp.get_durations()
        self.assertEqual(first_dur, self.fixture._not)
        elem = mp.to_webelement(mp.PLAY_BTN)
        self.assertTrue(elem.is_displayed())

if __name__ == "__main__":
    unittest.main()
