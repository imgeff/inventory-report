from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from tests.report_decorator.data_tests import (
    inventory,
    green_phrases,
    red_phrases, blue_phrases
)


def test_decorar_relatorio():

    colored_report = ColoredReport(SimpleReport)
    report = colored_report.generate(inventory)
    for list_phrases in green_phrases, red_phrases, blue_phrases:
        for phrase in list_phrases:
            assert phrase in report
