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



