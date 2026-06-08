from persistencia import carregar_dados, salvar_dados
from menus import menu_album, menu_repetidas, menu_buscas, menu_trocas
from ui import (
    limpar_tela, titulo, cabecalho_menu, sucesso, info, pausar,
    ler_texto, COR_INFO, COR_RESET, COR_DIM, COR_TITULO,
)


BANNER = r"""
1

              ═══ COPA 2026 ═══ ÁLBUM VIRTUAL ═══
"""


def exibir_banner():
    print(f"{COR_TITULO}{BANNER}{COR_RESET}")


def menu_principal(nome_usuario: str) -> str:
    limpar_tela()
    exibir_banner()
    print(f"  {COR_DIM}Bem-vindo, {nome_usuario}!{COR_RESET}\n")

    opcoes = [
        "Gerenciar Álbum",
        "Figurinhas Repetidas",
        "Sistema de Buscas",
        "Sistema de Trocas",
        "Salvar e Sair",
    ]
    cabecalho_menu("MENU PRINCIPAL")
    for i, op in enumerate(opcoes, 1):
        print(f"  {COR_INFO}{i}.{COR_RESET} {op}")
    print(f"  {COR_INFO}0.{COR_RESET} Sair sem salvar")

    from ui import ler_opcao_menu
    return ler_opcao_menu(opcoes)


def configurar_usuario() -> str:
    limpar_tela()
    exibir_banner()
    print(f"  {COR_DIM}Nenhum dado salvo encontrado.{COR_RESET}")
    return ler_texto("\n  Qual é o seu nome? ", minimo=2, maximo=40)


def main():
    nome_usuario, album, repetidas, historico = carregar_dados()

    if nome_usuario == "Colecionador":
        nome_usuario = configurar_usuario()
        sucesso(f"Olá, {nome_usuario}! Seu álbum foi criado.")
        pausar()

    while True:
        opcao = menu_principal(nome_usuario)

        if opcao == "1":
            menu_album(album, repetidas)
        elif opcao == "2":
            menu_repetidas(repetidas)
        elif opcao == "3":
            menu_buscas(album)
        elif opcao == "4":
            menu_trocas(album, repetidas, historico, nome_usuario)
        elif opcao == "5":
            salvar_dados(album, repetidas, historico, nome_usuario)
            sucesso("Dados salvos com sucesso!")
            info("Até logo, campeão!")
            break
        elif opcao == "0":
            info("Saindo sem salvar. Seus dados não foram persistidos.")
            break


if __name__ == "__main__":
    main()
