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

You can also run `.py` files from the Anaconda Prompt. To run the `hello_world.py` file, open the Anaconda Prompt/Powershell and do the following:

```
user$ cd C:\Users\your_username\path\to\api_environment_setup\demo_files
demo_files user$ python hello_world.py

...stuff happens...

demo_files user$
```

## Connecting to ArchivesSpace via `requests`

To connect to the ArchivesSpace API, you first need to enter your credentials into the `config.json` file included in the `demo_files` directory (use the ArchivesSpace TEST API URL for the api_url value - ask Alicia if you don't know the URL). Then open the Anaconda Prompt/Powershell (be sure that you are still in the `demo_files` directory before you open the interpreter) and do the following:

```
demo_files user$ python
Python 3.7.3 (default, Mar 27 2019, 16:54:48) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda custom (64-bit) on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import json
>>> import requests
>>> import archivesspace_login as as_login
>>> api_url, headers = as_login.login()
Login successful!
>>> api_url
https://archivesspace.university.edu/api
>>> headers
LONGSTRINGOFNUMBERSANDLETTERSREPRESENTINGAUTHKEY
```

If your login credentials are invalid you should be prompted to enter them again into the interpreter. If your login credentials were accepted, you can send your first API request - to retrieve a top container JSON record - by entering the following into the Python interpreter:

```
>>> import pprint
>>> top_container_uri = <URI of top container record>
>>> top_container_json = requests.get(f"{api_url}/{top_container_uri}", headers=headers).json()
>>> pprint.pprint(top_container_json)
{'active_restrictions': [],
 'barcode': '39002102377802',
 'collection': [{'display_string': 'Rights and Wrongs records',
                 'identifier': 'MS 1821',
                 'ref': '/repositories/12/resources/4869'}],
 'container_locations': [],
 'container_profile': {'ref': '/container_profiles/113'},
 'create_time': '2016-10-14T19:31:11Z',
 'created_by': 'cconnoll',
 'display_string': 'Box 153D: Series 4 [39002102377802]',
 'ils_holding_id': '6879939',
 'indicator': '153D',
 'is_linked_to_published_record': True,
 'jsonmodel_type': 'top_container',
 'last_modified_by': 'amd243',
 'lock_version': 7,
 'long_display_string': 'MS 1821, Series 4, Box 153D [39002102377802], video '
                        'Beta',
 'repository': {'ref': '/repositories/12'},
 'restricted': True,
 'series': [{'display_string': 'Programs, 1993-1996',
             'identifier': '4',
             'level_display_string': 'Series',
             'publish': True,
             'ref': '/repositories/12/archival_objects/2012461'}],
 'system_mtime': '2019-10-29T12:53:50Z',
 'type': 'Box',
 'uri': '/repositories/12/top_containers/239815',
 'user_mtime': '2018-09-28T13:04:43Z'}

```

Top containers and all other "top level" ArchivesSpace records (a very brief overview of "top level" records and the AS data model can be found in the second section of this [article](https://journal.code4lib.org/articles/14443)) can be accessed via the API by unique URIs, which correspond with their database identifiers. Top containers are scoped to repositories, and so the URI also includes the repository number, for instance `/repositories/12/top_containers/32918`. See the ArchivesSpace API documentation for more detailed explanations of how URIs and other parameters are formulated.

<!-- ## Creating and retrieving an ArchivesSpace resource record

A JSON template for a resource looks like this:

```

``` -->

## Updating a single top container indicator

JSON objects are treated essentially like Python [dictionaries](https://realpython.com/python-dicts/), which means that Python comes with a variety of built-in ways to manipulate the data that comes from ArchivesSpace.

Updating top container indicators (changing box numbers) is straightforward, as the indicator field is non-repeatable string value that is located at the top level of the record (i.e. it is not nested in a list or other dictionary).

To update an existing top container indicator, open a Python interpreter session (be sure you are in the `demo_files` directory) and execute the following code:

```
>>> import requests
>>> import json
>>> import traceback
>>> import archivesspace_login as as_login
>>> api_url, headers = as_login.login()
>>> top_container_uri = <URI of the container to update>
>>> top_container_json = requests.get(f"{api_url}/{top_container_uri}", headers=headers).json()
>>> top_container_json['indicator'] = '26'
>>> post_record = requests.post(f"{api_url}/{top_container_uri}", headers=headers, json=top_container_json).json()
>>> print(post_record):
{'status': 'updated', 'uri': }
>>>
```

## Preparing data for bulk upload

You can update ArchivesSpace data in bulk with Python using a spreadsheet as input. To update a top container indicator you only need the URI of the top container and the new box number. However, you may also want to include the old box number in your spreadsheet so that you can keep track of the previous value while preparing your data and to have a record if something goes wrong.

The easiest way to retrieve existing data from ArchivesSpace and prepare it for update is via the MySQL database. Retrieving data from the API is much slower, and it takes extra work to manipulate the JSON response into the spreadsheet formats that many archivists rely on use to create and update archival description. Here is a sample query for retrieving top container indicators for two series within a single collection:

```
select DISTINCT CONCAT('/repositories/', tc.repo_id, '/top_containers/', tc.id) as uri
	, tc.indicator as old_box_number
from archival_object ao
left join archival_object ao2 on ao2.id = ao.parent_id
left join archival_object ao3 on ao3.id = ao2.parent_id
left join instance on instance.archival_object_id = ao.id
left join sub_container sc on sc.instance_id = instance.id
left join top_container_link_rlshp tclr on tclr.sub_container_id = sc.id
left join top_container tc on tclr.top_container_id = tc.id
LEFT JOIN enumeration_value ev2 on ev2.id = tc.type_id
where ao.root_record_id = 4869
and (ao.parent_id = 2012449 or ao2.parent_id = 2012461)
and tc.id is not null
ORDER BY CAST(tc.indicator AS UNSIGNED)
```

After running this query you can export the results as a CSV. Open the file and add a column called 'new_box_number'. Then you can fill in the column with the new box number. Save the CSV file.

## Updating top container indicators in bulk

Opening your CSV file and using it to update multiple top container indicators takes only a few more lines of code than the previous example. To perform the update, import your modules, connect to the ArchivesSpace API, and execute the following code in a Python interpreter:

```
>>> with open('C:\\Username\\Path\\To\\File.csv', 'r', encoding='utf-8') as csvfile:
...		csvreader = csv.reader(csvfile)
...		next(csvreader, None)
...		for row in csvreader:
...			top_container_uri = row[0]
...			new_box_number = row[2]
...			try:
...				top_container_json = requests.get(f"{api_url}/{top_container_uri}", headers=headers).json()
...				top_container_json['indicator'] = new_box_number
...				post_record = requests.post(f"{api_url}/{top_container_uri}", headers=headers, json=top_container_json).json()
...				print(post_record)
...			except:
...				print(traceback.format_exc())
...				continue
...
<OUTPUT>
>>>
```

This code is also saved in the `update_top_container_indicator.py` file so it can be run from the Anaconda Prompt. Be aware that this code requires that the top container URI be in the first column of the spreadsheet, the old box number in the second column, and the new box number in the third. There are other methods which rely on a column title to look up the values, but the method above is slightly more straightforward for beginners.

## Creating and updating subrecords

<!-- extent types -->

## Creating and updating notes

<!-- scope and content notes -->

<!-- 

One challenge in working with ArchivesSpace JSON objects is that they are frequently nested. It is helpful to keep the following in mind:

* subrecords are usually repeatable and are contained in lists
* many records are linked to other records via URI refs, which are stored as nested dictionaries.

## Creating and updating ArchivesSpace data in bulk via the API

The obvious advantage of the ArchivesSpace API is that it enables users to create and update ArchivesSpace records in bulk. The primary input for these bulk updates are CSV spreadsheet files. An example file which might be used to update multiple archival objects  

## Retrieving ArchivesSpace data with MySQL

<-- ## Using the `aspace_tools` package to perform CRUD actions against the API and database-->

## Safety Tips

Creating and updating records via the ArchivesSpace API is fast and convenient, but can be dangerous. There is no undo button, and problems can have cascading effects. In order to prevent errors that may take significant effort to identify and remedy, please follow these guidelines:

* When running any updates against the API, have another staff member review your:
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
