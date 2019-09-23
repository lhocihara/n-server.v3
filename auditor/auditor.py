import os, pymongo
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from tipos_transacoes import Tipos_Transacoes
from blockchain import Blockchain

blch = Blockchain()
sched = BlockingScheduler()
t = Tipos_Transacoes()

# manipulações de variáveis teste
c = 0
t.log_interno_cadastro_inicial_usuario("5d2d2adba3587900042e75b4")
t.log_interno_cadastro_inicial_usuario("5d34c11ee936920004aaa4a9")
t.log_interno_cadastro_inicial_usuario("5d4f2a90ef361b00042a1266")

@sched.scheduled_job('interval', seconds = 10)
def job_atualizador():
  print("\n\nJob adição de bloco\n-------------")
  # criando variável temporaria para receber os dados que entrarão neste bloco atual e preparando a lista para as próximas transações
  transacoes_temp = t.transacoes
  t.transacoes = []

  # verifica se há transações para serem armazenadas no bloco, caso não tiver, não há necessidade de criar um novo bloco.
  if (len(transacoes_temp)):
    # Adicionando um novo bloco à chain
    blch.add_new_block(transacoes_temp)
    
    # print(" \n\nminha lista de blocos é:")
    # lista = block.get_all() 
    # print(lista)
    # print(" \n\nLista de transações do último bloco é:")
    # b = blch.ultimo_bloco()

    # b = b["dados"].transacoes

    # print(b)

    # print(" \nPrimeira transação do último bloco:")
    # print(b[0])

    # print(" \nTipo do log: " + str(b[0]["tipo_log"]))
    # print(" \nId usuário: " + str(b[0]["id_usuario"]))
    # print(" \nDatetime: " + str(b[0]["datetime"]))

    # print(blch.get_all())
  else:
    # Informando que a lista de transções está vazia
    print("\n\nLista de transações atuais está vazia...")


# # resto do tratador de blockchain
# @sched.scheduled_job('interval', seconds = 0.5)
# def tester_transacao():

#   # manipulações de variáveis teste
#   global c

#   # manipulações de variáveis teste
#   c += 1
#   t.log_interno_cadastro_inicial_usuario({"id": str(c)},datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))


# iniciando o job
sched.start()
