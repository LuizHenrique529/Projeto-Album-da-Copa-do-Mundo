# Projeto-Album-da-Copa-do-Mundo
# Álbum de Figurinhas — Copa 2026
### Projeto 3 — FATEC · Estrutura de Dados

---

## Como executar

```bash
cd album_copa2026
python main.py
```

Requisito: **Python 3.10+** (sem dependências externas).

---

## Estrutura do Projeto

```
album_copa2026/
├── main.py          → Ponto de entrada e menu principal
├── estruturas.py    → Classes de dados (Figurinha, Nós, Listas, Filas)
├── menus.py         → Lógica de todas as telas/ações
├── persistencia.py  → Salvar e carregar JSON
├── ui.py            → Utilitários de exibição e validação
└── dados_album.json → Gerado automaticamente ao salvar
```

---

## Estruturas de Dados Implementadas

| Classe        | Tipo                  | Descrição                                      |
|---------------|-----------------------|------------------------------------------------|
| `NodoLista`   | Nó                    | Encapsula uma Figurinha para a lista encadeada |
| `Album`       | Lista Encadeada       | Armazena as figurinhas do álbum (sem `list`)   |
| `NodoFila`    | Nó                    | Encapsula uma Figurinha para a fila FIFO       |
| `Fila`        | Fila FIFO (manual)    | Fila de figurinhas repetidas (sem `deque`)     |
| `NodoHistorico`| Nó                   | Nó encadeado para o histórico de trocas        |
| `Historico`   | Fila FIFO (manual)    | Registra todas as trocas realizadas            |

---

## Funcionalidades

### Álbum (Lista Encadeada)
- Inserir figurinha (evita duplicatas — envia para repetidas automaticamente)
- Remover figurinha por ID
- Consultar figurinha por ID
- Visualizar álbum completo ordenado
- Barra de progresso com porcentagem de conclusão (total: 638 figurinhas)

### Figurinhas Repetidas (Fila FIFO)
- Armazenamento automático ao inserir duplicata
- Listagem completa com cores por raridade
- Contagem de repetidas disponíveis

### Sistema de Buscas
- Busca por número/ID
- Busca por nome do jogador (parcial, case-insensitive)
- Busca por seleção (menu de países)

### Sistema de Trocas (Fila FIFO + Histórico)
- Proposta entre dois usuários
- Verificação automática de disponibilidade nas repetidas
- Transferência automática: remove das repetidas, adiciona ao álbum
- Registro completo com timestamp na fila de histórico

### Persistência
- Formato **JSON** (`dados_album.json`)
- Salvo explicitamente via "Salvar e Sair"
- Carregado automaticamente ao iniciar o programa

---

## Raridades e Cores

| Raridade  | Cor no terminal |
|-----------|-----------------|
| Comum     | Branco          |
| Incomum   | Verde           |
| Rara      | Azul            |
| Lendária  | Amarelo/Dourado |
