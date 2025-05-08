# backend/test_flow.py
import re
import json
from agents.preparation_agent import PreparationAgent
from agents.dialogue_agent import DialogueAgent
from agents.note_generator_agent import NoteGeneratorAgent
from agents.coder_agent import CoderAgent

def extract_json_block(text):
    """Extracts the first JSON object from a string (ignores markdown, explanations, etc.)."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else None

def test_flow():
    # Load sample patient data
    with open("sample_data/sample_patient.json") as f:
        patient_data = json.load(f)

    # # # Step 1: Generate pre-visit summary
    # prep_agent = PreparationAgent()
    # summary = prep_agent.run(json.dumps(patient_data, indent=2))
    # print("📝 Pre-Visit Summary:\n", summary)

    # Step 2: Analyze conversation
    with open("sample_data/sample_conversation.txt") as f:
        conversation = f.read()

    dialogue_agent = DialogueAgent("cardiology")
    analysis_output = dialogue_agent.run(conversation)
    print("\n📢 Dialogue Analysis:\n", analysis_output)
    # Extract pure JSON from LLM output
    json_str = extract_json_block(analysis_output)
    if not json_str:
        print("❌ Failed to extract JSON from dialogue_agent output.")
        return

    analysis_json = json.loads(json_str)
    # Step 3: Generate SOAP note
    # structured_data = json.loads(analysis_json).get("structured_data", {})
    structured_data = analysis_json.get("structured_data", {})

    note_agent = NoteGeneratorAgent()
    soap_note = note_agent.run(structured_data)
    print("\n📄 SOAP Note:\n", soap_note)

    # Step 4: Generate Billing Codes
    coder_agent = CoderAgent()
    codes = coder_agent.run(structured_data)
    print("\n💰 Billing Codes:\n", codes)

if __name__ == "__main__":
    test_flow()
