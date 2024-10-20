# Projeto de API de livraria

Backend simples de uma API de gestão de livraria

São utilizados nesse projeto:
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [Passlib](https://passlib.readthedocs.io/en/stable/)
- [JWT](https://github.com/GehirnInc/python-jwt)


## Configuração
Defina no seu ambiente a seguinte variável:
```bash
SQLALCHEMY_DATABASE_URL=sqlite:///./my_db.db
```

## Execução
Instale as dependencias
```bash
pip install -r requirements.txt
```

Então, rode com o comando:
```bash
uvicorn main:app --reload
```


## Testes
Instale as dependencias:
```bash
pip install -r requirements-dev.txt
```

Então, rode com o comando:
```bash
pytest
```
