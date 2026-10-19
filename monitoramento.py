
from colorama import init, Fore, Style

# Inicializa a biblioteca Colorama
init()

# Lista com os níveis, as situações e as cores
niveis = [
    ("Nível 1 - Muito baixo (crítico)", Fore.RED),
    ("Nível 2 - Baixo", Fore.YELLOW),
    ("Nível 3 - Médio", Fore.GREEN),
    ("Nível 4 - Alto", Fore.CYAN),
    ("Nível 5 - Muito alto (alerta)", Fore.BLUE)
]

# Função responsável por exibir a mensagem colorida
def exibir_nivel(nivel):
    if nivel >= 1 and nivel <= 5:
        mensagem, cor = niveis[nivel - 1]
        print(cor + mensagem + Style.RESET_ALL)
    else:
        print("Nível inválido! Informe um número de 1 a 5.")

# Simulação do nível atual do reservatório
nivel_atual = 3

# Exibição do monitoramento
print("=== MONITORAMENTO DO RESERVATÓRIO ===")
exibir_nivel(nivel_atual)
