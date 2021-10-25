#!/usr/bin/env python3
# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import glob
import sys

def is_valid_json(file):
  try:
    json.load(file)
  except json.JSONDecodeError:
    return False
  return True

def main():
  file_paths = glob.glob("../**/*.json", recursive=True)
  invalid_files = []

  for file_path in file_paths:
    file = open(file_path, 'r')
    if is_valid_json(file) == False:
      invalid_files.append(file_path)
    file.close()

  # Output message
  if len(invalid_files) == 0:
    print('All JSON files are valid!')
  else:
    print('The following JSON files are invalid :')
    for invalid_file in invalid_files:
      print(invalid_file.replace('..', ''))
      sys.exit(2)


if __name__ == '__main__':
  main()
