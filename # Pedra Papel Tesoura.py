# Pedra Papel Tesoura
import random as r

placar = {"Jogador": 0, "Máquina": 0, "Empates": 0}

def jogo(replay=False):
#    Variáveis
   resposta = ["sim", "não"]
   lista_Variaveis = ["pedra", "papel", "tesoura"]

   if not replay:
      while True:
         resposta_player = input("Vamos jogar Pedra, Papel e Tesoura? ").strip().lower()
         if resposta_player in resposta:
            break
         else:
            print("Resposta não aceita, tente novamente!")
   else:
      resposta_player = "sim"

   if resposta_player == resposta[0]:
        opcoes = [input("Ótimo, vamos jogar! Digite sua opção: ").strip().lower()]
        while True:
            if opcoes[0] not in lista_Variaveis:
               opcoes[0] = input("Essa opção não foi aceita. Tente outra! ")
            else:
               break
   else:
        print("Tudo bem! Jogaremos mais tarde! :)")
        return None

#  Lado Máquina
   numero_Aleatorio = r.randint(0,2)
   print(lista_Variaveis[numero_Aleatorio])
   opcoes.append(numero_Aleatorio)

# Conversão de valores str para int

   for posicao, objeto in enumerate(lista_Variaveis):
      if objeto == opcoes[0]:
         opcoes[0] = posicao
          
   return opcoes

def checagem_Valores(valores_Player_Maquina):

   if valores_Player_Maquina == None:
      return
   if valores_Player_Maquina[0] == valores_Player_Maquina[1]:
      placar["Empates"] += 1
      reJogar("Empate!")

      return
   else:
      resultados = str(valores_Player_Maquina[0])+str(valores_Player_Maquina[1])
   
   # Definição dos resultados possíveis
   vitoria_Player = ["10", "21", "02"]

   if resultados in vitoria_Player:
      placar["Jogador"] += 1
      reJogar("Você")
   
   else:
      placar["Máquina"] += 1
      reJogar("A máquina")
   
   return

def reJogar(ganhador):
   if ganhador == "Empate!":
      print("Placar: ","Empates", placar["Empates"],"Jogador", placar["Jogador"],"Máquina", placar["Máquina"])
      retry = input(f"{ganhador} Gostaria de jogar novamente? ").strip().lower()
   else:
      print("Placar: ","Empates", placar["Empates"],"Jogador", placar["Jogador"],"Máquina", placar["Máquina"])
      retry = input(f"{ganhador} ganhou! Gostaria de jogar novamente? ").strip().lower()

   if retry == "sim":
      checagem_Valores(jogo(True))
   else: 
      print("Okay, jogaremos mais tarde! :) ")

checagem_Valores(jogo())