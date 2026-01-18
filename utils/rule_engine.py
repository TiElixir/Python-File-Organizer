import os
import shutil


def matches_rule(filename, rule):
    name = filename.lower()
    ext = os.path.splitext(filename)[-1].lower()

    # If Extensions list is NOT empty, enforce it
    if rule["Extensions"]:
        if ext not in rule["Extensions"]:
            return False

    for keyword in rule["FilenameContains"]:
        if keyword not in name:
            return False

    return True



def apply_rules(root_path, config):
    for current_dir, _, files in os.walk(root_path):
        for file in files:
            full_path = os.path.join(current_dir, file)

            for rule in config["Rules"]:
                if matches_rule(file, rule):
                    dest_dir = os.path.join(root_path, rule["Destination"])
                    os.makedirs(dest_dir, exist_ok=True)

                    dest_path = os.path.join(dest_dir, file)

                    # Avoid moving file onto itself
                    if os.path.abspath(full_path) == os.path.abspath(dest_path):
                        continue

                    shutil.move(full_path, dest_path)
                    break
