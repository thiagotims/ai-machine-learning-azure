import os
from openai import AzureOpenAI  
from azure.identity import DefaultAzureCredential, get_bearer_token_provider  
  
endpoint = os.getenv("ENDPOINT_URL", "https://ragtim2283005908.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o")
  
# Initialize Azure OpenAI client with Entra ID authentication  
cognitiveServicesResource = os.getenv('AZURE_COGNITIVE_SERVICES_RESOURCE', 'YOUR_COGNITIVE_SERVICES_RESOURCE')  
token_provider = get_bearer_token_provider(  
    DefaultAzureCredential(),  
    f'{cognitiveServicesResource}.default'  
)  
        
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    azure_ad_token_provider=token_provider,  
    api_version='2024-05-01-preview',  
)  
       
completion = client.chat.completions.create(  
    model=deployment,  
    messages=[
    {
        "role": "system",
        "content": "Você é um especialista em Agentes de Inteligência Artificial e irá me ajudar com dúvidas sobre o tema. "
    },
    {
        "role": "user",
        "content": "Fale sobre uma área de aplicação de Agentes Inteligentes e sobre algumas das suas limitações ou desafios."
    },
    {
        "role": "assistant",
        "content": "Uma área de aplicação de Agentes Inteligentes (AI) é a **educação**, especialmente em contextos como Ambientes Virtuais de Aprendizagem (AVA) e Sistemas Tutores Inteligentes (STI). Esses agentes podem desempenhar diversas funções, como facilitar a comunicação entre alunos e professores, personalizar a aprendizagem com base nas necessidades dos alunos e promover a colaboração em atividades educacionais. Exemplos de projetos incluem assistentes virtuais e robôs sociais que personalizam interações para melhorar o desempenho dos alunos, como o SARA (Socially Aware Robot Assistant), que adapta suas funcionalidades com base na interação social [doc1][doc2].\n\nNo entanto, essa área também enfrenta **limitações e desafios**. Por exemplo, embora os AVAs tenham evoluído significativamente, eles ainda não são suficientemente interativos ou estimulantes para atender ao perfil de muitos estudantes online, o que contribui para altos índices de desistência em cursos de ensino a distância. Além disso, a criação de agentes que consigam manter diálogos coesos e verossímeis por longos períodos permanece um desafio técnico. Sistemas baseados em casamento de padrões, como o famoso ELIZA, enfrentam limitações em criar interações mais naturais e realistas [doc3]. \n\nEsses desafios destacam a necessidade de avanços na personalização, interatividade e realismo no uso de agentes inteligentes na educação."
    }
],  
    past_messages=10,
    max_tokens=800,  
    temperature=0.7,  
    top_p=0.95,  
    frequency_penalty=0,  
    presence_penalty=0,  
    stop=None,  
    extra_body={  
        "data_sources": [  
            {  
                "type": "azure_search",  
                "parameters": {  
                    "endpoint": os.environ["AZURE_AI_SEARCH_ENDPOINT"],  
                    "index_name": os.environ["AZURE_AI_SEARCH_INDEX"],  
                    "authentication": {  
                        "type": "system_assigned_managed_identity"  
                    }  
                }  
            }  
        ]  
    }  
)

print(completion.model_dump_json(indent=2))  



