import unittest
import importlib
import sqlite3
import pandas as pd

class TestFinal(unittest.TestCase):
    def test_01(self):
        time_series_confirmed, time_series_deaths = asgmt.import_time_series_confirmed_deaths()
        self.assertEqual(time_series_confirmed.shape, (289, 1147))
        self.assertEqual(time_series_deaths.shape, (289, 1147))
    def test_02(self):
        time_series_confirmed_long, time_series_deaths_long = asgmt.transform_time_series_confirmed_deaths()
        self.assertEqual(time_series_confirmed_long.shape, (330327, 6))
        self.assertEqual(time_series_deaths_long.shape, (330327, 6))
    def test_03(self):
        merged_time_series = asgmt.merge_time_series()
        self.assertEqual(merged_time_series.shape, (330327, 7))
    def test_04(self):
        groupby_time_series = asgmt.groupby_date_country()
        self.assertEqual(groupby_time_series.shape, (229743, 4))
    def test_05(self):
        formatted_time_series = asgmt.format_date_column()
        self.assertEqual(formatted_time_series.shape, (229743, 4))
    def test_06(self):
        last_day = asgmt.snapshot_last_day()
        self.assertEqual(last_day.shape, (201, 4))
    def test_07(self):
        table_shapes = asgmt.summarize_table_shapes()
        self.assertEqual(table_shapes.shape, (10, 3))
        self.assertEqual(table_shapes.iloc[:, 1].min(), 5)
        self.assertEqual(table_shapes.iloc[:, 2].min(), 2)
        self.assertEqual(table_shapes.iloc[:, 1].max(), 338105)
        self.assertEqual(table_shapes.iloc[:, 2].max(), 8)
        table_list = ["aboriginal_legislators", "candidates", "districts", "election_types", "parties", "party_legislators", "polling_places", "presidents", "regional_legislators", "villages"]
        table_names = table_shapes.iloc[:, 0].to_list()
        for tbl in table_list:
            self.assertIn(tbl, table_names)
    def test_08(self):
        presidential_votes = asgmt.summarize_presidential_votes()
        self.assertEqual(presidential_votes.shape, (3, 3))
        self.assertEqual(presidential_votes.iloc[:, 2].max(), 5586019)
        self.assertEqual(presidential_votes.iloc[:, 2].min(), 3690466)
        parties = presidential_votes.iloc[:, 0].to_list()
        candidates = presidential_votes.iloc[:, 1].to_list()
        for party in ["民主進步黨", "中國國民黨", "台灣民眾黨"]:
            self.assertIn(party, parties)
        for candidate in ["賴清德/蕭美琴", "侯友宜/趙少康", "柯文哲/吳欣盈"]:
            self.assertIn(candidate, candidates)
    def test_09(self):
        regional_aborinal_legislator_votes = asgmt.summarize_regional_aborinal_legislator_votes()
        self.assertEqual(regional_aborinal_legislator_votes.shape, (33, 3))
        election_types = regional_aborinal_legislator_votes.iloc[:, 0].to_list()
        self.assertIn("區域及原住民立委", election_types)
        parties = regional_aborinal_legislator_votes.iloc[:, 1].to_list()
        for party in ["民主進步黨", "中國國民黨", "台灣民眾黨", "小民參政歐巴桑聯盟", "社會民主黨", "時代力量", "無"]:
            self.assertIn(party, parties)
    def test_10(self):
        party_legislator_votes = asgmt.summarize_party_legislator_votes()
        self.assertEqual(party_legislator_votes.shape, (16, 3))
        election_types = party_legislator_votes.iloc[:, 0].to_list()
        self.assertIn("不分區立委", election_types)
        parties = party_legislator_votes.iloc[:, 1].to_list()
        for party in ["民主進步黨", "中國國民黨", "台灣民眾黨", "小民參政歐巴桑聯盟", "台灣綠黨", "時代力量"]:
            self.assertIn(party, parties)
        
asgmt = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestFinal)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"You've got {number_of_successes} successes among {number_of_test_runs} questions.")