from enum import Enum

class ClasseHeroi(Enum):
    GUERREIRO = "Guerreiro"
    MAGO = "Mago"
    ARQUEIRO = "Arqueiro"


class TipoInimigo(Enum):
    ORC = "Orc"
    GOBLIN = 'Goblin'
    DRAGAO = 'Dragão'

class StatusMissao(Enum):
    PENDENTE = 1
    EM_ANDAMENTO = 2
    CONCLUIDA = 3