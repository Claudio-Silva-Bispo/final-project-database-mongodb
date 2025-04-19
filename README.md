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
        "especialista_id": "1",
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
        "especialista_id": "1",
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
        "agendamento_id": "ag_001",
        "cliente_id": "cli_001",
        "especialista_id": "esp_789",
        "data": "2025-04-25",
        "horario": "14:00",
        "status": "Confirmado",
        "tipo_consulta": "Rotina",
        "avaliacao_cliente": null
    }
```

## 📅 Coleção: consultas

**✅ Justificativa**

Essa coleção representa a consulta oficial. Ela será vinculada ao resultado_consultas após a execução. Também pode ser usada em relatórios, histórico do cliente, e controle da agenda da clínica e do especialista.

```bash
    {
        "consulta_id": "con_001",
        "cliente_id": "cli_001",
        "clinica_id": "cli_001",
        "especialista_id": "esp_001",
        "data": "2025-04-25",
        "horario": "09:00",
        "turno": "Manhã",
        "tipo_consulta": "Limpeza",
        "status": "Confirmada", // Pode ser "Confirmada", "Cancelada", "Realizada"
        "foi_remarcada": false,
        "confirmacao_cliente": true,
        "confirmacao_clinica": true,
        "criado_em": "2025-04-19T14:22:00Z"
    }
```

## ⭐ Coleção: feedbacks

**✅ Justificativa** 

Permite gerar notas médias, análise de sentimentos e alimentar o sistema de IA com dados reais dos usuários. As pesquisas serão respondidas pelos clientes apenas.

```bash
    {
        "feedback_id": "fb_001",
        "cliente_id": "cli_001",
        "clinica_id": "cli_234",
        "especialista_id": "esp_789",
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
      "resultado_id": "res_001",  
      "agendamento_id": "ag_123",
      "cliente_id": "cli_001",
      "clinica_id": "cli_234",
      "especialista_id": "esp_789",
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
        "desafio_id": "ds_001",
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
        idUsuario: "abc123",  
        idAgendamento: "xyz789",               
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
    uidUsuario: "abc123",                
    mensagemUsuario: "Quais horários estão disponíveis?",
    respostaIA: "Você pode agendar para terça às 10h ou quarta às 16h.",
    dataHora: Timestamp.now(),
    tipoInteracao: "pergunta",            // 'pergunta' | 'formulario' | 'recomendacao' | 'outro'
    contextoRelacionado: "agendamento"    // Ex: 'cadastro', 'feedback', etc. (opcional)
  }
```

## Criar 10 documentos para cada coleção

Será criado a estrutura dos dados e inserir via import no terminal

Vamos montar um arquivo .json com 10 documentos, cada um com 10 atributos, simulando dados realistas. Isso é ideal para teste e desenvolvimento. O modelo será funcional através de importação dos arquivos .json na pasta projeto. Será possível importar e clicar para consultar os dados enviados.

**Estrutura dos arquivos**
