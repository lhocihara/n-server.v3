# ----------------------------------------------------------
# Importação dos módulos padrões
# ----------------------------------------------------------
from flask_json_schema import JsonSchema, JsonValidationError
from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
from bson.objectid import ObjectId
import pymongo
import dns

# ----------------------------------------------------------
# Importação do orquestrador da conexão com BD
# ----------------------------------------------------------
from orquestrador.orquestrador import Orquestrador
# ----------------------------------------------------------
# Importação dos Objetos de tratamento de erros
# ----------------------------------------------------------
from biblioteca_respostas.status_internos import StatusInternos
from biblioteca_respostas.respostas_api import RespostasAPI
# ----------------------------------------------------------
# Importação dos schemas referentes a Empresa
# ----------------------------------------------------------
from schemas.empresa import schemaCadastro

orq = Orquestrador()

# ----------------------------------------------------------
# Definição do Blueprint
# ----------------------------------------------------------
blueprint_empresa = Blueprint("Empresa", __name__)

# ----------------------------------------------------------
# Definição do Subapp e Schema
# ----------------------------------------------------------
app = Flask("Empresa")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
schema = JsonSchema(app)


# ----------------------------------------------------------
# Rotas dos serviços para o APP
# ----------------------------------------------------------
##
# @empresa_blue.route: A rota do endpoint
# @schema.validate: O schema a ser validado durante a requisição
# ----------------------------------------------------------

# ----------------------------------------------------------
# Endpoint de cadastro de empresas [POST]
# ----------------------------------------------------------
@blueprint_empresa.route("/cadastro", methods=['POST'])
@cross_origin()
@schema.validate(schemaCadastro)
def Cadastrar_Empresa():

    empresa_request = request.json

    print("\n[Requisição-POST] /empresa:\n" + str(empresa_request) + "\n")

    try:
        retorno_id = orq.cadastrar_empresa(empresa_request)

        json_retorno = RespostasAPI('Cadastro realizado com sucesso',
                                    {
                                        'segredo': str(retorno_id),
                                        'cnpj': str(empresa_request['cnpj'])
                                    }
                                    ).JSON

        return json_retorno
    except StatusInternos as e:
        return e.errors


# ----------------------------------------------------------
# Endpoint de consulta de empresas [GET]
# ----------------------------------------------------------

@blueprint_empresa.route("/consultar/<segredo>")
@cross_origin()
def Consultar_Empresa(segredo):
    segredo = ObjectId(segredo)
    empresa_request = request.json

    print("\n[Requisição-GET] /Consulta de Empresa: \n" +
          str(empresa_request) + "\n")

    try:
        retorno = orq.verificar_id_empresa(segredo)

        json_retorno = RespostasAPI('Consulta realizada com sucesso',
                                    {
                                        'segredo': str(segredo),
                                        'dados': retorno,
                                    }
                                    ).JSON

        return json_retorno
    except StatusInternos as e:
        return e.errors

# ----------------------------------------------------------
# Endpoint para listar empresas [GET]
# ----------------------------------------------------------


@blueprint_empresa.route("/listar", methods=['GET'])
@cross_origin()
def Listar_Empresa():
    print("\n[Requisição-GET] /Listar de Empresas")

    try:
        retorno = orq.listar_empresas()

        json_retorno = RespostasAPI(
            'Consulta realizada com sucesso', {'empresas': retorno}).JSON

        return json_retorno
    except StatusInternos as e:
        return e.errors
