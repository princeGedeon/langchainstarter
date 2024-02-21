#PydanticOutputParser
from typing import List

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Person(BaseModel):
    summary:str=Field("Résumé de la personne")
    facts:List[str]=Field("Faits interressants sur la personne")
    topics_of_interest=List[str]=Field(description="Sujet qui interesse cette personne")
    ice_breker=List[str]=Field(description="Créer un ice breaker pour ouvrir la conversation avec la personne")


    def to_dict(self):
        return {"summary":self.summary,"facts":self.facts,"topics_of_interest":self.topics_of_interest,"ice_breaker":self.ice_breker}



#La sortie on veut sous qu'elle format, JSON,XML,YAML,dossier packet??? On a assez d'options
person_parser=PydanticOutputParser(Person)