from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		#needs to be written.
		self.fail('write me')
		

if __name__ == '__main__':
	unittest.main()