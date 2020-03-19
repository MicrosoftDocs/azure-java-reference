import argparse
import os
import json
import fnmatch
import re
import yaml


LEGACY_SOURCE_FOLDER = "legacy-docs-toc-merge" #"legacy/docs-ref-autogen"
TARGET_SOURCE_FOLDER = "unified-latest/docs-ref-autogen" #"docs-ref-autogen"

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), ".."))

def check_against_targeted_namespaces(test_line, namespace_patterns_list):
  return any([re.match(namespace_pattern, test_line) for namespace_pattern in namespace_patterns_list])


if __name__ == "__main__":
  # parse packages.json
  with open(os.path.join(root_dir, "temporary-src-based-yml", 'migration.json'), 'r') as f:
    text = f.read().rstrip("\n")
    json = json.loads(text)

    migrating_namespaces = json["migrating_namespaces"]
    migrating_namespaces_regexs = [fnmatch.translate(namespace) for namespace in migrating_namespaces]

  # get the yml from legacy
  with open(os.path.join(LEGACY_SOURCE_FOLDER, 'toc.yml'), "r") as legacy_toc:
    legacy_toc = yaml.safe_load(legacy_toc)

  appended_content = ""
  # filter that toc
  for top_level_toc_item in legacy_toc:
    if check_against_targeted_namespaces(top_level_toc_item['uid'], migrating_namespaces_regexs):
      appended_content += yaml.dump(top_level_toc_item)

  # write the toc
  with open(os.path.join(TARGET_SOURCE_FOLDER, "toc.yml"), "a") as stable_toc:
    toc.write(yaml.dump(legacy_toc, default_flow_style=False))

    # with open(os.path.join(LEGACY_SOURCE_FOLDER, 'toc.yml'), "a") as legacy_toc:
    #   lines = legacy_toc.readlines()
      
      # print(lines)
      # filtered_to_known_namespaces = [line for line in lines if check_against_targeted_namespaces(test_line=line, namespace_patterns_list=migrating_namespaces_regexs)]

      # additional_content = "".join(filtered_to_known_namespaces)

      # print("gonna add")
      # print(additional_content)
      # # with open(os.path.join(TARGET_SOURCE_FOLDER, "toc.yml"), a) as toc:
      # #    toc.write(additional_content)

