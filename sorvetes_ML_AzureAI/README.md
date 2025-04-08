# 🍦 Prevendo Vendas de Sorvete com Machine Learning - Gelato Mágico na Nuvem ☁️

## 🌞 O Desafio Real por Trás da Tecnologia

Imagine a seguinte cena: um dia ensolarado e quente em uma cidade litorânea. A sorveteria *Gelato Mágico* está cheia de clientes em busca de uma deliciosa forma de se refrescar. No entanto, o estoque de sorvetes se esgota rapidamente — a produção do dia não deu conta da demanda. No dia seguinte, preocupado com a escassez anterior, o proprietário decide produzir em dobro. Mas o tempo muda, o dia esfria, e os freezers ficam lotados de sorvete que não será vendido.

Essa montanha-russa de perdas e oportunidades desperdiçadas é mais comum do que se imagina. Gerenciar o estoque de sorvete de forma eficiente, principalmente em locais onde o clima influencia diretamente o consumo, é crucial para o sucesso do negócio.

Foi exatamente pensando nesse cenário que nasceu este projeto. Utilizando **Machine Learning**, propus uma solução prática: prever a quantidade de sorvetes vendidos com base na temperatura do dia. Essa previsão permite:

- ✅ Reduzir desperdícios de produção
- ✅ Otimizar o uso de ingredientes e energia
- ✅ Aumentar as vendas, estando pronto para dias de alta demanda
- ✅ Melhorar o planejamento estratégico da loja

## 📈 A Solução com Machine Learning

O modelo desenvolvido busca correlacionar a **temperatura do dia** com a **quantidade de sorvetes vendidos**. A base de dados utilizada foi gerada artificialmente para simular vendas reais ao longo de diferentes condições climáticas.

A abordagem usada foi **Regressão Linear**, que nos permitiu compreender e quantificar essa relação de forma simples e eficiente.

### 🔬 Resultados e Métricas do Modelo

Após o treinamento do modelo na plataforma Azure ML, os resultados foram bastante satisfatórios, indicando que o modelo tem boa capacidade preditiva:

- **R² (Coeficiente de Determinação): 0.83426**  
  > Explica aproximadamente 83% da variação nas vendas com base na temperatura.

- **Erro Absoluto Médio Normalizado: 0.07389**  
  > Baixo erro médio, indicando previsões bastante próximas dos valores reais.

- **Erro de Raiz do Valor Quadrático Médio: 12.266**  
  > Representa a média do desvio padrão entre valores reais e previstos, em unidades de venda.

- **Correlação de Spearman: 0.84936**  
  > Forte correlação entre temperatura e vendas, confirmando a relação esperada.

Esses resultados demonstram que o modelo pode ser uma excelente ferramenta de apoio à decisão no gerenciamento de produção e estoque da sorveteria.

## ☁️ Por Que Usar o Azure Machine Learning?

O projeto foi inteiramente desenvolvido e executado na **Plataforma Azure ML**, que trouxe diversas vantagens:

- 🔁 **Automated ML**: permite testar e comparar diferentes modelos automaticamente.
- 🔍 **MLflow**: facilita o rastreamento dos experimentos e das métricas de desempenho.
- 🧪 **Reprodutibilidade**: com pipelines e ambientes configuráveis, os experimentos podem ser facilmente repetidos e versionados.
- 🚀 **Escalabilidade na nuvem**: ideal para ambientes produtivos ou testes com grandes volumes de dados.
- 💡 **Interface Intuitiva + Poder de Código**: tanto para quem está começando quanto para usuários avançados.

## 🧠 Conclusão

A previsão de vendas com base em dados históricos e variáveis externas como a temperatura permite uma gestão **mais inteligente**, **sustentável** e **lucrativa**. Este projeto une o mundo real com o poder da Inteligência Artificial, mostrando como soluções simples podem ter grande impacto nos negócios — mesmo em algo tão gostoso quanto sorvete 🍨.

---

### 👨‍💻 Tecnologias Utilizadas

- Python
- Regressão Linear
- Azure Machine Learning
- MLflow
- Pandas / Scikit-learn / Matplotlib

---

### 📁 Como Rodar este Projeto

1. Clone este repositório:
```bash
git clone https://github.com/seuusuario/projeto-ml-sorvete.git
```

2. Acesse o projeto no Azure ML Studio (ou configure um ambiente local Python)
3. Importe a base de dados fictícia `dados_sorvete.csv`
4. Execute o notebook de treinamento ou crie um experimento AutoML
5. Avalie as métricas geradas e faça previsões com novos dados de temperatura

---

### 🚀 Vamos conversar?

Se você gostou deste projeto, me siga aqui no GitHub e no LinkedIn! Estou sempre explorando novas ideias em dados e IA! 😄
