import unittest

import HtmlTestRunner

from tests.test_cerc import TestCerc

from tests.test_patrat import TestPatrat


class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        # tests_to_run.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestCerc))
        # tests_to_run.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(T))
        tests_to_run.addTests(
            [unittest.defaultTestLoader.loadTestsFromTestCase(TestCerc),
             unittest.defaultTestLoader.loadTestsFromTestCase(TestPatrat)])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="UnitTestResults",
            report_name="report"
        )

        runner.run(tests_to_run)