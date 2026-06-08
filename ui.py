import os

RARIDADES = ["Comum", "Incomum", "Rara", "Lendária"]
POSICOES = ["Goleiro", "Zagueiro", "Lateral", "Volante",
            "Meia", "Atacante", "Ponta"]

SELECOES = [
    "Argentina", "Alemanha", "Brasil", "Colômbia", "Canadá", "França", "Espanha",
    "Inglaterra", "Portugal", "Haiti", "Holanda", "Bélgica",
    "Croácia", "Uruguai", "México", "EUA", "Marrocos",
    "Senegal", "Japão", "Coreia do Sul", "Austrália", "Escócia",
    "Suécia", "Noruega", "Suíça", "Egito", "Gana", "Costa do Marfim",
    "Tunísia", "Irã", "Arábia Saudita", "Equador", "Curaçao", "Panamá", "Catar", "África do Sul",
    "República Tcheca", "Bósnia", "Paraguai", "Hungria", "Turquia",
    "Nova Zelandia","Cabo Verde", "Uzbequistão", "Jordânia", "RD do Congo", "Argélia",
    "Iraque",
]

COR_RESET = "\033[0m"
COR_TITULO = "\033[1;33m"
COR_SUCESSO = "\033[1;32m"
COR_ERRO = "\033[1;31m"
COR_INFO = "\033[1;36m"
COR_MENU = "\033[1;35m"
COR_DIM = "\033[2m"

RARIDADE_COR = {
    "Comum": "\033[37m",
    "Incomum": "\033[32m",
    "Rara": "\033[34m",
    "Lendária": "\033[33m",
}


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def titulo(texto: str):
    largura = 60
    print(f"\n{COR_TITULO}{'═' * largura}")
    print(f"  {texto.upper()}")
    print(f"{'═' * largura}{COR_RESET}\n")


def cabecalho_menu(texto: str):
    print(f"\n{COR_MENU}{'─' * 50}")
    print(f"  {texto}")
    print(f"{'─' * 50}{COR_RESET}")


def sucesso(msg: str):
    print(f"\n{COR_SUCESSO}✔  {msg}{COR_RESET}")


def erro(msg: str):
    print(f"\n{COR_ERRO}✘  {msg}{COR_RESET}")


def info(msg: str):
    print(f"\n{COR_INFO}ℹ  {msg}{COR_RESET}")


def exibir_figurinha(fig, prefixo: str = ""):
    cor = RARIDADE_COR.get(fig.raridade, COR_RESET)
    print(f"{prefixo}{cor}[{fig.id:03d}] {fig.nome:<25} "
          f"{fig.pais:<15} {fig.posicao:<10} ★ {fig.raridade}{COR_RESET}")


def pausar():
    input(f"\n{COR_DIM}[ Pressione ENTER para continuar... ]{COR_RESET}")


def ler_inteiro(prompt: str, minimo: int = None, maximo: int = None) -> int:
    while True:
        try:
            valor = int(input(prompt).strip())
            if minimo is not None and valor < minimo:
                erro(f"Valor mínimo: {minimo}")
                continue
            if maximo is not None and valor > maximo:
                erro(f"Valor máximo: {maximo}")
                continue
            return valor
        except ValueError:
            erro("Por favor, digite um número inteiro válido.")


def ler_opcao_menu(opcoes: list[str]) -> str:
    validas = [str(i + 1) for i in range(len(opcoes))]
    validas.append("0")
    while True:
        opcao = input(f"\n{COR_INFO}▶ Escolha: {COR_RESET}").strip()
        if opcao in validas:
            return opcao
        erro(f"Opção inválida. Digite entre 0 e {len(opcoes)}.")


def ler_opcao_lista(itens: list[str], titulo_lista: str) -> int:
    print(f"\n{COR_INFO}{titulo_lista}:{COR_RESET}")
    for i, item in enumerate(itens, 1):
        print(f"  {i:2d}. {item}")
    return ler_inteiro(f"\n▶ Escolha (1-{len(itens)}): ", 1, len(itens)) - 1


def ler_texto(prompt: str, minimo: int = 2, maximo: int = 60) -> str:
    while True:
        valor = input(prompt).strip()
        if len(valor) < minimo:
            erro(f"Texto muito curto (mínimo {minimo} caracteres).")
            continue
        if len(valor) > maximo:
            erro(f"Texto muito longo (máximo {maximo} caracteres).")
            continue
        return valor


def barra_progresso(atual: int, total: int, largura: int = 40) -> str:
    if total == 0:
        return "[" + " " * largura + "] 0.0%"
    proporcao = atual / total
    preenchido = int(proporcao * largura)
    barra = "█" * preenchido + "░" * (largura - preenchido)
    return f"[{barra}] {proporcao * 100:.1f}%"
