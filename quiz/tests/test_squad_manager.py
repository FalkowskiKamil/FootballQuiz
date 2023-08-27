from django.test import TestCase
from django.http import QueryDict
import pandas as pd
from quiz import squad_manager

class TestSquadManager(TestCase):
    def setUp(self):
        self.items_dict = {"Attack": [1, 2], "Midfield": [1, 2, 3, 4], "Defender": [1, 2, 3, 4], "Goalkeeper": [1]}
        self.query_dict = QueryDict(mutable=True)
        for key, values in self.items_dict.items():
            self.query_dict.setlist(key, values)
        
    def test_info_value_squad(self):
        result = squad_manager.info("value squad")
        self.assertIsInstance(result, pd.DataFrame)

    def test_info_goal_squad(self):
        result = squad_manager.info("goal squad")
        self.assertIsInstance(result, pd.DataFrame)

    def test_info_assist_squad(self):
        result = squad_manager.info("assist squad")
        self.assertIsInstance(result, pd.DataFrame)

    def test_info_yellow_squad(self):
        result = squad_manager.info("yellow squad")
        self.assertIsInstance(result, pd.DataFrame)
    
    def test_get_result_value_squad(self):
        result = squad_manager.get_squad_result("value squad", self.query_dict)
        self.assertIsNotNone(result)

    def test_get_result_goal_squad(self):
        result = squad_manager.get_squad_result("goal squad", self.query_dict)
        self.assertIsNotNone(result)

    def test_get_result_assist_squad(self):
        result = squad_manager.get_squad_result("assist squad", self.query_dict)
        self.assertIsNotNone(result)

    def test_get_result_yellow_squad(self):       
        result = squad_manager.get_squad_result("yellow squad", self.query_dict)
        self.assertIsNotNone(result)
