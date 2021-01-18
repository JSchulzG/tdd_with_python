from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class LayoutAndStylingTest(FunctionalTest):
		def test_layout_and_styling(self):
		# user goes to webpage
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024,768)
		# and notices the input is nice
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width']/2,
			512,
			delta=10
		)

