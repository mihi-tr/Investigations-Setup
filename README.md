# Ipython notebook setup for investigations

## Requirements

* Virtualenv
* pip
* python2.7

## Installation

### Virtualenv and pip

```
easy_install pip
```

```
pip install virtualenv
```

### create and activate a virtualenv

```
virtualenv venv
source venv/bin/activate
```

### Install ipython notebook

```
pip install -r requirements.txt
```

### Install your database connector 

If you do postgres this would be

```
pip install psycopg2
```

Not needed if you work with sqlite

### Create a nbserver profile

```
ipython profile create nbserver
```

### Setup for the profile

```
python profile_setup.py
```

### Copy the sample procfile

```
cp Procfile.tmpl Procfile
```

Edit the Procfile to reflect your system

e.q whether you want to enable the ftpd or have the multi-user setup.

### Start the notebook

```
honcho start
```

### connect to your notebook

[http://localhost:8888](http://localhost:8888)

