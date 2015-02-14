from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # A person hear about a new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # The header metion to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Biy peapock feathers" into a text box

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on her list

        # The site has generated a unique URL for her --- there is
        # some explanatory text to that effect.

        # She visits that URL - her to-do list is still there

        # Satisfied, she leaves Earth and goes back to Mars.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
