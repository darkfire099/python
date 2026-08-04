#Uma loja de produtos eletronicos tem os seguinetes produtos em estoque:
#monitor, teclado, mouse, headset
#o gerente te pediu para adicionar webcan no final da lista
#atualizar o teclado para teclado mecanico
#verificar se tem impressora na lista
#remover mouse da lista
estoque = ["monito", "teclado", "mouse", "headset"]
estoque.append ("webcam")
print(estoque)
posicao_teclado = estoque.index ("teclado")
print (posicao_teclado)
estoque[1] = "teclado mecânico"
print(estoque)
impressora_no_estoque = "impressora" in estoque
print("impressora no estoque?", impressora_no_estoque)
estoque.remove("mouse")
print(estoque)
estoque.insert(1,"mouse")
print(estoque)