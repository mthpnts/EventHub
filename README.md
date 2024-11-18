# ![logo](https://github.com/user-attachments/assets/06b719c9-d837-4a2d-8811-204433ce40d9)

**Eventhub** é um sistema de gerenciamento de eventos e vendas de ingressos, desenvolvido utilizando o framework Django e o Bootstrap. O sistema permite que usuários possam criar, visualizar e interagir com eventos, além de realizar a compra de ingressos para eventos de interesse. Projeto Integrador para o Eixo de Computação da Universidade Virtual do Estado de São Paulo (UNIVESP). 

---

## Funcionalidades

O **Eventhub** oferece as seguintes funcionalidades:

- **Exibição de Eventos**: Usuários podem visualizar e buscar eventos disponíveis.
- **Criação de Eventos**: Organize seus próprios eventos, com a opção de definir diferentes tipos de ingressos e preços.
- **Compra de Ingressos**: Compradores podem adquirir ingressos para eventos disponíveis, de forma simples e rápida.
- **Gestão de Eventos**: Como organizador, você pode gerenciar seus eventos criados, incluindo detalhes como data, horário, descrição e ingressos.
- **Sistema de Autenticação**: Usuários podem se registrar, fazer login e acessar suas contas para gerenciar eventos e comprar ingressos.
  
---

## Tecnologias Utilizadas

O sistema foi desenvolvido utilizando as seguintes tecnologias:

- **Backend**: [Django](https://www.djangoproject.com/) - Framework web de alto nível para o desenvolvimento de aplicações web rápidas e seguras.
- **Frontend**: [Bootstrap](https://getbootstrap.com/) - Framework front-end para construção de interfaces responsivas.
- **Banco de Dados**: SQLite (para desenvolvimento) - Sistema de gerenciamento de banco de dados leve, utilizado para persistência de dados.
  
---

## Como Rodar o Projeto

### 1. Pré-requisitos

Certifique-se de que você tenha o Python 3.8 ou superior instalado na sua máquina. Você pode verificar sua versão do Python com o seguinte comando:

```bash
python --version
```


Além disso, será necessário instalar o Django. Para isso, execute:

```bash
pip install django
```

2. Clonando o Repositório

Primeiramente, clone o repositório para o seu computador:

git clone https://github.com/mthpnts/eventhub.git

3. Instalando Dependências

Dentro do diretório do projeto, instale as dependências necessárias utilizando o pip:

pip install -r requirements.txt

4. Configuração do Banco de Dados

Após a instalação das dependências, é necessário migrar as tabelas para o banco de dados:

python manage.py migrate

5. Criando um Superusuário (Admin)

Para acessar o painel administrativo do Django, crie um superusuário com o comando:

python manage.py createsuperuser

Siga as instruções para definir o nome de usuário, e-mail e senha.
6. Rodando o Servidor

Agora, você pode rodar o servidor de desenvolvimento:

python manage.py runserver

Acesse o sistema no navegador através do endereço:

http://127.0.0.1:8000/

Para acessar a área administrativa, vá até:

http://127.0.0.1:8000/admin/
