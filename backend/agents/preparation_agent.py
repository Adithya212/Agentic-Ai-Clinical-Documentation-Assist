from llm_setup import get_llm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class PreparationAgent:
    def __init__(self):
        self.llm = get_llm()
        self.template = PromptTemplate.from_template("""
        Analyze this patient EHR summary and return a pre-visit summary:

        {input_text}

        Return:
        - Key metrics trend
        - Issues needing follow-up
        - Medication adherence
        - Screenings due
        """)
        self.chain = LLMChain(llm=self.llm, prompt=self.template)

    def run(self, patient_info: str) -> str:
        return self.chain.run({"input_text": patient_info})
