from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Aluno
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
aluno_tag = Tag(name="Aluno", description="Adição, visualização, atualização e remoção de alunos à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/aluno',tags=[aluno_tag],
          responses={"200": AlunoViewSchema, "422": ErrorSchema, "400": ErrorSchema})
def add_aluno(form: AlunoSchema):
    """Adiciona um novo Aluno à base de dados
    
    Retorna uam representação dos alunos registrados.
    """

    aluno = Aluno(
        nome=form.nome,
        matricula=form.matricula,
        classe=form.classe,
        turno=form.turno,
        email=form.email)
    logger.debug(f"Adicionado aluno de nome: '{aluno.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando aluno
        session.add(aluno)
        # efetivando o comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado aluno de nome: '{aluno.nome}'")
        return apresenta_aluno(aluno), 200
    
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Aluno de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar aluno '{aluno.nome}', {error_msg}")
        return {"mesage": error_msg}, 409
    
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao cadastrar o aluno '{aluno.nome}', {error_msg}")
        return {"mesage": error_msg}, 400

@app.get('/alunos', tags=[aluno_tag],
         responses={"200": ListagemAlunoSchema, "404": ErrorSchema})
def get_alunos():
    """Faz a busca por todos os Alunos cadastrados na base de dados
    
    Retorna uma representação da listagem de alunos.
    """

    logger.debug(f"Coletando alunos")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    alunos = session.query(Aluno).all()

    if not alunos:
        # se não há alunos cadastrados
        return{"alunos":[]}, 200
    else:
        logger.debug(f"%d alunos encontrados" %len(alunos))
        #retorna a representação de alunos
        print(alunos)
        return apresenta_alunos(alunos), 200
    

@app.get('/aluno', tags=[aluno_tag],
         responses={"200": AlunoViewSchema, "404": ErrorSchema})
def get_aluno(query: AlunoBuscaSchema):
    """Faz a busca por um Aluno a partir do nome
    
    Retorna uma apresentação dos alunos 
    """
    aluno_nome = query.nome
    logger.debug(f"Coletando dados sobre o aluno #{aluno_nome}")
    #criando conexão com a base
    session = Session()
    #fazendo a busca
    aluno = session.query(Aluno).filter(Aluno.nome == aluno_nome).first()

    if not aluno:
        # se o aluno não for encontrado na base de dados
        error_msg = "Aluno não encontrado na base de dados."
        logger.warning(f"Erro ao buscar aluno '{aluno_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Aluno encontrado: '{aluno.nome}'")
        # retorna a representação do aluno encontrado
        return apresenta_aluno(aluno), 200

@app.delete('/aluno', tags=[aluno_tag],
            responses={"200": AlunoDelSchema, "404": ErrorSchema})
def del_aluno(query: AlunoBuscaSchema):
    """Deleta um Aluno a partir do nome do aluno informado
    
    Retorna uma mensagem de confirmação da remoção
    """

    aluno_nome = unquote(unquote(query.nome))
    print(aluno_nome)
    logger.debug(f"Deletando dados do aluno #{aluno_nome}")
    #criando conexão com a base
    session = Session()
    #fazendo a remoção
    count = session.query(Aluno).filter(Aluno.nome == aluno_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado aluno #{aluno_nome}")
        return {"message": "Aluno removido", "id": aluno_nome}
    else:
        # se o aluno não foi encontrado
        error_msg = "Aluno não encontrado na base de dados."
        logger.warning(f"Erro ao deletar aluno #'{aluno_nome}', {error_msg}")
        return {"message": error_msg}, 404    