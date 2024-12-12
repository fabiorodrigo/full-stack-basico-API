# Sistema de Gestão Escolar - Modulo Back-end

**Pós-Graduação em Engenharia de Software da PUC-Rio**.

### **Informações do Projeto**
- **Disciplina:** Desenvolvimento Full Stack Básico
- **Aluno:** Fabio Araújo  
- **Data de Conclusão:** Dezembro de 2024  


O objetivo do projeto é implementar uma API para o gerenciamento de alunos, incluindo funcionalidades de cadastro, consulta, atualização e exclusão. Este backend foi desenvolvido em Python, utilizando **Flask** e segue os princípios básicos de desenvolvimento de APIs.

---

## **Estrutura do Projeto**
Abaixo está a estrutura principal do projeto:

```plaintext
.
├── app.py                 # Arquivo principal para execução da API
├── schemas/               # Definição dos schemas Pydantic
├── model/                 # Modelos de dados (SQLAlchemy)
├── logger.py              # Configuração de logs
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```
## **Como Executar**
Pré-requisitos
Python 3.8+ instalado: Certifique-se de que o Python esteja instalado em sua máquina.<br/>
Ambiente virtual (opcional, mas recomendado): Utilize virtualenv ou venv para gerenciar dependências de forma isolada.<br/>

**Passo a Passo:**

**1. Clonar o Repositório**
```
git clone https://github.com/fabiorodrigo/gestao_escolar_api.git
cd gestao_escolar_api
```
**2. Criar e Ativar o Ambiente Virtual (opcional)**
```
python -m venv env
source env/bin/activate   # Linux/MacOS
env\\Scripts\\activate      # Windows
```
**3. Instalar as Dependências**<br/>
Instale as bibliotecas necessárias listadas no arquivo requirements.txt:
```
pip install -r requirements.txt
```
**4. Executar a API**<br/>
Para iniciar o servidor da API, utilize o comando:
```
flask run --host 0.0.0.0 --port 5003
```
**5. Modo Desenvolvimento (opcional)**<br/>
Para facilitar o desenvolvimento, utilize o parâmetro --reload, que reinicia o servidor automaticamente ao detectar alterações no código:
```
flask run --host 0.0.0.0 --port 5003 --reload
```
**6. Testar a API**<br/>
Abra o navegador e acesse:
```
http://localhost:5003/#/
```


## **Funcionalidades Implementadas**

A API oferece os seguintes endpoints:

- **GET /alunos**
  Lista todos os alunos cadastrados.

- **POST /aluno**
  Adiciona um novo aluno ao banco de dados.

- **GET /aluno?nome=**
  Consulta os detalhes de um aluno específico pelo nome.

- **DELETE /aluno?nome=**
  Remove um aluno do banco de dados pelo nome.

## **Tecnologias Utilizadas**

O projeto utiliza as seguintes bibliotecas e frameworks:

- **Flask (2.1.3):** Framework web para criar APIs de maneira rápida e eficiente.
- **Flask-Cors (3.0.10):** Gerencia permissões de requisições cross-origin, permitindo que a API seja consumida por diferentes origens.
- **Flask-OpenAPI3 (2.1.0):** Ferramenta para gerar documentação interativa da API, seguindo o padrão OpenAPI 3.
- **Flask-SQLAlchemy (2.5.1):** Extensão do SQLAlchemy para integração com o Flask, facilitando o uso de ORM.
- **Pydantic (1.10.2):** Ferramenta para validação de dados e criação de schemas.
- **SQLAlchemy (1.4.41):** ORM robusto para interagir com bancos de dados relacionais.
- **SQLAlchemy-Utils (0.38.3):** Conjunto de extensões adicionais para o SQLAlchemy.
- **Typing-Extensions (4.3.0):** Suporte para anotações de tipo estendidas em Python.
- **Werkzeug (2.0.3):** Biblioteca WSGI utilizada pelo Flask para lidar com requisições HTTP.


## **Contribuição**
Este repositório foi desenvolvido como parte de um trabalho acadêmico.<br/> 
Contribuições são bem-vindas para fins educacionais ou de aprendizado!! <br/>
Sinta-se à vontade para abrir issues ou enviar pull requests =)


  
