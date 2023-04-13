import unittest
from src.task import Task
from src.task_decider import *

class TestTaskDecider(unittest.TestCase):
    def setUp(self):
        self.task_1 = Task("Wash Dishes", 30)
        self.task_2 = Task("Cook Dinner", 60)
        self.task_3 = Task("Clean Windows", 45)
        self.task_4 = Task("Do Ironing", 15)
        self.task_5 = Task("Wash Clothes", 120)
        self.task_all_preferences = {
            self.task_1.description : [
                self.task_2.description,
                self.task_5.description
            ],
            self.task_2.description : [
                self.task_4.description, 
                self.task_3.description
            ],
            self.task_3.description : [
                self.task_1.description,
                self.task_4.description
            ],
            self.task_4.description : [
                self.task_1.description,
                self.task_5.description
            ],
            self.task_5.description : [
                self.task_3.description,
                self.task_2.description
            ]
        }



        
    def test_preferences(self):
        self.assertEqual("first: Clean Windows, second: Wash Dishes",
                          get_preferred_option(self.task_1,self.task_3))
        
    def test_extensions_preferences_1(self):

        self.assertEqual("Wash Dishes is preferred over Wash Clothes",
                         get_preferred_options_extension(self.task_1,self.task_5,self.task_all_preferences ) )
        
    def test_extensions_preferences_1_Rev(self):

        self.assertEqual("Wash Dishes is preferred over Wash Clothes",
                         get_preferred_options_extension(self.task_5,self.task_1,self.task_all_preferences ) )

    def test_extensions_preferences_2(self):

        self.assertEqual("Cook Dinner is preferred over Do Ironing",
                         get_preferred_options_extension(self.task_2,self.task_4,self.task_all_preferences ) )
        
    def test_extensions_preferences_2_Rev(self):

        self.assertEqual("Cook Dinner is preferred over Do Ironing",
                         get_preferred_options_extension(self.task_4,self.task_2,self.task_all_preferences ) )


    def test_extensions_preferences_3(self):

        self.assertEqual("Clean Windows is preferred over Do Ironing",
                         get_preferred_options_extension(self.task_3,self.task_4,self.task_all_preferences ) )

    def test_extensions_preferences_3_Rev(self):

        self.assertEqual("Clean Windows is preferred over Do Ironing",
                         get_preferred_options_extension(self.task_4,self.task_3,self.task_all_preferences ) )
        
    def test_extensions_preferences_4(self):

        self.assertEqual("Do Ironing is preferred over Wash Clothes",
                         get_preferred_options_extension(self.task_5,self.task_4,self.task_all_preferences ) )
        
    def test_extensions_preferences_4_Rev(self):

        self.assertEqual("Do Ironing is preferred over Wash Clothes",
                         get_preferred_options_extension(self.task_4,self.task_5,self.task_all_preferences ) )

    def test_extensions_preferences_5(self):

        self.assertEqual("Do Ironing is preferred over Wash Dishes",
                         get_preferred_options_extension(self.task_1,self.task_4,self.task_all_preferences ) )
        
    def test_extensions_preferences_5_Rev(self):

        self.assertEqual("Do Ironing is preferred over Wash Dishes",
                         get_preferred_options_extension(self.task_4,self.task_1,self.task_all_preferences ) )

    def test_extensions_preferences_6(self):

        self.assertEqual("Wash Clothes is preferred over Cook Dinner",
                         get_preferred_options_extension(self.task_2,self.task_5,self.task_all_preferences ) )
        
    def test_extensions_preferences_6_Rev(self):

        self.assertEqual("Wash Clothes is preferred over Cook Dinner",
                         get_preferred_options_extension(self.task_5,self.task_2,self.task_all_preferences ) )

    def test_extensions_preferences_7(self):

        self.assertEqual("Wash Clothes is preferred over Clean Windows",
                         get_preferred_options_extension(self.task_3,self.task_5,self.task_all_preferences ) )

    def test_extensions_preferences_7_Rev(self):

        self.assertEqual("Wash Clothes is preferred over Clean Windows",
                         get_preferred_options_extension(self.task_5,self.task_3,self.task_all_preferences ) )
