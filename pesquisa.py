
print("================================")
print("     PESQUISA DE OPINIÃO")
print("          TUDOWEB")
print("================================")

excelente = 0
bom = 0
ruim = 0

total_entrevistados = 50

for i in range(1, total_entrevistados + 1):

    print(f"\n--- Entrevistado {i} ---")

    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")

    print("\nComo você avalia nosso atendimento?")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = input("Digite sua resposta: ")

    while opiniao not in ["1", "2", "3"]:
        print("Opção inválida! Escolha 1, 2 ou 3.")
        opiniao = input("Digite sua resposta: ")

    if opiniao == "1":
        excelente += 1
        print("Resposta registrada: EXCELENTE")

    elif opiniao == "2":
        bom += 1
        print("Resposta registrada: BOM")

    else:
        ruim += 1
        print("Resposta registrada: RUIM")

print("\n================================")
print("       RESULTADO DA PESQUISA")
print("================================")

print("Total de entrevistados:", total_entrevistados)
print("EXCELENTE:", excelente)
print("BOM:", bom)
print("RUIM:", ruim)

print("\nPesquisa finalizada!")
