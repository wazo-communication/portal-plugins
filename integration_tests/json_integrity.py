#!/usr/bin/env python3
# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import glob
import sys

def is_valid_json(data):
  try:
    json.loads(data)
  except ValueError:
    return False
  return True

def read_file(file_path):
  file = open(file_path, 'r')
  content = file.read()
  file.close()
  return content

def main():
  file_paths = glob.glob("../**/*.json", recursive=True)
  invalid_files = []

  for file_path in file_paths:
    content = read_file(file_path)
    if is_valid_json(content) == False:
      invalid_files.append(file_path)

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
