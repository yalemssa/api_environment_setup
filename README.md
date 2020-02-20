# api_environment_setup

A tutorial for setting up a Python environment on a Windows PC, connecting to the ArchivesSpace API, and making bulk updates using a spreadsheet as input. Also a brief mention of retrieving data from the ArchivesSpace MySQL database, and a note on safety tips.

To get started, clone or download this repository.

## Requirements

* Miniconda
* Access to ArchivesSpace API and/or MySQL database
<!-- * `aspace_tools` package -->

## Why Miniconda?

While many computers come with Python built-in, it is often many versions behind the latest release. Also, installing or upgrading Python packages in the system installation of Python can cause unexpected conflicts and errors within existing programs. It is highly recommended that you use a virtual environment to avoid these issues. 

There are many varieties of virtual environments, each with their own benefits and drawbacks. Anaconda and Miniconda are frequently used by data scientists and others who work with data (such as archivists!), and they come with frequently-used data processing packages preinstalled. Miniconda is a lightweight version of Anaconda, and both are based on `conda`. A good intro to `conda` can be found [here](https://towardsdatascience.com/getting-started-with-python-environments-using-conda-32e9f2779307).

## Installing Miniconda

* If you already have the full version of Anaconda, [uninstall](https://docs.anaconda.com/anaconda/install/uninstall/) it
* [Download](https://docs.conda.io/en/latest/miniconda.html) Miniconda
* Follow the setup instructions. Store the program in your home directory (i.e. C:\Users\your_username\Miniconda3). If you choose, per the installer's recommendations, not to add Miniconda to your PATH, you will need to use the Anaconda Prompt or Anaconda Powershell to interact with the interpreter and run scripts from the command line.
* After the program is installed, click on the Windows start menu and open the Anaconda Prompt or Anaconda Powershell.
<!-- * To further check your installation, type `echo $PATH` into the prompt. You should see some Miniconda-related directories.
 -->

## Setting up your environment

To see what Python packages are currently installed, type `conda list` into the prompt. You should see that `requests` is already installed. If it is not, enter `conda install requests` into the Anaconda prompt.

<!-- To install the `aspace_tools` package enter `git clone https://github.com/yalemssa/aspace_tools`. Then navigate to the top-level package directory and enter `pip install .` -->

## Working in the Python interpreter

Open the Anaconda Prompt and enter `python`. This will open the Python interpreter. To check the location of your Python installation, enter `import sys`. Then, enter `sys.executable`. You should see the path to your Miniconda Python executable.

To close the Python interpreter and return to the prompt, enter `quit()`

## Running Python scripts from the command line

You can also run `.py` files from the Anaconda Prompt. To run the `hello_world.py` file, enter the following into the Anaconda Prompt:

```
user$ cd C:\Users\your_username\path\to\api_environment_setup\demo_files
demo_files user$ python hello_world.py

...stuff happens...

```

## Connecting to ArchivesSpace via `requests`

To connect to the ArchivesSpace API, you first need to enter your credentials into the `config.json` file included in the `demo_files` directory (use the ArchivesSpace TEST instance for the api_url value). Then open a python interpreter session and enter the following into the interpreter (be sure that you are still in the `demo_files` directory before you open the interpreter):

```
>>> import json
>>> import requests
>>> import archivesspace_login as as_login
>>> api_url, headers = as_login.login()
Login successful!
>>> api_url
https://archivesspace.univesity.edu
>>> headers
LONGSTRINGOFNUMBERSANDLETTERSREPRESENTINGAUTHKEY
```

If your login credentials are invalid you should be prompted to enter them again into the interpreter. If your login credentials were accepted, you can send your first request to the ArchivesSpace API by entering the following into the Python interpreter:

```
>>> repo_id = <YOUR ARCHIVESSPACE REPOSITORY ID>
>>> list_of_resources = requests.get(f"{api_url}/repositories/{repo_id}/resources", headers=headers).json()
>>> print(list_of_resources)
{
	list of resources
}
```

## Creating and retrieving an ArchivesSpace resource record

A JSON template for a resource looks like this:

```



```

## Creating and retrieving an ArchivesSpace top container record

A JSON template for a top container looks like this. Only xx fields are required

JSON objects are treated essentially like Python [dictionaries](https://realpython.com/python-dicts/), which means that Python comes with a variety of built-in ways to manipulate the data that comes from ArchivesSpace.

One challenge in working with ArchivesSpace JSON objects is that they are frequently nested. It is helpful to keep the following in mind:

* subrecords are usually repeatable and are contained in lists
* many records are linked to other records via URI refs, which are stored as nested dictionaries.

## Creating and updating ArchivesSpace data in bulk via the API

The obvious advantage of the ArchivesSpace API is that it enables users to create and update ArchivesSpace records in bulk. The primary input for these bulk updates are CSV spreadsheet files. An example file which might be used to update multiple archival objects  

## Retrieving ArchivesSpace data with MySQL

The fastest and most straightforward way to retrieve data from ArchivesSpace is via the MySQL database. Retrieving data from the API is much slower, and it takes extra work to manipulate the JSON response into the spreadsheet formats that many archivists rely on use to create and update archival description.
<!-- ## Using the `aspace_tools` package to perform CRUD actions against the API and database

 -->

## Safety Tips

Creating and updating records via the ArchivesSpace API is fast and convenient, but can be dangerous. There is no undo button, and problems can have cascading effects. In order to prevent errors that may take significant effort to identify and remedy, please follow these guidelines:

* Before running any updates against the API, have another staff member review your:
	* Input data
	* Code
	* Output
* __ALWAYS__ run your updates in TEST or DEV before running in production
* Keep all JSON backups, log files, input data, and code. Organize your files by project/task. Document any and all actions you take. Due to the lack of an "edit history" in ArchivesSpace, it can be difficult to trace the source of data quality issues.

## Helpful Resources

* ArchivesSpace API [Documentation](http://archivesspace.github.io/archivesspace/api/)
* RealPython [Python Data Types](https://realpython.com/python-data-types/)
* RealPython [An Effective Python Environment: Making Yourself at Home](https://realpython.com/effective-python-environment/)
* RealPython [Running Python Scripts](https://realpython.com/run-python-scripts/)
* RealPython [Python Dictionaries](https://realpython.com/python-dicts/)
* RealPython [Introduction to Python](https://realpython.com/learning-paths/python3-introduction/) learning path
* [Setting up a miniconda environment](https://medium.com/dunder-data/anaconda-is-bloated-set-up-a-lean-robust-data-science-environment-with-miniconda-and-conda-forge-b48e1ac11646)
* [Python for Archivists](https://practicaltechnologyforarchives.org/issue7_wiedeman/)