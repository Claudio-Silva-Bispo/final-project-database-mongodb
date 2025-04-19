# final-project-database-mongodb

O projeto simula um cenário real de negócios, com ênfase na criação de soluções escaláveis, testáveis e alinhadas às exigências do mercado atual de desenvolvimento corporativo com MongoDb.

## Título do Projeto

Sistema Inteligente de Agendamento de Consultas com Sugestões Baseadas em IA

## Descrição do Projeto

O projeto visa desenvolver uma solução integrada composta por duas aplicações: uma aplicação móvel, gerenciada em Java e React Native, e uma aplicação web, desenvolvida em ASP.NET / C#. O objetivo central do sistema é sugerir consultas ideais para clientes, considerando:

**Localidade de preferência do cliente**

**Dia e turno disponíveis**

**Feedbacks das clínicas e especialistas**

**Menores custos**

A aplicação utilizará inteligência artificial (IA) para identificar padrões e recomendar as melhores opções de agendamento de consultas, promovendo um ciclo contínuo de atendimento com qualidade.

Além disso, será implementado um programa de relacionamento, no qual clientes e especialistas contribuem com feedbacks e conteúdos, possibilitando o treinamento contínuo do modelo de IA, enquanto acumulam pontos e recompensas.

## Justificativa para o uso do MongoDB (Banco NoSQL)

A escolha do MongoDB como banco de dados NoSQL se justifica pelas seguintes razões:

**Flexibilidade de Estrutura** 

O MongoDB armazena dados em documentos JSON-like (BSON), permitindo modelar entidades complexas (como usuários, agendamentos, feedbacks) de forma flexível e sem a rigidez de esquemas fixos.

**Escalabilidade Horizontal** 

A aplicação terá um potencial grande de crescimento com muitos usuários e feedbacks. MongoDB permite escalabilidade horizontal, essencial para atender grande volume de dados.

**Desempenho em Leitura e Escrita** 

Consultas rápidas e alta performance para leitura/escrita de documentos são fundamentais para o sistema de recomendações em tempo real.

**Facilidade de Integração** 

MongoDB possui drivers compatíveis com Java, C# e bibliotecas de IA, facilitando a integração entre back-end, mobile, e os algoritmos de inteligência artificial.

**Armazenamento de Dados Semiestruturados** 

Ideal para armazenar dados de feedback, preferências personalizadas de usuários e registros de interação, que não seguem uma estrutura fixa e podem variar por usuário.

# Modelo de Dados e Justificativas

Abaixo está a modelagem dos principais documentos do sistema, estruturados de forma que aproveitem a flexibilidade do MongoDB. Cada coleção representa uma entidade essencial para o funcionamento do sistema:

## 🧑 Coleção: clientes

**✅ Justificativa** 

A estrutura permite armazenar preferências específicas de cada cliente, como disponibilidade e localização, em um único documento. Isso é ideal para consultas rápidas baseadas em preferências.

```bash
  [
      {
          "cliente_id": "1",
          "nome": "João Silva",
          "email": "joao@email.com",
          "telefone": "11999999999",
          "cpf": "12345678901",
          "endereco_preferencia": {
            "estado": "SP",
            "cidade": "São Paulo",
            "bairro": "Centro",
            "rua": "Rua das Flores",
            "cep": "01001-000"
          },
          "dias_disponiveis": ["Segunda", "Quarta", "Sexta"],
          "turno_disponivel": "Manhã",
          "horario_disponivel": "18:00",
          "nivel_participacao": 4,
          "pontos_acumulados": 150,
          "ativo": true,
          "perfil": "Comum",
          "senha": "123456"
      }
  ]

```

## 🏥 Coleção: clinicas

**✅ Justificativa** 

Permite consultar clínicas com base na localidade, especialidade e avaliação. Ideal para sistemas de recomendação com IA.

```bash
    {
        "clinica_id": "1",
        "nome": "Clínica OdontoMais",
        "especialidades": ["1", "2"],
        "cnpj": "1234567811000150",
        "dias_disponiveis": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"], 
        "turno_disponivel": ["Manhã", "Tarde"], 
        "horario_disponivel": ["08:00", "14:00", "18:00"],
        "localizacao": 
        {
            "estado": "SP",
            "cidade": "Campinas",
            "bairro": "Taquaral",
            "cep": "05720333",
            "rua": "Rua Teste, 20"
        },
        "avaliacao_media": 4.8,
        "quantidade_feedbacks": 125,
        "custo_medio": 90.00,
        "parceira": true,
        "dentistas": 
        [
            {
            "dentista_id": "1",
            },
            {
            "dentista_id": "5",
            }

        ]
    }
```

## 🩺 Coleção: dentista

**✅ Justificativa** 

Ter os dentistas em uma coleção separada permite cruzar facilmente dados como especialidade, avaliação, disponibilidade e performance (ex: total de atendimentos) — fundamentais para a IA sugerir profissionais adequados.

```bash
    {
        "clinica_id": "1"
        "dentista_id": "1",
        "nome": "Dra. Juliana Fernandes",
        "especialidade_id": "1",
        "crm": "SP-54321",
        "email": "juliana.fernandes@clinicakids.com",
        "telefone": "(11) 99999-1234",
        "avaliacoes": 4.8,
        "total_consultas": 215,
        "disponibilidade": [
          { "dia": "Segunda", "turno": "Manhã" },
          { "dia": "Quarta", "turno": "Tarde" }
        ],
        "ativo": true
    }
```

## 🧑‍⚕️ Coleção: especialidade

**✅ Justificativa** 

Conectado à clínica e com disponibilidade própria de suas especialidades, o que permite cruzar dados para oferecer as melhores sugestões ao cliente pensando na clinica, dentistas e especialidades.

```bash
    {
        "especialidade_id": "1",
        "especialidade": "Ortodontia",
    }
```

## 🧠 Coleção: sugestoes_para_clinica

**✅ Justificativa**

Permite registrar que a IA sugeriu algo com base nos dados e aguarda resposta da clínica, o que é essencial antes de notificar o cliente.

```bash
    {
        "sugestao_clinica_id": "1",
        "cliente_id": "1",
        "clinica_id": "1",
        "dentista_id": "1",
        "especialidade_id": "1",
        "data_sugerida": "2025-04-25",
        "turno": "Manhã",
        "motivo_sugestao": "Limpeza",
        "status_clinica": "Pendente",
        "data_envio": "2025-04-18"
    }
```

## 📩 Coleção: sugestoes_para_cliente

**✅ Justificativa** 

Permite controlar a resposta do cliente à sugestão feita pela clínica. Se for aceita, podemos gerar um agendamento. Se recusada, pode-se armazenar o motivo e alimentar o sistema de IA com esse feedback.

```bash
    {
        "sugestao_cliente_id": "1",
        "cliente_id": "1",
        "clinica_id": "1",
        "dentista_id": "1",
        "especialidade_id": "1",
        "data_sugerida": "2025-04-25",
        "turno_sugerido": "Manhã",
        "horario_sugerido": "09:00",
        "status_clinica": "Aceito", 
        "status_cliente": "Pendente", 
        "validade": "2025-04-22",
        "data_envio": "2025-04-18",
        "data_alteracao": "2025-04-21",
        "motivo_sugestao": "Prevencao"
    }
```

## 📅 Coleção: agendamentos

**✅ Justificativa** 

Armazena os agendamentos de forma eficiente. Pode ser facilmente consultado por cliente, especialista, ou período. Isso não é a consulta ainda.

```bash
    {
        "agendamento_id": "1",
        "cliente_id": "1",
        "clinica_id": "1",
        "dentista_id": "6",
        "especialidade": "3",
        "data": "2025-04-25",
        "turno": "Manhã",
        "horario": "14:00",
        "status": "Confirmado",
        "tipo_consulta": "Rotina de Prevenção",
    }
```

## 📅 Coleção: consultas

**✅ Justificativa**

Essa coleção representa a consulta oficial. Ela será vinculada ao resultado_consultas após a execução. Também pode ser usada em relatórios, histórico do cliente, e controle da agenda da clínica e do especialista.

```bash
    {
        "consulta_id": "1",
        "cliente_id": "2",
        "clinica_id": "3",
        "dentista_id": "4",
        "especialidade_id": "4",
        "data": "2025-04-25",
        "horario": "09:00",
        "turno": "Manhã",
        "tipo_consulta": "Limpeza",
        "status": "Confirmada", // Pode ser "Confirmada", "Cancelada", "Realizada"
        "foi_remarcada": false,
        "confirmacao_cliente": true,
        "confirmacao_clinica": true,
        "criado_em": "2025-04-19",
        "feedback_id": "1"
    }
```

## ⭐ Coleção: feedbacks

**✅ Justificativa** 

Permite gerar notas médias, análise de sentimentos e alimentar o sistema de IA com dados reais dos usuários. As pesquisas serão respondidas pelos clientes apenas.

```bash
    {
        "feedback_id": "1",
        "cliente_id": "2",
        "clinica_id": "1",
        "dentista_id": "3",
        "nota": 5,
        "comentario": "Excelente atendimento! Dentista só precisa ter mais atenção.",
        "data_feedback": "2025-04-10"
    }
```

## 📝 Coleção: resultados_consultas

**✅ Justificativa** 

Essa estrutura é a base para decisões preditivas, como:

**1. frequência ideal de retorno**

**2. se deve sugerir retorno com o mesmo médico ou outro**

**3. se o problema persiste**

**4. se há padrão de reclamações/sintomas**

```bash
    {
      "resultado_id": "1",  
      "agendamento_id": "1",
      "cliente_id": "2",
      "clinica_id": "1",
      "dentista_id": "3",
      "diagnostico": "Gengivite",
      "recomendacoes": "Uso de enxaguante bucal e retorno em 30 dias",
      "medicamentos_prescritos": ["Enxaguante bucal Clorexidina"],
      "retorno_sugerido_em": "2025-05-25",
      "avaliacao_clinica": "Ótima infraestrutura, mas atraso de 10 minutos",
      "sintomas_relatados": ["Gengiva sangrando", "Sensibilidade"],
      "data_resultado": "2025-04-25"
    }
```


## 🎁 Coleção: desafios_participacao

**✅ Justificativa** 

Suporta o programa de relacionamento e gamificação, com tracking dos usuários que participam.

```bash
    {
        "desafio_id": "1",
        "titulo": "Complete seu cadastro",
        "descricao": "Preencha todos os dados do perfil",
        "pontos": 20,
        "status": "concluido"
    }
```

## 📁 Coleção: t_notificacoes_usuario

**✅ Justificativa** 

Armazena notificações direcionadas a cada usuário sobre agendamentos, feedbacks, atualizações ou alertas gerais.

```bash
    {
        cliente_id: "1",  
        agendamento_id: "1",               
        tipo: "agendamento",                 
        titulo: "Confirmação de agendamento",
        mensagem: "Sua consulta está confirmada para o dia 24/04 às 14h.",
        dataCriacao: Timestamp.now(),
        lida: false
    }
```

## 📁 Coleção: t_interacoes_ia_chatbot

**✅ Justificativa** 

Armazena interações do usuário com a inteligência artificial para análise e melhorias do sistema.

```bash
    {
        cliente_id: "abc123",                
        mensagemUsuario: "Quais horários estão disponíveis?",
        respostaIA: "Você pode agendar para terça às 10h ou quarta às 16h.",
        dataHora: Timestamp.now(),
        tipoInteracao: "pergunta",            // 'pergunta' | 'formulario' | 'recomendacao' | 'outro'
        contextoRelacionado: "agendamento"    // Ex: 'cadastro', 'feedback', etc. (opcional)
    }
```

## Criar 10 documentos para cada Coleção

Será criada a estrutura dos dados e os documentos serão inseridos via importação no terminal.

Vamos elaborar um arquivo .json contendo 10 documentos, cada um com 10 atributos, simulando dados realistas. Isso servirá para testes e desenvolvimento. O modelo permitirá a importação dos arquivos .json diretamente na pasta do projeto. Após a importação, será possível consultar os dados enviados diretamente na interface.

## Importação e Consulta de Dados JSON no MongoDB

Este projeto foi desenvolvido utilizando Flask (para o backend) e MongoDB (como banco de dados), com o objetivo de permitir a importação de arquivos JSON para diferentes coleções do MongoDB e também a consulta desses dados diretamente por meio de uma interface web simples.

# Funcionalidades

**1. Importação de Arquivo JSON para MongoDB**

O usuário pode selecionar um arquivo JSON e escolher a coleção do MongoDB onde deseja importar os dados.

O arquivo JSON pode ser importado tanto para uma coleção única quanto para várias coleções, com base na estrutura do arquivo.

Após selecionar o arquivo e a coleção desejada, basta clicar no botão "Importar", e os dados do arquivo JSON serão enviados e inseridos na coleção escolhida.

O arquivo JSON deve estar em formato adequado para ser inserido no MongoDB (ou como um único documento ou como uma lista de documentos).

**2. Consulta de Dados nas Coleções**

O usuário pode escolher uma coleção específica do MongoDB e consultar todos os documentos presentes nela.

Após selecionar a coleção desejada e clicar em "Consultar", todos os documentos presentes nessa coleção serão exibidos em uma tabela.

A tabela exibe os campos de cada documento como cabeçalhos e os respectivos valores nas linhas abaixo, facilitando a visualização e análise dos dados.

# Estrutura de Funcionamento

## Backend (Flask)

O backend foi desenvolvido utilizando o framework Flask, que gerencia as rotas e as interações com o banco de dados MongoDB.

**Conexão com o MongoDB** 

Utiliza o driver PyMongo para conectar ao banco de dados MongoDB e inserir ou consultar dados nas coleções.

***Rotas***

/ (Rota Principal): Exibe a interface para o usuário, permitindo tanto a importação de arquivos JSON quanto a consulta dos dados.

**Método POST (Importação)** 

Quando um arquivo JSON é enviado, os dados são carregados e inseridos na coleção escolhida.

**Método POST (Consulta)** 

Quando uma coleção é selecionada, os documentos dessa coleção são consultados e exibidos na interface.

## Frontend (HTML):

O frontend foi desenvolvido utilizando HTML simples, com formulários para a importação de arquivos JSON e a seleção de coleções para consulta.

Seleção de Coleção para Importação: O usuário pode escolher entre várias coleções (como t_cliente, t_clinica, t_dentista, entre outras) para importar os dados JSON.

Seleção de Coleção para Consulta: O usuário pode selecionar a coleção desejada e visualizar todos os documentos contidos nela em formato de tabela.

**Exibição de Dados:** 

A tabela é gerada dinamicamente, com os campos dos documentos sendo exibidos como cabeçalhos e os dados preenchendo as células.

**Tecnologias Utilizadas**

**Flask**

Framework para criação de aplicativos web.

**PyMongo** 

Driver Python para interagir com o MongoDB.

**MongoDB** 

Banco de dados NoSQL utilizado para armazenar os dados.

**HTML** 

Para a criação da interface web.

# Como Rodar o Projeto

**Instalar Dependências** 

Para rodar o projeto localmente, você precisará de um ambiente Python com as dependências necessárias instaladas. Execute o comando abaixo para instalar as dependências:

```bash
    pip install flask pymongo
```

**Executar o Servidor Flask** 

Após instalar as dependências, execute o servidor Flask:

```bash
    python app.py
```

**Acessar a Interface Web** 

Abra o navegador e acesse a interface em http://127.0.0.1:5000/ para importar arquivos JSON ou consultar dados nas coleções. Assim como na exportação do json ou CRUD.

## Observações

O MongoDB está configurado para se conectar via MongoDB Atlas. Certifique-se de substituir o URL de conexão pelo seu próprio string de conexão do MongoDB, caso não esteja utilizando o MongoDB Atlas.

O formato do arquivo JSON enviado deve estar correto para ser inserido nas coleções. Arquivos mal formatados podem resultar em erros durante o processo de importação.


## Análise de Performance e Escalabilidade

A análise de performance e escalabilidade para o sistema de consultas ao MongoDB considera diversos fatores, como o volume de dados, a complexidade das consultas e a necessidade de alta disponibilidade. A seguir, discutimos as expectativas de performance e as abordagens para escalar o sistema conforme o crescimento.

## Expectativas de Performance

As operações de consulta implementadas no sistema são baseadas em buscas simples em coleções do MongoDB, com foco na leitura de documentos. As consultas, como a exibição de todos os documentos de uma coleção ou a busca por documentos com base em um campo específico, devem ter um desempenho satisfatório para pequenas e médias quantidades de dados.

O MongoDB é otimizado para consultas rápidas e pode lidar com grandes volumes de dados graças à sua arquitetura de indexação. No entanto, conforme a base de dados cresce, a performance das consultas pode ser impactada se não houver índices adequados. Portanto, é fundamental que índices sejam criados nas coleções, especialmente para campos que são frequentemente consultados, como identificadores, datas e outros campos de pesquisa comum.

## Escalabilidade

MongoDB oferece diversas abordagens para escalabilidade horizontal, o que permite ao sistema crescer conforme a necessidade. Para escalabilidade horizontal, o MongoDB pode ser configurado em um cluster de servidores, distribuindo dados em várias máquinas. Isso é realizado através do sharding, onde os dados são divididos em fragmentos distribuídos entre diferentes nós, permitindo que o sistema seja escalado de maneira eficiente.

Além disso, o MongoDB é altamente flexível, o que facilita a adaptação do sistema a novas exigências e a implementação de novas funcionalidades sem comprometer a estrutura de dados existente. O aumento de recursos de hardware e a distribuição de carga entre múltiplos servidores são formas de garantir que o sistema se mantenha ágil e responsivo à medida que a demanda aumenta.

## Segurança e Integração

### Medidas de Segurança no MongoDB

A segurança dos dados no MongoDB é crucial, especialmente quando se trata de dados sensíveis e informações pessoais. As principais medidas de segurança incluem:

**Autenticação e Autorização** 

O MongoDB oferece autenticação robusta, onde cada usuário e aplicativo deve fornecer credenciais válidas para acessar a base de dados. Além disso, é possível configurar roles e permissões detalhadas para limitar o acesso a dados específicos e controlar operações como leitura, gravação, e administração.

**Criptografia de Dados** 

O MongoDB suporta a criptografia de dados em trânsito (TLS/SSL) e a criptografia de dados em repouso, garantindo que as informações sejam protegidas tanto durante o tráfego de rede quanto quando armazenadas no disco.

**Auditoria** 

O MongoDB Enterprise oferece um mecanismo de auditoria que permite registrar e monitorar as atividades dentro do banco de dados, como logins, operações de leitura/gravação e alterações na configuração. Isso ajuda a garantir a integridade dos dados e a detectar atividades suspeitas.

**Backup e Recuperação** 

A realização de backups regulares é uma prática importante para garantir que os dados possam ser restaurados em caso de falhas. O MongoDB oferece opções de backup online e snapshots, permitindo que os dados sejam recuperados rapidamente em caso de necessidade.

**Firewall e Segurança da Rede** 

Configurar firewalls para bloquear o acesso não autorizado ao banco de dados e garantir que as conexões sejam feitas apenas por clientes ou servidores autorizados.

# Integração do MongoDB com Outras Aplicações ou Sistemas

No nosso projeto de sugestão de consultas preventivas odontológicas, utilizamos o MongoDB como banco de dados principal devido à sua flexibilidade, escalabilidade e capacidade de lidar com grandes volumes de dados não estruturados. O MongoDB se destaca como uma excelente escolha para o nosso sistema, que precisa armazenar dados relacionados a pacientes, consultas, históricos médicos e sugestões preventivas de maneira eficiente e que permita crescimento futuro. Neste projeto, o MongoDB será integrado com as tecnologias .NET, Java e Python/IOT para atender às diversas necessidades e funcionalidades do sistema.

## Integração com .NET

No .NET, a integração com o MongoDB será feita utilizando o driver oficial do MongoDB para .NET, que possibilita a realização de operações de CRUD diretamente do código C#. A aplicação web, desenvolvida em ASP.NET Core, será responsável por gerenciar a interface do usuário, permitindo que profissionais de saúde ou pacientes consultem, atualizem e visualizem suas informações. O MongoDB será a base de dados onde armazenaremos informações sobre os pacientes, como histórico médico, exames realizados, resultados de consultas anteriores, e as recomendações preventivas feitas pelo sistema.

A API RESTful que estamos desenvolvendo em ASP.NET Core será a principal responsável por fazer a comunicação entre a aplicação web e o banco de dados MongoDB. Essa arquitetura permite que os dados sejam acessados de forma eficiente e em tempo real, proporcionando ao sistema flexibilidade para lidar com alterações nos dados, como novas consultas ou modificações nas sugestões preventivas. O MongoDB vai permitir que esses dados sejam armazenados de forma não estruturada, o que facilita a adição de novos campos conforme as necessidades do sistema evoluem.

### Integração com Java

A parte do backend em Java será usada para fornecer escalabilidade adicional e suporte a operações de processamento mais complexas. Usaremos o driver oficial do MongoDB para Java para integrar a plataforma com o banco de dados. O sistema em Java será utilizado para o processamento de dados mais pesados, como o cálculo das necessidades de consultas preventivas, que envolvem a análise de históricos de pacientes, idade, fatores de risco, e outros parâmetros médicos.

A integração com Spring Boot facilitará a criação de APIs robustas que se comunicarão com o MongoDB, garantindo que o sistema possa escalar facilmente para lidar com um número crescente de usuários. Além disso, essa parte do sistema será responsável por integrar outros serviços, como a recomendação de consultas com base em algoritmos preventivos, e também por fornecer resultados analíticos que possam ser acessados pelos profissionais de saúde para decisões clínicas.

### Integração com Python/IOT

A integração com Python e IoT será fundamental para a análise preventiva, especialmente na coleta e processamento de dados em tempo real. Usaremos a biblioteca PyMongo para integrar o MongoDB com scripts Python, que serão responsáveis por processar os dados dos pacientes e sugerir as consultas preventivas adequadas. A vantagem dessa abordagem é que Python pode ser utilizado para desenvolver modelos de machine learning ou algoritmos de recomendação baseados em dados médicos, utilizando técnicas de análise de dados, como análise preditiva e modelos estatísticos.

Além disso, dispositivos IoT (como sensores médicos ou dispositivos conectados) podem gerar dados em tempo real, que serão armazenados no MongoDB. Esses dados podem incluir informações como pressão arterial, batimentos cardíacos, ou até mesmo informações sobre hábitos de saúde, que serão usados para personalizar as recomendações preventivas e sugerir consultas odontológicas conforme o risco identificado pelo sistema.

Com a flexibilidade do MongoDB, podemos facilmente armazenar e consultar esses dados, mesmo que eles sejam gerados em grande quantidade e de diferentes fontes (como dispositivos e sensores). A escalabilidade do MongoDB garantirá que o sistema consiga lidar com esse volume de dados e se adaptar conforme novos dispositivos ou variáveis de saúde sejam adicionados.

# Conclusão

Ao integrar o MongoDB com .NET, Java e Python/IOT, conseguimos criar um sistema eficiente e altamente escalável para sugerir consultas preventivas odontológicas. O MongoDB se adapta bem às necessidades do projeto, pois permite o armazenamento flexível de dados não estruturados e oferece a escalabilidade necessária para o crescimento futuro do sistema. A integração entre as tecnologias assegura que cada parte do sistema funcione de forma coordenada, desde a interface web (usando .NET) até o backend (com Java) e as análises preventivas baseadas em dados de IoT (usando Python).

Esse ambiente integrado não só proporciona uma experiência fluida para o usuário, como também permite um gerenciamento eficiente dos dados, desde o armazenamento de informações sobre os pacientes até a análise preditiva e geração de recomendações de consultas odontológicas.