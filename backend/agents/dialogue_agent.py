# from llm_setup import get_llm
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain

# class DialogueAgent:
#     def __init__(self, clinician_specialty: str = "general"):
#         self.clinician_specialty = clinician_specialty
#         self.llm = get_llm()
#         self.template = PromptTemplate.from_template("""
#         As a {specialty} specialist, analyze the following clinician-patient conversation:

#         {conversation_text}

#         Return ONLY a valid JSON object with this structure — no markdown, no explanations:

#         {
#             "missing_elements": [...],
#             "alerts": [...],
#             "structured_data": {
#                 "Symptoms": [...],
#                 "Medications": [...],
#                 "Allergies": [...],
#                 "Conditions": [...]
#             }
#         }
       
#         """)
#         self.chain = LLMChain(llm=self.llm, prompt=self.template)

#     def run(self, conversation_text: str) -> str:
#         return self.chain.run({
#             "conversation_text": conversation_text,
#             "specialty": self.clinician_specialty
#         })
from llm_setup import get_llm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class DialogueAgent:
    def __init__(self, clinician_specialty: str = "general"):
        self.clinician_specialty = clinician_specialty
        self.llm = get_llm()

        self.template = PromptTemplate(
            input_variables=["conversation_text", "specialty"],
            template="""
            As a {specialty} specialist, analyze the following clinician-patient conversation:

            {conversation_text}

            Identify:
            1. Missing elements for history, diagnosis, or billing
            2. Real-time alerts/suggestions
            3. Structured medical data

            Return JSON with:
            - missing_elements: list
            - alerts: list
            - structured_data: object
            """
                    )

        self.chain = LLMChain(llm=self.llm, prompt=self.template)

    def run(self, conversation_text: str) -> str:
        return self.chain.run({
            "conversation_text": conversation_text,
            "specialty": self.clinician_specialty
        })

