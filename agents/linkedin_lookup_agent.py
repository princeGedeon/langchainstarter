from langchain.agents import initialize_agent, AgentType
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI

from tools.tools import get_profile_url


def lookup(name:str):
    # je defini le llm
    llm=ChatOpenAI(temperature=0,model_name="gpt-3.5-turbo")
    template="Donne un nom complet {name}.Je veux que tu me donne le lien de la page profile Linkedin de cette personne.Le résultat doit contenir seulement un URL"

    prompt=PromptTemplate(input_variables=[name],template=template)



    # Je définis les outils de l'agents
    tools_for_agent=[Tool(name="Explorer Google pour trouver les pages profils Linkedin",func=get_profile_url,
                          description="Utile quand tu as besoin de trouver des page profils Linkedin")]

    agent= initialize_agent(llm=llm,tools=tools_for_agent,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)
    linked_profile_url=agent.run(prompt.format_prompt(name=name))
    return  linked_profile_url