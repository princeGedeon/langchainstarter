from dotenv import load_dotenv
import os

from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import person_parser, Person
from tiers.linkedin import scrape_linkedin_profile
from tools.tools import adapt_bj_to_normal_url

def  prince_break(name:str)->Person:
    """

    :param name:
    :return:
    """
    linkedin_profile_url = linkedin_lookup_agent(name=name)

    print(linkedin_profile_url)
    linkedin_profile_url = adapt_bj_to_normal_url(linkedin_profile_url)
    print(f"URL LINKEDIN FOUND: {linkedin_profile_url}")

    summary_template = """
        Étant donné les informations {information} sur une personne que je veux que vous me donnez:
        1. Un court résumé
        2. Deux faits interressants sur lui
        3. Des sujets interressants auxquelles il est interressait
        4. 2 icebreaker créatif pour ouvrir une conversation avec lui
        \n{format_instruction}
        """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template,partial_variables={'format_instruction':person_parser.get_format_instructions()})
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    res = chain.invoke(input={'information': linkedin_data})
    print(res)
    return res


if __name__ == "__main__":
    load_dotenv()
    print(prince_break("GUEDJE Gédéon"))

