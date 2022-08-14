# from simple_report import SimpleReport
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def order_by_id(company):
        return company["id"]

    @staticmethod
    def mount_additional_report(list_products):
        additional_report = "\nProdutos estocados por empresa:\n"
        list_companies = (
            SimpleReport.calculate_company_products(list_products))

        for company in list_companies:
            name_company = company["nome_da_empresa"]
            quantity = company["quantity_products"]
            additional_report += f"- {name_company}: {quantity}\n"
        return additional_report

    @staticmethod
    def generate(list):
        simple_report = SimpleReport.generate(list)
        additional_report = CompleteReport.mount_additional_report(list)
        report = simple_report + additional_report
        return report
