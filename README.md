# api_environment_setup

A tutorial for setting up a Python environment on a Windows PC, connecting to the ArchivesSpace API, and making bulk updates using a spreadsheet as input. Also a brief mention of retrieving data from the ArchivesSpace MySQL database.

## Requirements

* miniconda
* `requests` package
<!-- * `aspace_tools` package -->

## Installing Miniconda

* If you already have the full version of Anaconda, [uninstall](https://docs.anaconda.com/anaconda/install/uninstall/) it
* [Download](https://docs.conda.io/en/latest/miniconda.html) Miniconda
* Follow the setup instructions. Store the program in your home directory (i.e. C:\Users\your_username\Miniconda3). If you choose not to add Miniconda to your PATH, you will need to use the Anaconda Prompt to interact with the interpreter and run scripts from the command line.
* After the program is installed, click on the Windows start menu and open the Anaconda Prompt (it may be called Anaconda Powershell)
* To further check your installation, type `echo $PATH` into the prompt. You should see some Miniconda-related directories.

## Setting up your environment

To see what Python packages are currently installed, type `conda list` into the prompt.

To install the latest version of `requests`, open an Anaconda prompt window and enter `conda install requests`.
<!-- To install the `aspace_tools` package enter `git clone https://github.com/yalemssa/aspace_tools`. Then navigate to the top-level package directory and enter `pip install .` -->

## Working in the Python interpreter

Open the Anaconda Prompt and enter `python`. This will open the Python interpreter. To run yet another check on your Python installation, enter `import sys`. Then, enter `sys.executable`. You should see the path to your Miniconda Python executable.

To close the Python interpreter and return to the prompt, enter `quit()`

## Running Python scripts from the command line

You can also run `.py` files from the Anaconda Prompt. To run the `hello_world.py` file, `cd` to the `demo_files` directory in the prompt and type `python hello_world.py`.

## Connecting to ArchivesSpace via `requests`

To verify your `requests` installation, open a Python interpreter and enter `import requests` into the interpreter. You should not see any return value on the screen, just a `>>>` prompt. <!-- Follow the same steps to verify `aspace_tools`. -->

To connect to the ArchivesSpace API, you first need to enter your credentials into the `config.json` file included in the `demo_files` directory. Then open a python interpreter session and enter `import archivesspace_login as as_login` (be sure that you are in the `demo_files` directory before you open the interpreter). Then enter the following into the interpreter:

```
>>> import requests
>>> api_url, headers = as_login.login()
Login successful!
>>> api_url
https://archivesspace.univesity.edu
>>> headers
LONGSTRINGOFNUMBERSANDLETTERSREPRESENTINGAUTHKEY
```

If your login credentials are invalid you should be prompted to enter them again into the interpreter. If your login credentials were accepted, you can send your first request to the ArchivesSpace API by entering the following into the Python interpreter:

```




```

A JSON response for an archival object looks like this:

```



```

JSON objects are treated essentially like Python [dictionaries](https://realpython.com/python-dicts/), which means that Python comes with a variety of built-in ways to manipulate the data that comes from ArchivesSpace.

## Creating and updating ArchivesSpace data via the API

The obvious advantage of the ArchivesSpace API is that it enables users to create and update ArchivesSpace records in bulk. The primary input for these bulk updates are CSV spreadsheet files. An example file which might be used to update multiple archival objects  

## Retrieving ArchivesSpace data with MySQL

The fastest and most straightforward way to retrieve data from ArchivesSpace is via the MySQL database. Retrieving data from the API is much slower, and it takes extra work to manipulate the JSON response into the spreadsheet formats that many archivists rely on use to create and update archival description.
<!-- ## Using the `aspace_tools` package to perform CRUD actions against the API and database

 -->

## Helpful Resources

* RealPython [Introduction to Python](https://realpython.com/learning-paths/python3-introduction/) learning path
* [Setting up a miniconda environment](https://medium.com/dunder-data/anaconda-is-bloated-set-up-a-lean-robust-data-science-environment-with-miniconda-and-conda-forge-b48e1ac11646)
* [Python for Archivists](https://practicaltechnologyforarchives.org/issue7_wiedeman/)