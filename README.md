ban2stats
============

Stats for Fail2Ban (for relational database)

#Overview

   See diagram at https://github.com/prontodev/ban2stats/blob/master/docs/Ban2Stats_diagram.pdf

### Ban2Stats Web Service
   Ban2Stats Web Service is a Django web application and also use Haystack to connect with ElasticSearch.

### Ban2Stats Web Page
   A static web page that display Statistics from Ban2Stats Web Service.

### Ban2Stats Client
   is a Python script that makes HTTP Request to Ban2Stats web service API. The client is used by Fail2Ban hook.

### ElasticSearch
   ElasticSearch is used to do search and indexing for Ban2Stats Web Service

Installation
------------

#. Install following libraries::

    geos
    elasticsearch
    python


#. Create an empty virtualenv and install more library using Pip::

    pip install -r ban2stats/ban2stats/setup/requirements.txt


Configuration
-------------

    create local.py under ban2stats/ban2stats/settings/
    - database configuration
    - ElasticSearch configuration (HAYSTACK_CONNECTIONS)
    - BAN2STATS_SERVICE_TOKEN (should match with client's TOKEN)

    In ban2stats/client/webservice_client.py
    - WEBSERVICE_HOST
    - TOKEN (should match with Banstats's BAN2STATS_SERVICE_TOKEN in settings)

    In ban2stats/webpage/index.html
    - api_host

Run
---

#. ElasticSearch
   Run ElasticSearch

#. Ban2Stats Web Service
   Run Ban2Stats

#. Ban2Stats Web Page
   You can run this using any static web server.

   if you want to run it using Python

   python -m SimpleHTTPServer 80



