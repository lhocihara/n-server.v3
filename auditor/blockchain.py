from hashlib import sha256
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

import dns
import urllib.parse

from AESCipher import AESCipher

class Blockchain:

  def __init__(self):
    self.blocks = []

    key_for_md5_aes = '#TCC2019-N2N#'
    self.aes = AESCipher(key_for_md5_aes)

    # Carregando com paramêtros de acesso para desenvolvedor
    usuario_banco = urllib.parse.quote_plus('dev_connect')
    senha_banco = urllib.parse.quote_plus('rgPuzhTgc8HAHFlV')

    # Criando conexão com o MongoDB
    conexao_servidor = MongoClient('mongodb+srv://%s:%s@cluster0-hygoa.gcp.mongodb.net/?retryWrites=true' % (usuario_banco, senha_banco))

    # Instanciando um gerenciador do banco de dados TCC
    self.conexao_bd = conexao_servidor.TCC

    v = self.conexao_bd.HBase.aggregate([
      {
          "$group": {
              "_id": 0,
              "maxQuantity": {"$max": "$timestamp"}
          }
      }
      ])

    print("oi oi")

    self.set_genesis_block()

  def set_genesis_block(self):
    first_transaction = [
      {
        "tipo_log": "log_inicial"
      }
    ] 

    self.hash_block_and_send(first_transaction)

  def hash_block_and_send(self, transactions):
    transactions = self.aes.encrypt(transactions)

    timestamp = datetime.utcnow().timestamp()
    prev_hash = self.get_last_hash()
    index = self.get_blockchain_length()

    block_formatted = {
      'transactions': transactions, 'timestamp': timestamp, 'prev_hash': prev_hash, 'index': index
    }

    block_string = '{}'.format(
      block_formatted
    )
    
    datatime = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    hash = sha256(block_string.encode()).hexdigest()

    self.blocks.append(hash)

    # self.conexao_bd.HBase.insert(block_formatted)

    print("\n bloco criado às " + datatime + " " + str(timestamp))


  def add_new_block(self, transactions):
    self.hash_block_and_send(transactions)

  def get_last_hash(self):
      return self.blocks[-1] if (len(self.blocks) > 0) else "initial"

  def get_blockchain_length(self):
      return len(self.blocks)


  # def is_hash_valid(self,hash):
  #     return hash.startswith('0000')

  def get_all(self):
      return self.blocks[:]