import re
import json
from agents.dialogue_agent import DialogueAgent

def extract_json_block(text):
    """Extracts the first JSON object from a string (ignores markdown or extra text)."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else None

def test_dialogue_agent():
    # Load sample conversation
    with open("sample_data/sample_conversation.txt") as f:
        conversation = f.read()

    # Run DialogueAgent
    agent = DialogueAgent("cardiology")
    output = agent.run(conversation)
    print("🔍 Raw Output:\n", output)

    # Extract and validate JSON
    json_str = extract_json_block(output)
    if not json_str:
        print("❌ Could not extract valid JSON from output.")
        return

    try:
        parsed = json.loads(json_str)
        print("\n✅ Parsed JSON:\n", json.dumps(parsed, indent=2))
    except json.JSONDecodeError as e:
        print("❌ JSON Decode Error:", e)

if __name__ == "__main__":
    test_dialogue_agent()

