shumgrepper
===========

A web interface of summershum


Prerequisites
~~~~~~~~~~~~~
    * virtualenvwrapper

Install virtualenvwrapper::

   $ sudo yum install -y python-virtualenvwrapper

Create a virtualenv::

    $ mkvirtualenv shumgrepper
    $ workon shumgrepper
    
Install dependencies::

    $ pip install -r requirements.txt
    
Run shumgrepper
~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    $ python runserver.py
    
Query the database
~~~~~~~~~~~~~~~~~~~~~~~~~~

Query by sha1sum
In a browser, visit http://localhost:5000/sha1/<sha1sum>

Query by sha256sum
In a browser, visit http://localhost:5000/sha256/<sha256sum>

Query by md5sum
In a browser, visit http://localhost:5000/md5/<md5sum>

Query by tarsum
In a browser, visit http://localhost:5000/tar/<tarsum>

