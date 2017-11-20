# Python3

# Python Search Challenge
# =======================
# This is my answer to a programming challenge given as part of a job application for
# the position of Developer Marketing Manager at a a company whose online service allows
# users to integrate or “glue” various web and other applications together to create new
# functionality, without programming. I’ll leave it to you to guess who they are.
#
# The challenge was to take a CSV file with 2 columns...
#
# 1. Search Term: A column full of search terms. The first row should contain the title,
#    “Search Term”, and subsequent rows should contain words or phrases for which you
#    want to find the first Google result.
# 2. First Web Result: A column that will eventually contain the output of this program.
#    The first row should contain the title, “First Web Result”, and subsequent rows
#    should be empty.
#
# ...and write an application that does the following for each non-heading row:
# 
# 1. Perform a Google search for the item in the “Search Term” column, and then
# 2. Write the URL for the first result of that search into the “First Web Result” column.
#
# This application uses the “google” Python package, which is available at:
# https://pypi.python.org/pypi/google
# If you have pip installed on your system, you can install google by entering the following
# in your terminal:
# pip install google
#
# For copyright/licensing information, see the end of this file.
 
SEARCH_TERM = "Search Term"
RESULT = "First Web Result"

def read_input_file(file):
  IOERROR_MESSAGE = "ERROR: I/O Error. Couldn’t read from file \"%s\"."
  UNEXPECTED_ERROR_MESSAGE = "ERROR: Unexpected error - %s."
  import os
  rows = []
  if os.path.exists(file):
    try:
      import csv
      with open(file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
          if row[SEARCH_TERM].strip() != '': # Ignore rows without search terms
            rows.append(row)
        return rows
    except IOError:
      print(IOERROR_MESSAGE % input_file)
      raise SystemExit
    except Exception as e:
      # Handle all other exceptions.
      print(UNEXPECTED_ERROR_MESSAGE % str(e))
      raise SystemExit
  else:
    print("The file \"%s\" doesn't exist." % filename )
    raise SystemExit
 
def first_google_result_url(search_term):
  URLERROR_MESSAGE = "ERROR: urllib.error.URLError. Check the network connection; you’re probably offline."
  UNEXPECTED_ERROR_MESSAGE = "ERROR: Unexpected error - %s."
  import urllib
  from google import search
  try:
    for url in search(search_term, start=0, stop=1):
      break
    return url
  except urllib.error.URLError:
    # Handle "nodename nor servname provided, or not known" exception;
    # probably caused by being offline.
    print(URLERROR_MESSAGE)
    raise SystemExit
  except Exception as e:
    print(UNEXPECTED_ERROR_MESSAGE % str(e))
    raise SystemExit
    
def add_search_results(rows):
  num_rows = len(rows)
  print(f"Starting processing of {num_rows} rows of search terms.")
  current_row_index = 1
  for current_row in rows:
    print(f"Processing row {current_row_index} of {num_rows} -- Search term: {current_row[SEARCH_TERM]}")
    current_row[RESULT] = first_google_result_url(current_row[SEARCH_TERM])
    current_row_index += 1
  return rows
 
def write_output_file(rows, file):
  IOERROR_MESSAGE = "ERROR: I/O Error. Couldn’t write to file \"%s\"."
  UNEXPECTED_ERROR_MESSAGE = "ERROR: Unexpected error - %s."
  try:
    import csv
    new_file = open(file, 'w')
    with new_file:
      field_names = [SEARCH_TERM, RESULT]
      writer = csv.DictWriter(new_file, fieldnames = field_names)
      writer.writeheader()
      writer.writerows(rows)
  except IOError:
    print(IOERROR_MESSAGE % file)
    raise SystemExit
  except Exception as e:
    print(UNEXPECTED_ERROR_MESSAGE % str(e))
    raise SystemExit
 
def main():
  import sys
  if len(sys.argv) == 2:
    (input_file, output_file) = (sys.argv[1], sys.argv[1])
  elif len(sys.argv) == 3:
    (input_file, output_file) = (sys.argv[1], sys.argv[2])
  else:
    print("Usage: python search_challenge.py [input_file] [output_file]")
    print("If no output file is specified, the input file will be used as the output file.")
    raise SystemExit
  input_file_rows = read_input_file(input_file)
  output_file_rows = add_search_results(input_file_rows)
  write_output_file(output_file_rows, output_file)
 
 
if __name__ == '__main__': 
  main()


# This code is released under the MIT license.
# Simply put, you're free to use this in your own projects, both
# personal and commercial, as long as you include the copyright notice below.
# It would be nice if you mentioned my name somewhere in your documentation
# or credits.
#
# MIT LICENSE
# -----------
# (As defined in https:#opensource.org/licenses/MIT)
#
# Copyright © 2017 Joey deVilla. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom
# the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.