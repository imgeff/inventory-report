import csv
import json
import xml.etree.ElementTree as ET
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
    def read_csv(path):
        with open(path, encoding="utf-8") as file:
            dict_reader = csv.DictReader(file)
            data = Inventory.convert_dict_reader_to_list(dict_reader)
        return data

    @staticmethod
    def read_json(path):
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
        return data

    @staticmethod
    def read_xml(path):
        tree = ET.parse(path)
        root = tree.getroot()
        data = [
            {
                "id": child[0].text,
                "nome_do_produto": child[1].text,
                "nome_da_empresa": child[2].text,
                "data_de_fabricacao": child[3].text,
                "data_de_validade": child[4].text,
                "numero_de_serie": child[5].text,
                "instrucoes_de_armazenamento": child[6].text
            } for child in root
        ]
        
        return data

    @staticmethod
    def import_data(path, type_report):
        data = ""
        if path.endswith(".json"):
            data = Inventory.read_json(path)
        elif path.endswith(".csv"):
            data = Inventory.read_csv(path)
        else:
            data = Inventory.read_xml(path)
        return Inventory.handle_type_report(data, type_report)


# if __name__ == "__main__":
#     Inventory.read_xml('inventory_report/data/inventory.xml')
