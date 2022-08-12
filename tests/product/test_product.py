from inventory_report.inventory.product import Product


def test_cria_produto():
    dataTest = {
        "id": 1,
        "nome_do_produto": "produto de teste",
        "nome_da_empresa": "empresa de teste",
        "data_de_fabricacao": "12-08-2022",
        "data_de_validade": "22-08-2022",
        "numero_de_serie": "1234567890",
        "instrucoes_de_armazenamento": "instruções de teste"
    }
    product = Product(
        dataTest["id"],
        dataTest["nome_do_produto"],
        dataTest["nome_da_empresa"],
        dataTest["data_de_fabricacao"],
        dataTest["data_de_validade"],
        dataTest["numero_de_serie"],
        dataTest["instrucoes_de_armazenamento"]
    )
    assert product.id == dataTest["id"]
    assert product.nome_do_produto == dataTest["nome_do_produto"]
    assert product.nome_da_empresa == dataTest["nome_da_empresa"]
    assert product.data_de_fabricacao == dataTest["data_de_fabricacao"]
    assert product.data_de_validade == dataTest["data_de_validade"]
    assert product.numero_de_serie == dataTest["numero_de_serie"]
    assert product.instrucoes_de_armazenamento == (
        dataTest["instrucoes_de_armazenamento"])
