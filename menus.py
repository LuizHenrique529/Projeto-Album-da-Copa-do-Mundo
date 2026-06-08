from datetime import datetime
from estruturas import Figurinha, Album, Fila, Historico, RegistroTroca
from ui import (
    titulo, cabecalho_menu, sucesso, erro, info,
    exibir_figurinha, pausar, ler_inteiro, ler_texto,
    ler_opcao_lista, barra_progresso,
    RARIDADES, POSICOES, SELECOES, COR_INFO, COR_RESET, COR_DIM,
)


def _coletar_dados_figurinha() -> Figurinha | None:
    print(f"\n{COR_INFO}Cadastro de Figurinha{COR_RESET}")
    print(f"{COR_DIM}{'─' * 40}{COR_RESET}")

    id_fig = ler_inteiro("  ID (1-638): ", 1, 638)
    nome = ler_texto("  Nome do jogador: ")
    idx_pais = ler_opcao_lista(SELECOES, "Seleções disponíveis")
    pais = SELECOES[idx_pais]
    idx_pos = ler_opcao_lista(POSICOES, "Posições")
    posicao = POSICOES[idx_pos]
    idx_rar = ler_opcao_lista(RARIDADES, "Raridades")
    raridade = RARIDADES[idx_rar]

    return Figurinha(id_fig, nome, pais, posicao, raridade)


def menu_album(album: Album, repetidas: Fila):
    while True:
        titulo("Gerenciar Álbum")
        opcoes = [
            "Inserir figurinha",
            "Remover figurinha",
            "Consultar figurinha por ID",
            "Visualizar álbum completo",
            "Ver progresso do álbum",
        ]
        for i, op in enumerate(opcoes, 1):
            print(f"  {COR_INFO}{i}.{COR_RESET} {op}")
        print(f"  {COR_INFO}0.{COR_RESET} Voltar")

        from ui import ler_opcao_menu
        opcao = ler_opcao_menu(opcoes)

        if opcao == "1":
            _inserir_figurinha(album, repetidas)
        elif opcao == "2":
            _remover_figurinha(album)
        elif opcao == "3":
            _consultar_figurinha(album)
        elif opcao == "4":
            _visualizar_album(album)
        elif opcao == "5":
            _ver_progresso(album)
        elif opcao == "0":
            break

        pausar()


def _inserir_figurinha(album: Album, repetidas: Fila):
    titulo("Inserir Figurinha")
    fig = _coletar_dados_figurinha()
    if fig is None:
        return

    if album.adicionar(fig):
        sucesso(f"Figurinha '{fig.nome}' adicionada ao álbum!")
    else:
        info(f"Figurinha #{fig.id} já existe no álbum. Adicionando às repetidas.")
        repetidas.enqueue(fig)
        sucesso(f"Figurinha '{fig.nome}' adicionada às repetidas.")


def _remover_figurinha(album: Album):
    titulo("Remover Figurinha")
    if album.tamanho() == 0:
        info("O álbum está vazio.")
        return

    id_fig = ler_inteiro("  ID da figurinha a remover: ", 1, 638)
    removida = album.remover(id_fig)
    if removida:
        sucesso(f"Figurinha '{removida.nome}' removida do álbum.")
    else:
        erro(f"Figurinha #{id_fig} não encontrada no álbum.")


def _consultar_figurinha(album: Album):
    titulo("Consultar Figurinha")
    id_fig = ler_inteiro("  ID da figurinha: ", 1, 638)
    fig = album.buscar(id_fig)
    if fig:
        print()
        exibir_figurinha(fig, prefixo="  ")
    else:
        erro(f"Figurinha #{id_fig} não encontrada no álbum.")


def _visualizar_album(album: Album):
    titulo("Álbum Completo")
    todas = album.listar_todas()
    if not todas:
        info("O álbum está vazio.")
        return

    print(f"  {'ID':<5} {'Nome':<25} {'País':<15} {'Posição':<10} Raridade")
    print(f"  {'─' * 65}")
    for fig in todas:
        exibir_figurinha(fig, prefixo="  ")
    print(f"\n  Total: {album.tamanho()} figurinhas")


def _ver_progresso(album: Album):
    titulo("Progresso do Álbum")
    total = Album.TOTAL_FIGURINHAS
    atual = album.tamanho()
    pct = album.porcentagem_conclusao()
    barra = barra_progresso(atual, total)
    print(f"\n  {COR_INFO}{barra}{COR_RESET}")
    print(f"\n  Figurinhas coletadas : {atual}")
    print(f"  Total do álbum       : {total}")
    print(f"  Faltam               : {total - atual}")
    print(f"  Conclusão            : {pct:.2f}%")


def menu_repetidas(repetidas: Fila):
    while True:
        titulo("Figurinhas Repetidas")
        opcoes = [
            "Listar repetidas",
            "Contar repetidas",
        ]
        for i, op in enumerate(opcoes, 1):
            print(f"  {COR_INFO}{i}.{COR_RESET} {op}")
        print(f"  {COR_INFO}0.{COR_RESET} Voltar")

        from ui import ler_opcao_menu
        opcao = ler_opcao_menu(opcoes)

        if opcao == "1":
            _listar_repetidas(repetidas)
        elif opcao == "2":
            _contar_repetidas(repetidas)
        elif opcao == "0":
            break

        pausar()


def _listar_repetidas(repetidas: Fila):
    titulo("Lista de Repetidas")
    todas = repetidas.listar_todas()
    if not todas:
        info("Nenhuma figurinha repetida.")
        return

    print(f"  {'ID':<5} {'Nome':<25} {'País':<15} {'Posição':<10} Raridade")
    print(f"  {'─' * 65}")
    for fig in todas:
        exibir_figurinha(fig, prefixo="  ")


def _contar_repetidas(repetidas: Fila):
    titulo("Contagem de Repetidas")
    qtd = repetidas.tamanho()
    info(f"Você possui {qtd} figurinha(s) repetida(s).")


def menu_buscas(album: Album):
    while True:
        titulo("Sistema de Buscas")
        opcoes = [
            "Buscar por número (ID)",
            "Buscar por nome do jogador",
            "Buscar por seleção",
        ]
        for i, op in enumerate(opcoes, 1):
            print(f"  {COR_INFO}{i}.{COR_RESET} {op}")
        print(f"  {COR_INFO}0.{COR_RESET} Voltar")

        from ui import ler_opcao_menu
        opcao = ler_opcao_menu(opcoes)

        if opcao == "1":
            _buscar_por_id(album)
        elif opcao == "2":
            _buscar_por_nome(album)
        elif opcao == "3":
            _buscar_por_selecao(album)
        elif opcao == "0":
            break

        pausar()


def _buscar_por_id(album: Album):
    titulo("Busca por ID")
    id_fig = ler_inteiro("  ID da figurinha: ", 1, 638)
    fig = album.buscar(id_fig)
    if fig:
        print()
        exibir_figurinha(fig, prefixo="  ")
    else:
        erro(f"Nenhuma figurinha com ID {id_fig} encontrada no álbum.")


def _buscar_por_nome(album: Album):
    titulo("Busca por Nome")
    nome = ler_texto("  Nome (ou parte do nome): ", minimo=1)
    resultados = album.buscar_por_nome(nome)
    if resultados:
        print(f"\n  {len(resultados)} resultado(s) encontrado(s):\n")
        for fig in resultados:
            exibir_figurinha(fig, prefixo="  ")
    else:
        erro(f"Nenhum jogador com '{nome}' encontrado.")


def _buscar_por_selecao(album: Album):
    titulo("Busca por Seleção")
    idx = ler_opcao_lista(SELECOES, "Selecione o país")
    pais = SELECOES[idx]
    resultados = album.buscar_por_pais(pais)
    if resultados:
        print(f"\n  {len(resultados)} figurinha(s) de {pais}:\n")
        for fig in resultados:
            exibir_figurinha(fig, prefixo="  ")
    else:
        info(f"Nenhuma figurinha de {pais} no álbum.")


def menu_trocas(
    album: Album,
    repetidas: Fila,
    historico: Historico,
    nome_usuario: str,
):
    while True:
        titulo("Sistema de Trocas")
        opcoes = [
            "Propor e efetuar troca",
            "Ver histórico de trocas",
        ]
        for i, op in enumerate(opcoes, 1):
            print(f"  {COR_INFO}{i}.{COR_RESET} {op}")
        print(f"  {COR_INFO}0.{COR_RESET} Voltar")

        from ui import ler_opcao_menu
        opcao = ler_opcao_menu(opcoes)

        if opcao == "1":
            _efetuar_troca(album, repetidas, historico, nome_usuario)
        elif opcao == "2":
            _ver_historico(historico)
        elif opcao == "0":
            break

        pausar()


def _efetuar_troca(
    album: Album,
    repetidas: Fila,
    historico: Historico,
    nome_usuario: str,
):
    titulo("Propor Troca")

    if repetidas.esta_vazia():
        erro("Você não possui figurinhas repetidas para trocar.")
        return

    print(f"\n  {COR_INFO}Suas figurinhas repetidas disponíveis:{COR_RESET}")
    todas_rep = repetidas.listar_todas()
    for fig in todas_rep:
        exibir_figurinha(fig, prefixo="    ")

    id_oferta = ler_inteiro("\n  ID da figurinha que você vai OFERECER: ", 1, 638)
    if not repetidas.buscar_por_id(id_oferta):
        erro(f"Você não possui a figurinha #{id_oferta} nas repetidas.")
        return

    print(f"\n  {COR_INFO}─── Dados do outro usuário ───{COR_RESET}")
    nome_outro = ler_texto("  Nome do outro colecionador: ", minimo=2)

    print(f"\n  {COR_INFO}Cadastre a figurinha que {nome_outro} vai oferecer:{COR_RESET}")
    fig_recebida = _coletar_dados_figurinha()
    if fig_recebida is None:
        return

    if album.buscar(fig_recebida.id) is not None:
        erro(f"Você já possui a figurinha #{fig_recebida.id} no álbum. Troca cancelada.")
        return

    fig_ofertada = repetidas.remover_por_id(id_oferta)
    if fig_ofertada is None:
        erro("Erro ao remover a figurinha das repetidas.")
        return

    album.adicionar(fig_recebida)

    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    registro = RegistroTroca(
        nome_usuario, fig_ofertada,
        nome_outro, fig_recebida,
        timestamp,
    )
    historico.registrar(registro)

    sucesso("Troca efetuada com sucesso!")
    print(f"\n  Você deu    : ", end="")
    exibir_figurinha(fig_ofertada)
    print(f"  Você recebeu: ", end="")
    exibir_figurinha(fig_recebida)


def _ver_historico(historico: Historico):
    titulo("Histórico de Trocas")
    if historico.esta_vazio():
        info("Nenhuma troca registrada ainda.")
        return

    registros = historico.listar()
    print(f"  Total de trocas: {historico.tamanho()}\n")
    print(f"  {'─' * 65}")
    for reg in registros:
        print(f"  {reg}")
    print(f"  {'─' * 65}")
