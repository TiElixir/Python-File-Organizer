import google.generativeai as genai
import json
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

PROMPT_TEMPLATE = """
Convert the following instruction into executable file-sorting rules.

Instruction:
"{instruction}"

Output rules as JSON using this schema ONLY:

{{
  "Rules": [
    {{
      "Extensions": array of file extensions (lowercase, starting with "."),
      "FilenameContains": array of lowercase substrings,
      "Destination": string
    }}
  ]
}}

Rules:
- Output ONLY valid JSON
- No explanations
- No fallback logic
"""

def generate_temp_config(instruction, out_file="temp_config.json"):
    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(
        PROMPT_TEMPLATE.format(instruction=instruction)
    )

    text = response.text.strip()
    text = text.replace("```json", "").replace("```", "")

    data = json.loads(text)

    with open(out_file, "w") as f:
        json.dump(data, f, indent=4)
