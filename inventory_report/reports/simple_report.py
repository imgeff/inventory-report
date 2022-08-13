class SimpleReport:
    @staticmethod
    def order_fabrication(product):
        return product["data_de_fabricacao"]

    @staticmethod
    def order_validity(product):
        return product["data_de_validade"]

    @staticmethod
    def order_products(company):
        return company["quantity_products"]

    @staticmethod
    def get_company_more_products(list):
        list.sort(reverse=True, key=SimpleReport.order_products)
        return list[0]["nome_da_empresa"]

    @staticmethod
    def get_fabrication_more_old(list):
        list.sort(key=SimpleReport.order_fabrication)
        return list[0]["data_de_fabricacao"]

    @staticmethod
    def get_validity_more_recent(list):
        list.sort(key=SimpleReport.order_validity)
        return list[0]["data_de_validade"]

    @staticmethod
    def set_list_companies(list_of_products):
        list_of_companies = []

        for product in list_of_products:
            company = {
                "nome_da_empresa": product["nome_da_empresa"],
                "quantity_products": 0
            }

            if company not in list_of_companies:
                list_of_companies.append(company)

        return list_of_companies

    @staticmethod
    def calculate_company_products(list_products):
        list_companies = SimpleReport.set_list_companies(list_products)

        for company in list_companies:
            for product in list_products:
                if product["nome_da_empresa"] == company["nome_da_empresa"]:
                    company["quantity_products"] += 1

        return list_companies

    @staticmethod
    def generate(list):
        fabrication_more_old = SimpleReport.get_fabrication_more_old(list)
        validity_more_recent = SimpleReport.get_validity_more_recent(list)
        companies = SimpleReport.calculate_company_products(list)
        company_more_products = (
            SimpleReport.get_company_more_products(companies))
        return (
            f"Data de fabricação mais antiga: {fabrication_more_old}\n"
            f"Data de validade mais próxima: {validity_more_recent}\n"
            f"Empresa com mais produtos: {company_more_products}"
        )
