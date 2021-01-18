from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):
	
	def test_can_start_a_list_for_one_user(self):
		#Somone is comming new to the homepage
		self.browser.get(self.live_server_url)
		# Nutzerin sieht page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# posebilaty to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)

		# User Input
		inputbox.send_keys('Buy peacock feathers')

		# USER hits enter, the page updates, and now the page lists
		#'1: ...'
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy peacock feathers')

		# User can add another item
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		#time.sleep(1)

		
		self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
		self.wait_for_row_in_list_table('1: Buy peacock feathers')

	def test_multiple_users_can_start_lists_at_different_urls(self):
		# user 1
		self.browser.get(self.live_server_url)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy peacock feathers')

		user_1_url = self.browser.current_url
		self.assertRegex(user_1_url, '/lists/.+')

		# user 1 log out and a new user comes to the site
		self.browser.quit()
		self.browser = webdriver.Firefox()

		# user 2 can't see user 1 list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		# user 2 create add item to list
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('gibt es hier Bilder?')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: gibt es hier Bilder?')

		user_2_url = self.browser.current_url
		self.assertRegex(user_2_url, '/lists/.+')
		self.assertNotEqual(user_1_url, user_2_url)
		page_text = self.browser.find_element_by_tag_name('body').text

		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('gibt es hier Bilder?', page_text)

		# both users go to sleep
		self.fail('Finish the test!')

