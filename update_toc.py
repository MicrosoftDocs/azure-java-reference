# Assumptions
#   This script is being executed in the MicrosoftDocs/azure-java-reference repository
#   This script is running on at least python 2.7
#   PyYaml is installed `python -m pip install pyyaml`

# This script is designed as a stopgap way to repair the global ToC necessary to power docs.microsoft.com. 
# Currently the ToC from a CI run only includes the first package of whichever set
# For the unified-latest moniker, need to update the ToC under core/toc.yml to include all the packages within 
# package.json

import json
import os
import glob
import yaml

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
    chosen_service_folder = [results for results in os.listdir('./{path}/'.format(path=moniker_path))][0]

    member_discovery_folder = os.path.join(moniker_path, chosen_service_folder)
    toc_output_path = os.path.join(member_discovery_folder, 'toc.yml')

    print(member_discovery_folder)
    print(toc_output_path)    

    for namespace in moniker_maps[moniker_path]:
      full_namespace = os.path.join(member_discovery_folder, namespace[0] + '.' + namespace[1].replace('-','.'))

      member_file = full_namespace +".yml"


      try:
        # Read YAML file
        with open(member_file, 'r') as stream:
          data_loaded = yaml.safe_load(stream)
      except:
        print("Can't find {}".format(member_file))

      print(full_namespace)
      namespace_members = [os.path.basename(file) for file in glob.glob(full_namespace + '*')]

      if namespace == "unified-latest\\core\\com.azure.data.appconfiguration"
      
  





      



  # generate set of members

