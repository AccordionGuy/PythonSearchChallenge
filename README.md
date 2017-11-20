# Python Search Challenge

Given a CSV file with a column of search terms, this simple Python 3 application performs a Google search for each item that column and writes the URL for the first result in the adjacent column.


## Table of contents

* [Overview](overview)
* [Installation](installation)
* [Usage](usage)
* License(license)

## Overview

### Motivation
This application is my answer to a programming challenge given as part of a job application. I was applying for the position of Developer Marketing Manager at a company whose online service allows users to integrate or “glue” various web and other applications together to create new
functionality, without programming. I’ll leave it to you to guess who they are.

I didn’t land the job, but going through the challenge was still a worthwhile experience, and thought that my solution was worth sharing.

### What the application does
The challenge was to take a CSV file with the following contents…

![](http://www.globalnerdy.com/wordpress/wp-content/uploads/2017/03/initial-spreadsheet.jpg)

…and write an application that does the following for each non-heading row:

* Perform a Google search for the item in the first column
* Write the URL from the first result of that search into the second column

Once this has been done for all the rows, write the results into a new CSV file. For the example search terms, the resulting file should look like this:

![](http://www.globalnerdy.com/wordpress/wp-content/uploads/2017/03/final-spreadsheet.jpg)

## Installation

This application uses the [**google** Python package](https://pypi.python.org/pypi/google) to fetch search results from Google.

The simplest way to install this package is to use **pip**, the Python package manager. With pip, installing the google package is as simple as entering this at the command line:

~~~~
pip install google
~~~~

If for some reason you don’t have pip installed, you can go to the [google Python package page,](https://pypi.python.org/pypi/google) and download the tarred-and-gzipped package. At the time of this writing, its filename is **google-1.9.3.tar.gz**. Once you’ve downloaded it, you’ll have a new directory named **google-1.9.3**. From the command line, go into the directory and run setup.py using the following command:

~~~~
python setup.py install
~~~~

Once the google Python packahge is installed, you can simply run the script.

## Usage

To use the script, run it using the following command:

~~~~
python search_challenge.py input_file output_file
~~~~

where:

* *input_file* is the filename of the CSV file containing search terms.
* *output_file* is the filename of the output file that the application will create.

*output_file* is optional. If you don’t specify an output file, the application will assume that you want to overwrite the input file with the output file.

## License

This code is released under the [MIT license](https://opensource.org/licenses/MIT). Simply put, you're free to use this in your own projects, both personal and commercial, as long as you include the copyright notice below. It would be nice if you mentioned my name somewhere in your documentation or credits.