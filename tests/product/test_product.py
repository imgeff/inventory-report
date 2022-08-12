from inventory_report.inventory.product import Product
from tests.data_fakes.product import product_fake


def test_cria_produto():
    product = Product(
        product_fake["id"],
        product_fake["nome_do_produto"],
        product_fake["nome_da_empresa"],
        product_fake["data_de_fabricacao"],
        product_fake["data_de_validade"],
        product_fake["numero_de_serie"],
        product_fake["instrucoes_de_armazenamento"]
    )
    assert product.id == product_fake["id"]
    assert product.nome_do_produto == product_fake["nome_do_produto"]
    assert product.nome_da_empresa == product_fake["nome_da_empresa"]
    assert product.data_de_fabricacao == product_fake["data_de_fabricacao"]
    assert product.data_de_validade == product_fake["data_de_validade"]
    assert product.numero_de_serie == product_fake["numero_de_serie"]
    assert product.instrucoes_de_armazenamento == (
        product_fake["instrucoes_de_armazenamento"])
