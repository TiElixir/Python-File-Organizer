import os
import json

from utils.ai_config_generator import generate_temp_config
from utils.rule_engine import apply_rules


def main():
    path = input("Enter the directory to sort: ").strip()
    #path = ("/home/tielixir/Coding/Projects/Python-File-Organizer/sampleDir").strip()

    if not os.path.isdir(path):
        print("Invalid directory")
        return

    instruction = input("Enter sorting instruction: ").strip()
    #instruction = ("move every file with 'screenshot' in its name to a folder called Screenshots").strip()

    generate_temp_config(instruction)

    with open("temp_config.json") as f:
        config = json.load(f)

    apply_rules(path, config)

    print("Done.")


if __name__ == "__main__":
    main()
