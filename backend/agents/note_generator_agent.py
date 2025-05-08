from llm_setup import get_llm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import json

class NoteGeneratorAgent:
    def __init__(self):
        self.llm = get_llm()
        self.template = PromptTemplate.from_template("""
        Generate a SOAP note from this structured medical data:

        {structured_data}

        Use the following format:
        Subjective: Patient's symptoms and history
        Objective: Exam findings and tests
        Assessment: Diagnoses or differentials
        Plan: Treatment, follow-up, education

        Keep it professional and concise.
        """)
        self.chain = LLMChain(llm=self.llm, prompt=self.template)

    def run(self, structured_data: dict) -> str:
        return self.chain.run({"structured_data": json.dumps(structured_data, indent=2)})
