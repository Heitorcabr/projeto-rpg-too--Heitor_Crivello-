from model.personagem import Personagem
from model.missao import MissaoCaca, MissaoColeta, MissaoEscolta
from model.enums import StatusMissao

def demonstracao_rpg():
    print("          SIMULAÇÃO RPG: TESTE DE MISSÕES            \n")
  


    heroi = Personagem("Aragorn", 100, 100, 20, 10)  # Nome, Vida, Vida Máxima, Ataque, Defesa
    
    # Criamos missões balanceadas para que o herói ganhe XP suficiente para subir de nível
    missao_caca = MissaoCaca("Caçada aos Goblins", "Eliminar os goblins da caverna.", 40, 6)      # Base 40 + (6 * 10) = 100 XP
    missao_coleta = MissaoColeta("Colheita Noturna", "Coletar cogumelos azuis.", 30, 4)         # Base 30 + (4 * 5) = 50 XP
    missao_escolta = MissaoEscolta("Caravana Real", "Escoltar o ferreiro até a vila.", 50, 5)   # Base 50 + (5 * 15) = 125 XP

    lista_missoes = [missao_caca, missao_coleta, missao_escolta]
    
    print("[Passo 1] Listando e Iniciando as Missões Disponíveis")
    for missao in lista_missoes:
        # Exibe os dados iniciais usando o método herdado da classe mãe
        print(missao.exibir_dados())
        # Inicia a missão demonstrando o comportamento dinâmico
        print(missao.iniciar_missao())
        print("-" * 50)

    print("\n--- [Passo 2] Ciclo de Evolução e Level Up do Herói ---")
    print(f"ATRIBUTOS ANTES: Nome: {heroi.nome} | Nível: {heroi.nivel} | XP: {heroi.xp}\n")
    
    print(f"Concluindo a missão: '{missao_caca.nome}'...")
    missao_caca.concluir_missao(heroi)
    
    print(f"\nATRIBUTOS DEPOIS: Nome: {heroi.nome} | Nível: {heroi.nivel} | XP: {heroi.xp}")
    print("-" * 50)

    # 4. Provoque um erro de propósito (status inválido ou transição proibida) e o trate com try/except
    print("\n--- [Passo 3] Teste de Segurança: Forçando Erro de Transição ---")
    print(f"Status atual da missão '{missao_coleta.nome}': {missao_coleta.status.name}")
    
    try:
        print("Tentando retroceder o status de EM_ANDAMENTO direto para PENDENTE...")
        missao_coleta.status = StatusMissao.PENDENTE
        
    except ValueError as erro:
        print("\n[SUCESSO] O sistema de encapsulamento bloqueou a operação ilegal!")
        print(f"Mensagem de erro capturada: {erro}")
        
    print("\n          FIM DA DEMONSTRAÇÃO DO TRABALHO             \n")

if __name__ == "__main__":
    demonstracao_rpg()
