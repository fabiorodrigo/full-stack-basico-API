from pydantic import BaseModel
from typing import List
from model.aluno import Aluno

class AlunoSchema(BaseModel):
    """ Define como um novo aluno a ser cadastrado deve ser representado. """
    nome: str = "João Silva"
    matricula: int =12345
    classe: str = "5ª Série"
    turno: str = "Manhã"
    email: str = "joao.silva@gmail.com"

class AlunoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura para buscar um aluno com base no nome. """
    nome: str = "João Silva"


class ListagemAlunoSchema(BaseModel):
    """ Define como uma listagem de alunos será retornada. """
    alunos: List[AlunoSchema]


def apresenta_alunos(alunos: List[Aluno]):
    """ Retorna uma representação dos alunos seguindo o schema definido. """
    result = []
    for aluno in alunos:
        result.append({
            "nome": aluno.nome,
            "matricula": aluno.matricula,
            "classe": aluno.classe,
            "turno": aluno.turno,
            "email": aluno.email,
            "data_cadastro": aluno.data_cadastro.strftime('%Y-%m-%d %H:%M:%S'),
        })

    return {"alunos": result}


class AlunoViewSchema(BaseModel):
    """ Define como um aluno será retornado. """
    id: int = 1
    nome: str = "João Silva"
    matricula: int = 12345
    classe: str = "5ª Série"
    turno: str = "Manhã"
    email: str = "joao.silva@gmail.com"
    data_cadastro: str = "2024-12-03 14:30:00"


class AlunoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção. """
    message: str
    nome: str


def apresenta_aluno(aluno: Aluno):
    """ Retorna uma representação de um único aluno seguindo o schema definido. """
    return {
        "id": aluno.id,
        "nome": aluno.nome,
        "matricula": aluno.matricula,
        "classe": aluno.classe,
        "turno": aluno.turno,
        "email": aluno.email,
        "data_cadastro": aluno.data_cadastro.strftime('%Y-%m-%d %H:%M:%S'),
    }