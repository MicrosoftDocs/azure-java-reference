import argparse
import os
import json


LEGACY_SOURCE_FOLDER = "legacy-docs-toc-merge" #"legacy/docs-ref-autogen"
TARGET_SOURCE_FOLDER = "unified-latest/docs-ref-autogen" #"docs-ref-autogen"

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), ".."))

def check_against_targeted_namespaces(test_line, namespace_list):



if __name__ == "__main__":
  # parse packages.json
  with open(os.path.join(root_dir, "temporary-src-based-yml", 'migration.json'), 'r') as f:
    text = f.read().rstrip("\n")
    json = json.loads(text)

    migrating_namespaces = json["migrating_namespaces"]

    with open(os.path.join(LEGACY_SOURCE_FOLDER, 'toc.yml')) as legacy_toc:
      lines = legacy_toc.readlines()
      
      filtered_to_known_namespaces = [line for line in lines if check_against_targeted_namespaces(test_line=line, namespace_list=migrating_namespaces)]

      additional_content = "".join(filtered_to_known_namespaces)

      with open(os.path.join(TARGET_SOURCE_FOLDER, "toc.yml"), a) as toc:
         toc.write(additional_content)