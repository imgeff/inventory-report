import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):

    @staticmethod
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

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
