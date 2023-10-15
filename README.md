# GoldenRaspbarry

API RESTful para possibilitar a leitura da lista de indicados e vencedores
da categoria Pior Filme do Golden Raspberry Awards.
 Esta API obtem o produtor com maior intervalo entre dois prêmios consecutivos, e o que
obteve dois prêmios mais rápido.

## Estrutura do Projeto

Este projeto foi desenvolvido usando arquitetura MVC e utilizando conseitos de DDD.

```plaintext
goldenRaspberryAwards/
|-- app/
|   |-- __init__.py
|   |-- controllers/
|   |   |-- __init__.py
|   |   |-- filme_controller.py
|   |-- models/
|   |   |-- __init__.py
|   |   |-- filme.py
|   |-- repositories/
|   |   |-- __init__.py
|   |   |-- filme_repository.py
|   |-- services/
|   |   |-- __init__.py
|   |   |-- filme_service.py
|-- data/
|   |-- movielist.csv
|-- dados.db
|-- tests/
|   |-- __init__.py
|   |-- test_filme_controller.py
|-- main.py

