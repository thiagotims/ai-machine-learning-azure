import os  
import base64
from openai import AzureOpenAI  

endpoint = os.getenv("ENDPOINT_URL", "https://ragtim2283005908.openai.azure.com/")  
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o")  
search_endpoint = os.getenv("SEARCH_ENDPOINT", "https://rag-tim-search.search.windows.net/")  
search_key = os.getenv("SEARCH_KEY", "put your Azure AI Search admin key here")  
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "REPLACE_WITH_YOUR_KEY_VALUE_HERE")  

# Inicializar o cliente do Serviço OpenAI do Azure com autenticação baseada em chave    
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    api_key=subscription_key,  
    api_version="2024-05-01-preview",
)
    
    
# IMAGE_PATH = "YOUR_IMAGE_PATH"
# encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')

#Preparar o prompt de chat 
chat_prompt = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "Você é um especialista em Agentes de Inteligência Artificial e irá me ajudar com dúvidas sobre o tema. "
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Fale sobre uma área de aplicação de Agentes Inteligentes e sobre algumas das suas limitações ou desafios."
            }
        ]
    },
    {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "Uma área de aplicação de Agentes Inteligentes (AI) é a **educação**, especialmente em contextos como Ambientes Virtuais de Aprendizagem (AVA) e Sistemas Tutores Inteligentes (STI). Esses agentes podem desempenhar diversas funções, como facilitar a comunicação entre alunos e professores, personalizar a aprendizagem com base nas necessidades dos alunos e promover a colaboração em atividades educacionais. Exemplos de projetos incluem assistentes virtuais e robôs sociais que personalizam interações para melhorar o desempenho dos alunos, como o SARA (Socially Aware Robot Assistant), que adapta suas funcionalidades com base na interação social [doc1][doc2].\n\nNo entanto, essa área também enfrenta **limitações e desafios**. Por exemplo, embora os AVAs tenham evoluído significativamente, eles ainda não são suficientemente interativos ou estimulantes para atender ao perfil de muitos estudantes online, o que contribui para altos índices de desistência em cursos de ensino a distância. Além disso, a criação de agentes que consigam manter diálogos coesos e verossímeis por longos períodos permanece um desafio técnico. Sistemas baseados em casamento de padrões, como o famoso ELIZA, enfrentam limitações em criar interações mais naturais e realistas [doc3]. \n\nEsses desafios destacam a necessidade de avanços na personalização, interatividade e realismo no uso de agentes inteligentes na educação."
            }
        ]
    }
] 
    
# Incluir resultado de fala se a fala estiver habilitada  
messages = chat_prompt  
    
# Gerar a conclusão  
completion = client.chat.completions.create(  
    model=deployment,
    messages=messages,
    max_tokens=800,  
    temperature=0.7,  
    top_p=0.95,  
    frequency_penalty=0,  
    presence_penalty=0,
    stop=None,  
    stream=False,
    extra_body={
      "data_sources": [{
          "type": "azure_search",
          "parameters": {
            "filter": None,
            "endpoint": f"{search_endpoint}",
            "index_name": "teal-pot-qnw7x9hb81",
            "semantic_configuration": "azureml-default",
            "authentication": {
              "type": "api_key",
              "key": f"{search_key}"
            },
            "query_type": "simple",
            "in_scope": True,
            "role_information": "Você é um especialista em Agentes de Inteligência Artificial e irá me ajudar com dúvidas sobre o tema. ",
            "strictness": 3,
            "top_n_documents": 5
          }
        }]
    }
)

print(completion.to_json())  
    
