import json
import os
from estruturas import Figurinha, Album, Fila, Historico, RegistroTroca

ARQUIVO_DADOS = "dados_album.json"


def salvar_dados(album: Album, repetidas: Fila, historico: Historico,
                 nome_usuario: str):
    dados = {
        "usuario": nome_usuario,
        "album": [f.to_dict() for f in album.listar_todas()],
        "repetidas": [f.to_dict() for f in repetidas.listar_todas()],
        "historico": [r.to_dict() for r in historico.listar()],
    }
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arq:
        json.dump(dados, arq, ensure_ascii=False, indent=2)


def carregar_dados() -> tuple[str, Album, Fila, Historico]:
    album = Album()
    repetidas = Fila()
    historico = Historico()
    nome_usuario = "Colecionador"

    if not os.path.exists(ARQUIVO_DADOS):
        return nome_usuario, album, repetidas, historico

    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arq:
            dados = json.load(arq)

        nome_usuario = dados.get("usuario", "Colecionador")

        for d in dados.get("album", []):
            album.adicionar(Figurinha.from_dict(d))

        for d in dados.get("repetidas", []):
            repetidas.enqueue(Figurinha.from_dict(d))

        for d in dados.get("historico", []):
            historico.registrar(RegistroTroca.from_dict(d))

    except (json.JSONDecodeError, KeyError, TypeError):
        pass

    return nome_usuario, album, repetidas, historico
