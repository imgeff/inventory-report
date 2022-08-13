import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def handle_type_report(data, type_report):
        if type_report == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)

    @staticmethod
    def convert_dict_reader_to_list(dict_reader):
        data = []
        for row in dict_reader:
            data.append(row)
        return data

    @staticmethod
    def import_data(caminho, type_report):
        with open(caminho, encoding="utf-8") as file:
            dict_reader = csv.DictReader(file)
            data = Inventory.convert_dict_reader_to_list(dict_reader)
            return Inventory.handle_type_report(data, type_report)
