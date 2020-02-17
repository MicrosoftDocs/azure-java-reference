# Assumptions
#   This script is being executed in the MicrosoftDocs/azure-java-reference repository
#   This script is running on at least python 2.7
#   PyYaml is installed `python -m pip install pyyaml`

# This script is designed as a stopgap way to repair the global ToC necessary to power docs.microsoft.com. 
# Currently the ToC from a CI run only includes the first package of whichever set is being run.
# For the unified-latest moniker, this script will update the ToC under core/toc.yml to include all the packages within 
# package.json

import json
import os
import glob
import yaml
import pdb

NAMESPACE_OUTPUT_TEMPLATE = """- uid: "{namespace}"
  name: "{namespace}"
  items:
{member_classes}
"""

MEMBER_OUTPUT_TEMPLATE = """  - uid: \"{member_uid}\"
    name: \"{member_name}\""""

def output_namespace_yml(namespace_key, namespace_results):
  top_level_members = sorted([member for member in namespace_results if not member.split('.')[-1][0].isupper()], key=lambda namespace: len(namespace.split(".")))
  output = ""
  for top_level_member in top_level_members:
    top_level_member_array = top_level_member.split(".")
    
    members = [member for member in namespace_results if member.split(".")[0:-1] == top_level_member_array and member.split('.')[-1][0].isupper()]
    sorted_members = sorted(members, key=lambda x: x.split(".")[-1])


    output += NAMESPACE_OUTPUT_TEMPLATE.format(
      namespace=top_level_member,
      member_classes="\n".join([MEMBER_OUTPUT_TEMPLATE.format(member_uid=member,member_name=member.split(".")[-1]) for member in sorted_members])
    )
  return output

def read_yaml_file(member_file):
  try:
    # Read YAML file
    with open(member_file, 'r') as stream:
      data_loaded = yaml.safe_load(stream)
  except:
    print("Can't find {}".format(member_file))


if __name__ == "__main__":
  # parse packages.json
  with open('package.json', 'r') as f:
    text = f.read().rstrip("\n")
    json = json.loads(text)

  # extract all outputpath -> namespace tuples 
  paths = [(i['output_path'], [(p['packageGroupId'].replace(".azure",""),p['packageArtifactId']) for p in i['packages']]) for i in json]

  # flat list
  moniker_maps = {}

  for output_tuple in paths:
    for namespace in output_tuple[1]:
      moniker_tuple = output_tuple[0].split('/')[0]
      if moniker_tuple in moniker_maps:
        moniker_maps[moniker_tuple].append(namespace)
      else:
        moniker_maps[moniker_tuple] = [ namespace ]

  # choose the first service folder (should be core)
  for moniker_path in moniker_maps.keys():
    print('STARTING {}'.format(moniker_path))
    chosen_service_folder = [results for results in os.listdir('./{path}/'.format(path=moniker_path))][0] or ''

    member_discovery_folder = os.path.join(moniker_path, chosen_service_folder)
    toc_output_path = os.path.join(member_discovery_folder, 'toc_new.yml')

    print(member_discovery_folder)
    print(toc_output_path)    

    namespace_members = {}
    yaml_output = ""

    for namespace in moniker_maps[moniker_path]:
      full_namespace = namespace[0] + '.' + namespace[1].replace('-','.')
      full_namespace_path = os.path.join(member_discovery_folder, full_namespace)
      member_file = full_namespace_path +".yml"
      if full_namespace not in namespace_members:
        namespace_members[full_namespace] = []

      namespace_members[full_namespace].extend([os.path.splitext(os.path.basename(file))[0] for file in glob.glob(full_namespace_path + '*') if ".implementation" not in os.path.splitext(os.path.basename(file))[0]])

    for i in namespace_members:
      yaml_output += output_namespace_yml(i, namespace_members[i])


    print(yaml_output)
    with open(toc_output_path, "w") as f:
      f.write("### YamlMime:TableOfContent\n")
      f.write(yaml_output)



  # generate set of members

