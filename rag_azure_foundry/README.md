# 🤖 Chat RAG Especializado em Agentes de IA

Este projeto consiste no desenvolvimento de um **chat interativo baseado em RAG (Retrieval-Augmented Generation)**, que responde perguntas a partir de arquivos PDF carregados sobre o tema de **Agentes de Inteligência Artificial**.

Utilizando técnicas de **IA generativa**, **busca vetorial** e **embeddings**, o sistema é capaz de entender, indexar e responder com precisão com base em documentos fornecidos, sem depender exclusivamente do conhecimento pré-treinado do modelo.

---

## 🧠 Descrição do Projeto

Neste desafio, foi desenvolvido um **sistema de chatbot** capaz de responder perguntas com base em informações extraídas de **5 documentos PDF sobre Agentes de IA**.  

O pipeline utiliza conceitos de **Processamento de Linguagem Natural (NLP)** e **Machine Learning** para:
- Ler e interpretar os textos dos PDFs
- Vetorizar os conteúdos
- Realizar busca semântica
- Gerar respostas personalizadas com um modelo LLM

A aplicação pode ser implantada como serviço web, permitindo **interações em tempo real** com o usuário.

---

## 🎯 Objetivos

✅ Carregar arquivos PDF contendo conteúdos específicos sobre Agentes de IA  
✅ Implementar uma **busca vetorial inteligente** para indexação dos documentos  
✅ Utilizar **IA generativa** para compor respostas baseadas nos PDFs  
✅ Criar um **chatbot interativo** que responda com base em fontes confiáveis e carregadas pelo próprio usuário  

---

## 📘 Cenário de Uso (Hipotético)

Imagine que você é um estudante de Engenharia de Software prestes a escrever seu TCC. Para isso, precisa revisar diversos artigos científicos sobre Agentes de IA. Porém, extrair informações úteis e cruzar ideias entre documentos se torna uma tarefa demorada.

Com esse sistema, você carrega os artigos em PDF e interage com um **assistente virtual inteligente**, capaz de:
- Compreender o conteúdo dos artigos
- Encontrar relações entre os textos
- Gerar respostas embasadas nas suas fontes

---

## 🛠️ Tecnologias Utilizadas

- **Azure OpenAI Service** (GPT-4 / GPT-3.5)
- **Azure AI Search** (busca vetorial com embeddings)
- **Azure Blob Storage** (armazenamento dos PDFs)
- **Python SDKs / REST APIs**
- **NLP & IA Generativa**

---

## 🚀 Como Funciona

1. O usuário carrega os arquivos PDF
2. O sistema divide os textos em **chunks**
3. Cada trecho é transformado em um **vetor de embeddings**
4. Quando o usuário faz uma pergunta:
   - O sistema faz uma **busca vetorial** nos documentos
   - Recupera os trechos mais relevantes
   - Envia junto com a pergunta para o modelo LLM (GPT)
5. O modelo responde de forma **contextual e fundamentada**

---

## 📎 Exemplos de Perguntas Suportadas

> "Quais são os principais tipos de agentes inteligentes?"  
> "Como funcionam os agentes baseados em utilidade?"  
> "Qual a relação entre agentes e ambientes em IA?"  

---

## 💡 Próximos Passos

- Adicionar upload dinâmico de arquivos pelo usuário
- Criar interface web responsiva (usando Streamlit, Flask ou Next.js)
- Implementar controle de versão nos documentos carregados
- Otimizar o chunking e a geração de embeddings

---

## 📄 Licença

Este projeto é de caráter educacional e experimental.  
Sinta-se livre para clonar, estudar e adaptar.

---

### 🤝 Contribuições

Contribuições são bem-vindas!  
Se tiver sugestões, dúvidas ou quiser melhorar algo, abra uma issue ou um pull request!

---

