import argparse
import os
import json
import fnmatch
import re
import yaml
import glob


LEGACY_SOURCE_FOLDER = "legacy/docs-ref-autogen" #"legacy/docs-ref-autogen"
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
  with open(os.path.join(root_dir, LEGACY_SOURCE_FOLDER, 'toc.yml'), "r") as legacy_toc:
    legacy_toc = yaml.safe_load(legacy_toc)

  appended_content = ""
  file_sets = []

  import pdb
  pdb.set_trace()

  # filter that toc
  for top_level_toc_item in legacy_toc:
    if check_against_targeted_namespaces(top_level_toc_item['uid'], migrating_namespaces_regexs):
      appended_content += yaml.dump(top_level_toc_item, default_flow_style=False)
      file_sets += glob.glob(os.path.join(root_dir, LEGACY_SOURCE_FOLDER, top_level_toc_item['uid']+"*"))

  # write the toc
  with open(os.path.join(root_dir, TARGET_SOURCE_FOLDER, "toc.yml"), "a", encoding="utf-8") as stable_toc:
    stable_toc.write(appended_content)

  print(file_sets)
  for file in file_sets:
    print(file)
