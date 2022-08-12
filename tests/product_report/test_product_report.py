from inventory_report.inventory.product import Product
from tests.data_fakes.product import product_fake


def test_relatorio_produto():
    (
        id_do_produto,
        produto,
        fabricacao,
        empresa,
        validade,
        serie,
        armazenamento
    ) = (
        product_fake["id"],
        product_fake["nome_do_produto"],
        product_fake["data_de_fabricacao"],
        product_fake["nome_da_empresa"],
        product_fake["data_de_validade"],
        product_fake["numero_de_serie"],
        product_fake["instrucoes_de_armazenamento"]
    )

    product = Product(
        id_do_produto,
        produto,
        empresa,
        fabricacao,
        validade,
        serie,
        armazenamento
    )

    assert str(product) == (
            f"O produto {produto}"
            f" fabricado em {fabricacao}"
            f" por {empresa} com validade"
            f" até {validade}"
            f" precisa ser armazenado {armazenamento}."
        )
