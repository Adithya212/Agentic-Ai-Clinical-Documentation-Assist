from llm_setup import get_llm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import json

class CoderAgent:
    def __init__(self):
        self.llm = get_llm()
        self.template = PromptTemplate.from_template("""
        Given this structured clinical data:

        {structured_data}

        Return a JSON with:
        - ICD-11 codes (primary and secondary)
        - CPT procedure codes
        - E/M level justification

        Each entry should include the code, description, and rationale.
        """)
        self.chain = LLMChain(llm=self.llm, prompt=self.template)

    def run(self, structured_data: dict) -> str:
        return self.chain.run({"structured_data": json.dumps(structured_data, indent=2)})
