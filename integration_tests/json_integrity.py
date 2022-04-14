#!/usr/bin/env python3
# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import glob
import sys
from pathlib import Path


def file_to_json(file):
  try:
    data = json.load(file)
  except json.JSONDecodeError:
    return False
  return data


# Check if files are valid JSON
#
def check_json_integrity():
  file_paths = glob.glob("../**/*.json", recursive=True)
  invalid_files = []

  for file_path in file_paths:
    file = open(file_path, 'r')
    if file_to_json(file) is False:
      invalid_files.append(file_path.replace('..', ''))
    file.close()

  # Output message
  if len(invalid_files) == 0:
    print('All JSON files are valid!')
  else:
    print('The following JSON files are invalid :')
    for invalid_file in invalid_files:
      print(invalid_file.replace('..', ''))
      sys.exit(2)


# Check if path and slugs are valid for SIP trunk plugins
#
def check_sip_plugin_integrity():
  invalid_plugins = []

  with open('../plugins/sip/list.json') as file:
    data = file_to_json(file)
    for item in data['items']:
      pluginFilePath = f"../plugins/sip/{item['slug']}.json"
      if not Path.is_dir(Path(pluginFilePath)):
        invalid_plugins.append(f"{item['name']}: {pluginFilePath.replace('..', '')}")

  if(len(invalid_plugins) == 0):
    print('All SIP trunk plugins are valid!')
  else:
    print('The following SIP trunk plugins are invalid :')
    for invalid_plugin in invalid_plugins:
      print(invalid_plugin)
      sys.exit(2)


def main():
  check_json_integrity()
  check_sip_plugin_integrity()


if __name__ == '__main__':
  main()
