"""
THESE ARE MY TESTS FOR PROJECT_4

"""

import unittest, sqlite3
from Project_4 import ask_user_for_time,\
    main_menu,\
    ask_user_for_name_task_notes,\
    lookup_menu,\
    lookup,\
    make_edit_question

from unittest.mock import patch


class Lookuptest(unittest.TestCase):

    def test_ask_user_for_time(self):
        """
        HERE I TEST THE INPUT OF FUNCTION ASK_USER_FOR_TIME.

        """
        #create some fake data
        user_input = ['5', "ignore"]

        # Override input function. send fake data to input as side_effect
        with patch('builtins.input', side_effect = user_input):

            # run the function, fake collects the fake data
            fake = ask_user_for_time()

            # Test the fake data
            self.assertEqual(fake, 5)

    # def test_ask_user_for_time_error(self):
    #
    #     #create some fake data
    #     user_input = ['t', "4"]
    #
    #     # Override input function. send fake data to input as side_effect
    #     with patch('builtins.input', side_effect = user_input):
    #
    #         # run the function, fake collects the fake data
    #         fake = ask_user_for_time()
    #
    #         # Test the fake data
    #         self.assertRaises(ValueError, fake)

    def test_ask_user_for_name_task_notes(self):
        """
        HERE I TEST THE INPUT OF FUNCTION ASK_USER_FOR_NAME_TASK_NOTES.

        """

        user_input = ["john", "make test", "here are some notes"]

        with patch("builtins.input", side_effect = user_input):

            fake = ask_user_for_name_task_notes()

            self.assertEqual(fake, ("john", "make test", "here are some notes"))




    def test_main_input(self):
        """
        HERE I TEST THE INPUT OF FUNCTION MAIN_MENU.

        """
        user_input = ["a", "b"]

        with patch("builtins.input", side_effect = user_input):

            fake = main_menu()

            self.assertEqual(fake, "a")



    def test_main_input_lower(self):
        """
        HERE I TEST THE INPUT OF FUNCTION MAIN_MENU FOR LOWERCASE.

        """
        user_input = ["A", "b"]

        with patch("builtins.input", side_effect = user_input):

            fake = main_menu()

            self.assertEqual(fake, "a")



    def test_lookup_menu_a(self):
        """
        HERE I TEST THE INPUT OF FUNCTION LOOKUP_MENU

        """
        user_input = ["a", "ignore"]

        with patch("builtins.input", side_effect = user_input):

            fake = lookup_menu()

            self.assertEqual(fake, "a")

    def test_lookup_menu_lower(self):
        """
        HERE I TEST THE INPUT OF FUNCTION LOOKUP_MENU FOR LOWERCASE.

        """
        user_input = ["A", "ignore"]

        with patch("builtins.input", side_effect = user_input):
            fake = lookup_menu()

            self.assertEqual(fake, "a")


    def test_lookup_a(self):
        """
        HERE I TEST THE INPUT OF FUNCTION LOOKUP, IF ELIF CONDITIONS.

        """
        user_input = ["a", "jack", "n", "n", "c"]


        with patch("builtins.input", side_effect = user_input):

            fake = lookup()

            self.assertEqual(fake, "a")

    def test_lookup_b(self):
        """
        HERE I TEST THE INPUT OF FUNCTION LOOKUP, IF ELIF CONDITIONS.

        """
        user_input = ["b", "b", "c", "d", "e"]

        with patch("builtins.input", side_effect = user_input):

            fake = lookup()

            self.assertEqual(fake, "b")

    def test_lookup_c(self):
        """
        HERE I TEST THE INPUT OF FUNCTION LOOKUP, IF ELIF CONDITIONS.

        """
        user_input = ["c", "b", "c", "d", "e"]

        with patch("builtins.input", side_effect = user_input):

            fake = lookup()

            self.assertEqual(fake, "c")

    def test_lookup_d(self):
        """
        HERE I TEST THE INPUT OF FUNCTION LOOKUP, IF ELIF CONDITIONS.

        """
        user_input = ["b", "20-11-2018", "n","n", "c"]

        with patch("builtins.input", side_effect = user_input):

            fake = lookup()

            self.assertEqual(fake, "b")


    # def test_lookup_e(self):
    #     user_input = ["e", "c"]
    #
    #     with patch("builtins.input", side_effect = user_input):
    #
    #         fake = lookup()
    #
    #         self.assertEqual(fake, "c")



    def test_make_edit_question(self):
        """
        HERE I TEST THE INPUT OF FUNCTION MAKE_EDIT

        """
        user_input = ["a", "b", "c"]

        with patch("builtins.input", side_effect = user_input):

            fake = make_edit_question()

            self.assertEqual(fake,"a")

    def test_make_edit_question_lower(self):
        """
        HERE I TEST THE INPUT OF FUNCTION MAKE_EDIT LOWERCASE

        """
        user_input = ["A", "b", "c"]

        with patch("builtins.input", side_effect = user_input):

            fake = make_edit_question()

            self.assertEqual(fake,"a")

if __name__ == '__main__':
    unittest.main()

