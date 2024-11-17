Eventhub

Eventhub é uma plataforma de gerenciamento de eventos e vendas de ingressos desenvolvida com o framework Django e Bootstrap para o design do front-end.
Recursos Principais

Com o Eventhub, os usuários podem:

    Explorar e Pesquisar Eventos
    Os usuários podem navegar por uma lista de eventos futuros, buscar eventos específicos e visualizar informações detalhadas, como opções de ingressos, data, horário e local.

    Criar Eventos com Opções de Ingressos Personalizadas
    Organizadores podem criar eventos, definir diferentes opções de ingressos com preços variados e estabelecer uma taxa base de participação. Imagens de eventos enviadas são armazenadas com identificadores únicos.

    Interagir com Eventos
        Demonstrar Interesse: Os usuários podem marcar interesse nos eventos.
        Comprar Ingressos: Ingressos podem ser selecionados e adquiridos, com o cálculo em tempo real do custo total com base nas opções e quantidades escolhidas.

Tecnologias Utilizadas

    Backend: Django (Python)
    Frontend: HTML, CSS, JavaScript (com Bootstrap)
    Banco de Dados: Django ORM (compatível com bancos como SQLite, PostgreSQL, etc.)
    API: Django REST Framework (DRF) para gerenciamento de eventos.

Funcionalidades

    Exploração de Eventos:
        Visitantes podem explorar eventos disponíveis na página inicial ou acessar informações detalhadas de eventos específicos.

    Criação de Eventos:
        Usuários registrados e logados podem criar eventos, configurar opções de ingressos personalizadas e enviar imagens para ilustrar o evento.

    Compra de Ingressos:
        Os usuários podem escolher a opção de ingresso desejada e a quantidade. O sistema calcula automaticamente o custo total.

    Recursos em AJAX:
        Interações como marcar interesse em um evento ou calcular o custo total dos ingressos são feitas dinamicamente, sem recarregar a página.