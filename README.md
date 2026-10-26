# ATV09 — Portal da Dupla

## Identificação

**Integrantes:** Gabriele Adla Barbosa da Silva e Thayse Soares Cordeiro  
**Turma:** 513  
**Instituição:** IFAL — Campus Palmeira dos Índios  
**Curso:** Técnico em Informática

## Descrição do projeto

Este projeto corresponde à ATV09 — Migração do Portal para Django.

O portal desenvolvido anteriormente na ATV06 foi adaptado para utilizar o framework Django, mantendo a identidade visual, a estrutura do layout, as imagens, o HTML semântico, o CSS e a responsividade.

A navegação e os conteúdos passaram a ser administrados pelo Django Admin.

## Tecnologias utilizadas

- Python
- Django
- HTML5
- CSS3
- JavaScript
- SQLite
- Git
- GitHub

## Estrutura principal

O projeto utiliza:

- **Model Conteudo:** armazena título, slug, conteúdo HTML e status de ativação.
- **Model Menu:** armazena os itens da navegação, sua ordem, tipo de destino, conteúdo relacionado e URLs externas.
- **Django Admin:** utilizado para cadastrar e alterar conteúdos e itens do menu.
- **Templates Django:** responsáveis pela estrutura das páginas.
- **Arquivos estáticos:** utilizados para armazenar CSS e imagens.
- **URLs e Views:** responsáveis pela navegação e apresentação dos conteúdos.

## Ambiente virtual

Para criar um ambiente virtual:

```bash
python3 -m venv myworld
```

Para ativar no Linux:

```bash
source myworld/bin/activate
```

## Instalação do Django

Com o ambiente virtual ativado:

```bash
pip install django
```

## Migrations

Para criar as migrations:

```bash
python manage.py makemigrations
```

Para aplicar as migrations:

```bash
python manage.py migrate
```

## Criar superusuário

Para criar um usuário administrador:

```bash
python manage.py createsuperuser
```

Depois, informe o nome de usuário, e-mail e senha solicitados.

## Executar o servidor

Com o ambiente virtual ativado:

```bash
python manage.py runserver
```

## Acesso à aplicação

No navegador, acesse:

```text
http://127.0.0.1:8000/
```

## Acesso ao Django Admin

No navegador:

```text
http://127.0.0.1:8000/admin/
```

No Django Admin é possível cadastrar, alterar, excluir, ativar, desativar e organizar os conteúdos e itens do menu.

## Conteúdos do portal

O portal possui conteúdos internos cadastrados no Django Admin, incluindo:

- Início
- Currículo Gabriele
- Fúria da Luz
- Currículo Thayse
- Attack on Titan

Também possui links externos para:

- GitHub
- W3Schools

## Navegação dinâmica

O menu é obtido a partir dos registros cadastrados no Model `Menu`.

Os itens internos utilizam as URLs do Django e o `slug` do Model `Conteudo`.

Os itens externos utilizam a URL cadastrada no Django Admin.

Dessa forma, alterações realizadas no Django Admin podem ser refletidas no menu do portal sem precisar alterar manualmente os itens da navegação no HTML.

## Repositório GitHub

Repositório do projeto:

https://github.com/adla08/my_tennis_club
