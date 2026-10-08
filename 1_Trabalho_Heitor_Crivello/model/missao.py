# Justificativa do Setter (Parte 1):
# O único setter com lógica de alteração que faz sentido durante o jogo é o do 'status'.
# Atributos como 'nome', 'descricao' e 'recompensa' são definidos na criação da missão e
# devem permanecer imutáveis para evitar modificações acidentais ou trapaças ao longo do jogo.

from model.enums import StatusMissao

class Missao:
    def __init__(self, nome: str, descricao: str, recompensa: int):
        self.__nome = nome
        self.__descricao = descricao
        self.__recompensa = recompensa
        self.__status = StatusMissao.PENDENTE

    # --- Propriedades de Leitura (Getters) (Parte 1) ---
    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def recompensa(self) -> int:
        return self.__recompensa

    @property
    def status(self) -> StatusMissao:
        return self.__status

    # --- Setter com validação rígida de estados (Parte 2) ---
    @status.setter
    def status(self, novo_status: StatusMissao):
        if not isinstance(novo_status, StatusMissao):
            raise ValueError("Status inválido.")
        
        # Sequência estrita: PENDENTE -> EM_ANDAMENTO -> CONCLUIDA
        if self.__status == StatusMissao.PENDENTE and novo_status != StatusMissao.EM_ANDAMENTO:
            raise ValueError(f"Transição proibida! Não é possível mudar de PENDENTE para {novo_status.name}.")
        elif self.__status == StatusMissao.EM_ANDAMENTO and novo_status != StatusMissao.CONCLUIDA:
            raise ValueError(f"Transição proibida! Não é possível mudar de EM_ANDAMENTO para {novo_status.name}.")
        elif self.__status == StatusMissao.CONCLUIDA:
            raise ValueError("Transição proibida! Uma missão CONCLUIDA não pode ter seu status alterado.")
            
        self.__status = novo_status

    # --- Métodos Base Fornecidos pelo Professor (Adaptados para as propriedades e Enum) ---
    def iniciar_missao(self):
        if self.status == StatusMissao.PENDENTE:
            self.status = StatusMissao.EM_ANDAMENTO  # Utiliza o setter com validação
            return f"A missão {self.nome} começou! O objetivo é {self.descricao}."
        else:
            return f'A missão {self.nome} já foi iniciada!!!'

    def exibir_dados(self):
        # .name exibe o texto amigável do Enum (Ex: "PENDENTE" ou "EM_ANDAMENTO")
        msg = f'''
[{self.__class__.__name__}]
Nome: {self.nome}
Descrição: {self.descricao}
Recompensa: {self.recompensa}
Status: {self.status.name}
'''
        return msg

    def __str__(self):
        return f'missão [{self.__class__.__name__}]: {self.nome} | status: {self.status.name}'

    # --- Método base para cálculo de recompensa (Parte 3) ---
    def calcular_recompensa(self) -> int:
        if self.status is not StatusMissao.CONCLUIDA:
            return 0
        return self.recompensa

    # --- Entrega de XP ao herói (Parte 4) ---
    def concluir_missao(self, heroi):
        # Garante o cumprimento completo da sequência exigida pelo enunciado
        if self.status == StatusMissao.PENDENTE:
            self.status = StatusMissao.EM_ANDAMENTO
            
        self.status = StatusMissao.CONCLUIDA
        
        # Calcula a recompensa total (polimorfismo nas subclasses)
        xp_ganho = self.calcular_recompensa()
        
        # Repassa a recompensa ao herói utilizando o método existente
        heroi.ganhar_experiencia(xp_ganho)


# =====================================================================
# PARTE 3: Subclasses de Missão 
# =====================================================================

class MissaoCaca(Missao):
    def __init__(self, nome: str, descricao: str, recompensa: int, qtd_inimigos: int):
        super().__init__(nome, descricao, recompensa)
        self.__qtd_inimigos = qtd_inimigos  

    @property
    def qtd_inimigos(self) -> int:
        return self.__qtd_inimigos

    def calcular_recompensa(self) -> int:
        recompensa_base = super().calcular_recompensa()
        if recompensa_base == 0:
            return 0
        return recompensa_base + (self.__qtd_inimigos * 10)


class MissaoColeta(Missao):
    def __init__(self, nome: str, descricao: str, recompensa: int, itens_requeridos: int):
        super().__init__(nome, descricao, recompensa)
        self.__itens_requeridos = itens_requeridos

    @property
    def itens_requeridos(self) -> int:
        return self.__itens_requeridos

    def calcular_recompensa(self) -> int:
        recompensa_base = super().calcular_recompensa()
        if recompensa_base == 0:
            return 0
        return recompensa_base + (self.__itens_requeridos * 5)


class MissaoEscolta(Missao):
    def __init__(self, nome: str, descricao: str, recompensa: int, distancia_km: int):
        super().__init__(nome, descricao, recompensa)
        self.__distancia_km = distancia_km

    @property
    def distancia_km(self) -> int:
        return self.__distancia_km

    def calcular_recompensa(self) -> int:
        recompensa_base = super().calcular_recompensa()
        if recompensa_base == 0:
            return 0
        return recompensa_base + (self.__distancia_km * 15)
