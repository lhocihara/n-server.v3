from datetime import datetime

class Tipos_Transacoes:
  def __init__(self):
    self.transacoes = []

  # --------------------------------------------------------------------------
  # Logs acionados por acões em sistemas da aplicação
  # --------------------------------------------------------------------------
  def log_interno_cadastro_inicial_usuario(self, id_usuario, t = ""):
    """Utilizada para registrar logs de cadastro inicial dos usuários.

    `param id_usuario` - recebe o valor em string do ObjectId do documento que foi inserido dentro da collection de Pessoa.
    """
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "interno_cadastro_inicial",
      "id_usuario": id_usuario,
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_interno_login_usuario(self, id_usuario, t = ""):
    """Utilizada para registrar logs do]e login dos usuários nas soluções internas.
    
    `param id_usuario` - recebe o valor em string do ObjectId do documento dentro da collection de Pessoa que está logando.
    """
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "login_interno_usuario",
      "id_usuario": id_usuario,
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_interno_consulta_dados_usuario(self, id_usuario, t = ""):
    """Utilizada para registrar logs de consulta dos dados dos usuários nas soluções internas.
    
    `param id_usuario` - recebe o valor em string do ObjectId do documento dentro da collection de Pessoa que está sendo consultado.
    """
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "interno_consulta_dados_usuario",
      "id_usuario": id_usuario,
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_adicao_dados_usuario(self, id_usuario, campos_adicionados, t = ""):
    """Utilizada para registrar logs de adição de dados dos usuários.
    
    `param id_usuario` - recebe o valor em string do ObjectId do documento dentro da collection de Pessoa que está efetuando a adição de dados.
    
    `param campos_adicionados` - recebe a lista com o nome dos campos que o usuário, apontado por `id_pessoa`, adicionou.
    """
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "adicao_dados_usuario",
      "id_usuario": id_usuario,
      "campos_adicionados": campos_adicionados,
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_alteracao_dados_usuario(self, id_usuario, campos_alterados, t = ""):
    """Utilizada para registrar logs de edição dos dados de usuário.
    
    `param id_usuario` - recebe o valor em string do ObjectId do documento dentro da collection de Pessoa que está efetuando a alteração de dados.
    
    `param campos_alterados` - recebe a lista com o nome dos campos que o usuário, apontado por `id_pessoa`, alterou.
    """
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "alteracao_dados_usuario",
      "id_usuario": id_usuario,
      "campos_alterados": campos_alterados,
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_exclusao_dados_usuario(self, id_usuario, campos_excluidos, t = ""): 
    """Utilizada para registrar logs de exclusões de dados do usuário.
    
    `param id_usuario` - recebe o valor em string do ObjectId do documento dentro da collection de Pessoa que está efetuando a exclusão de dados.
    
    `param campos_excluidos` - recebe a lista com o nome dos campos que o usuário, apontado por `id_pessoa`, excluiu.
    """
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "exclusao_dados_usuario",
      "id_usuario": id_usuario,
      "campos_excluidos": campos_excluidos,
      "datetime": timestamp_do_evento
    } 
    self.transacoes.append(formato_log)

  def log_solicitacao_exclusao_usuario(self, id_usuario, data_vencimento, t = ""):
    """Utilizada para registrar logs das solicitações de exclusão de conta.
    
    `param id_usuario` - recebe o valor em string do ObjectId do documento dentro da collection de Pessoa que está solicitando a exclusão de conta.
    
    `param data_vencimento` - recebe a última data em que o usuário poderá decidir se irá excluir totalmente os seus dados pessoais.
    """
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "solicitacao_exclusao_usuario",
      "id_usuario": id_usuario,
      "data_vencimento": data_vencimento,
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_cancelamento_exclusao_usuario(self, id_usuario, data_camcelamento, t = ""):
    """Utilizada para registrar logs do cancelamento de exclusão do usuário.
    
    `param id_usuario` - recebe o valor em string do ObjectId do documento dentro da collection de Pessoa que está cancelando a exclusão de conta.
    
    `param data_vencimento` - recebe a última data em que o usuário poderá decidir se irá excluir totalmente os seus dados pessoais.
    """
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "cancelamento_exclusao_usuario",
      "id_usuario": id_usuario,
      "data_camcelamento": data_camcelamento,
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_confirmacao_exclusao_usuario(self, id_usuario, data_exclusao, t = ""):
    """Utilizada para registrar logs do login dos usuários nas soluções internas.
    
    `param id_usuario` - recebe o valor em string do ObjectId do documento dentro da collection de Pessoa que havia solicitado a exclusão e que a partir de agora não terá mais acesso a conta.
    
    `param data_exclusao` - recebe a data em que os dados do usuário foram excluídos
    """
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "confirmacao_exclusao_usuario",
      "id_usuario": id_usuario,
      "data_exclusao": data_exclusao,
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_interno_criacao_vinculo(self, id_usuario, id_projeto, id_vinculo, t = ""):
    """Utilizada para registrar logs de criação de vínculo de pessoa com parceiros.
    
    `param id_usuario` - recebe o valor em string do ObjectId do documento dentro da collection de Pessoa que está no vínculo.
    
    `param id_projeto` - recebe o valor em string do ObjectId do documento dentro da collection de Projetos que está no vínculo.
    
    `param id_vinculo` - recebe o valor em string do ObjectId do documento dentro da collection de PessoaProjetos que está no vínculo, ele é o vínculo entre `id_usuario` e `id_projeto`.
    """
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "interno_criacao_vinculo",
      "id_usuario": id_usuario,
      "id_projeto": id_projeto,
      "id_vinculo": id_vinculo,
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_interno_exclusao_vinculo(self, id_usuario, id_projeto, id_vinculo, t = ""):
    """Utilizada para registrar logs de exclusão de vínculo de pessoa com parceiros.
    
    `param id_usuario` - recebe o valor em string do ObjectId do documento dentro da collection de Pessoa que está no vínculo.
    
    `param id_projeto` - recebe o valor em string do ObjectId do documento dentro da collection de Projetos que está no vínculo.
    
    `param id_vinculo` - recebe o valor em string do ObjectId do documento dentro da collection de PessoaProjetos que está no vínculo, ele é o vínculo entre `id_usuario` e `id_projeto`.
    """
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "interno_exclusao_vinculo",
      "id_usuario": id_usuario,
      "id_projeto": id_projeto,
      "id_vinculo": id_vinculo,
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)


  # --------------------------------------------------------------------------
  # Logs acionados por acões em sistemas externos a aplicação
  # --------------------------------------------------------------------------
  def log_externo_login_usuario(self, id_usuario, id_projeto, id_vinculo, t = ""):
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "externo_login_usuario",
      "id_usuario": id_usuario,
      "id_projeto": id_projeto,
      "id_vinculo": id_vinculo,
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_externo_consulta_dados_usuario(self, id_usuario, id_projeto, id_vinculo,campos_consultados, t = ""):
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "externo_consulta_dados_usuario",
      "id_usuario": id_usuario,
      "id_projeto": id_projeto,
      "id_vinculo": id_vinculo,
      "campos_consultados": campos_consultados,
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_externo_criacao_vinculo(self, id_usuario, id_projeto, id_vinculo, t = ""):
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "externo_criacao_vinculo",
      "id_usuario": id_usuario,
      "id_projeto": id_projeto,
      "id_vinculo": id_vinculo,
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)

  def log_externo_exclusao_vinculo(self, id_usuario, id_projeto, id_vinculo, t = ""):
    timestamp_do_evento = t if t != "" else datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    formato_log = {
      "tipo_log": "externo_exclusao_vinculo",
      "id_usuario": id_usuario,
      "id_projeto": id_projeto,
      "id_vinculo": id_vinculo,
      "datetime": timestamp_do_evento
    }
    self.transacoes.append(formato_log)