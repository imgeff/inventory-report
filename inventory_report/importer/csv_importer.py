from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):

    @staticmethod
    def convert_dict_reader_to_list(dict_reader):
        data = []
        for row in dict_reader:
            data.append(row)
        return data

    @staticmethod
    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path, encoding="utf-8") as file:
            dict_reader = csv.DictReader(file)
            data = CsvImporter.convert_dict_reader_to_list(dict_reader)
        return data
