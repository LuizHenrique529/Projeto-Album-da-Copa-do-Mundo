class Figurinha:
    def __init__(self, id: int, nome: str, pais: str, posicao: str, raridade: str):
        self.id = id
        self.nome = nome
        self.pais = pais
        self.posicao = posicao
        self.raridade = raridade

    def __str__(self):
        return (f"[{self.id:03d}] {self.nome} | {self.pais} | "
                f"{self.posicao} | {self.raridade}")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "pais": self.pais,
            "posicao": self.posicao,
            "raridade": self.raridade,
        }

    @staticmethod
    def from_dict(d):
        return Figurinha(d["id"], d["nome"], d["pais"], d["posicao"], d["raridade"])


class NodoLista:
    def __init__(self, figurinha: Figurinha):
        self.figurinha = figurinha
        self.proximo: "NodoLista | None" = None


class Album:
    TOTAL_FIGURINHAS = 638

    def __init__(self):
        self._cabeca: NodoLista | None = None
        self._tamanho: int = 0

    def adicionar(self, figurinha: Figurinha) -> bool:
        if self.buscar(figurinha.id) is not None:
            return False
        novo = NodoLista(figurinha)
        if self._cabeca is None:
            self._cabeca = novo
        else:
            atual = self._cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo
        self._tamanho += 1
        return True

    def remover(self, id_figurinha: int) -> Figurinha | None:
        if self._cabeca is None:
            return None
        if self._cabeca.figurinha.id == id_figurinha:
            removida = self._cabeca.figurinha
            self._cabeca = self._cabeca.proximo
            self._tamanho -= 1
            return removida
        atual = self._cabeca
        while atual.proximo is not None:
            if atual.proximo.figurinha.id == id_figurinha:
                removida = atual.proximo.figurinha
                atual.proximo = atual.proximo.proximo
                self._tamanho -= 1
                return removida
            atual = atual.proximo
        return None

    def buscar(self, id_figurinha: int) -> Figurinha | None:
        atual = self._cabeca
        while atual is not None:
            if atual.figurinha.id == id_figurinha:
                return atual.figurinha
            atual = atual.proximo
        return None

    def buscar_por_nome(self, nome: str):
        resultado = []
        atual = self._cabeca
        while atual is not None:
            if nome.lower() in atual.figurinha.nome.lower():
                resultado.append(atual.figurinha)
            atual = atual.proximo
        return resultado

    def buscar_por_pais(self, pais: str):
        resultado = []
        atual = self._cabeca
        while atual is not None:
            if pais.lower() in atual.figurinha.pais.lower():
                resultado.append(atual.figurinha)
            atual = atual.proximo
        return resultado

    def listar_todas(self):
        resultado = []
        atual = self._cabeca
        while atual is not None:
            resultado.append(atual.figurinha)
            atual = atual.proximo
        return resultado

    def porcentagem_conclusao(self) -> float:
        return (self._tamanho / self.TOTAL_FIGURINHAS) * 100

    def tamanho(self) -> int:
        return self._tamanho


class NodoFila:
    def __init__(self, figurinha: Figurinha):
        self.figurinha = figurinha
        self.proximo: "NodoFila | None" = None


class Fila:
    def __init__(self):
        self._inicio: NodoFila | None = None
        self._fim: NodoFila | None = None
        self._tamanho: int = 0

    def enqueue(self, figurinha: Figurinha):
        novo = NodoFila(figurinha)
        if self._fim is None:
            self._inicio = novo
            self._fim = novo
        else:
            self._fim.proximo = novo
            self._fim = novo
        self._tamanho += 1

    def dequeue(self) -> Figurinha | None:
        if self._inicio is None:
            return None
        removida = self._inicio.figurinha
        self._inicio = self._inicio.proximo
        if self._inicio is None:
            self._fim = None
        self._tamanho -= 1
        return removida

    def peek(self) -> Figurinha | None:
        if self._inicio is None:
            return None
        return self._inicio.figurinha

    def limpar(self):
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def esta_vazia(self) -> bool:
        return self._inicio is None

    def tamanho(self) -> int:
        return self._tamanho

    def buscar_por_id(self, id_figurinha: int) -> bool:
        atual = self._inicio
        while atual is not None:
            if atual.figurinha.id == id_figurinha:
                return True
            atual = atual.proximo
        return False

    def remover_por_id(self, id_figurinha: int) -> Figurinha | None:
        if self._inicio is None:
            return None
        if self._inicio.figurinha.id == id_figurinha:
            return self.dequeue()
        atual = self._inicio
        while atual.proximo is not None:
            if atual.proximo.figurinha.id == id_figurinha:
                removida = atual.proximo.figurinha
                if atual.proximo == self._fim:
                    self._fim = atual
                atual.proximo = atual.proximo.proximo
                self._tamanho -= 1
                return removida
            atual = atual.proximo
        return None

    def listar_todas(self):
        resultado = []
        atual = self._inicio
        while atual is not None:
            resultado.append(atual.figurinha)
            atual = atual.proximo
        return resultado


class RegistroTroca:
    def __init__(self, usuario1: str, figurinha1: Figurinha,
                 usuario2: str, figurinha2: Figurinha, timestamp: str):
        self.usuario1 = usuario1
        self.figurinha1 = figurinha1
        self.usuario2 = usuario2
        self.figurinha2 = figurinha2
        self.timestamp = timestamp

    def __str__(self):
        return (f"[{self.timestamp}] {self.usuario1} deu {self.figurinha1.nome} "
                f"<-> {self.usuario2} deu {self.figurinha2.nome}")

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "usuario1": self.usuario1,
            "figurinha1": self.figurinha1.to_dict(),
            "usuario2": self.usuario2,
            "figurinha2": self.figurinha2.to_dict(),
        }

    @staticmethod
    def from_dict(d):
        return RegistroTroca(
            d["usuario1"], Figurinha.from_dict(d["figurinha1"]),
            d["usuario2"], Figurinha.from_dict(d["figurinha2"]),
            d["timestamp"],
        )


class NodoHistorico:
    def __init__(self, registro: RegistroTroca):
        self.registro = registro
        self.proximo: "NodoHistorico | None" = None


class Historico:
    def __init__(self):
        self._inicio: NodoHistorico | None = None
        self._fim: NodoHistorico | None = None
        self._tamanho: int = 0

    def registrar(self, registro: RegistroTroca):
        novo = NodoHistorico(registro)
        if self._fim is None:
            self._inicio = novo
            self._fim = novo
        else:
            self._fim.proximo = novo
            self._fim = novo
        self._tamanho += 1

    def listar(self):
        resultado = []
        atual = self._inicio
        while atual is not None:
            resultado.append(atual.registro)
            atual = atual.proximo
        return resultado

    def tamanho(self) -> int:
        return self._tamanho

    def esta_vazio(self) -> bool:
        return self._inicio is None
