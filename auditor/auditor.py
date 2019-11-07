from apscheduler.schedulers.blocking import BlockingScheduler

from orquestrador.orquestrador import lista_transc
from blockchain import Blockchain

sched = BlockingScheduler()
blch = Blockchain()

@sched.scheduled_job('interval', seconds = 10)
def job_atualizador():
  print("\n\nJob adição de bloco\n-------------")
    # verifica se há transações para serem armazenadas no bloco, caso não tiver, não há necessidade de criar um novo bloco.
  if (len(lista_transc.transacoes)):
      # criando variável temporaria para receber os dados que entrarão neste bloco atual e preparando a lista para as próximas transações
    transacoes_temp = lista_transc.transacoes
    lista_transc.reset()
    print("Qtd. transações encontradas: " + str(len(transacoes_temp)))
    # Adicionando um novo bloco à chain
    blch.add_new_block(transacoes_temp)

  else:
    # Informando que a lista de transções está vazia
    print("Lista de transações atuais está vazia...")


# @sched.scheduled_job('interval', seconds = 2)
# def job_tester():
#     print("Testando...")
#     lista_transc.log_interno_cadastro_inicial_usuario("Teste")

# iniciando o job
sched.start()