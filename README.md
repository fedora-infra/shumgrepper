shumgrepper
===========

A web interface of summershum

Hacking on shumgrepper
----------------------

Prerequisites
~~~~~~~~~~~~~
    * virtualenvwrapper
    
Install virtualenvwrapper::

   $ sudo yum install -y python-virtualenvwrapper

Setting up the stack
~~~~~~~~~~~~~~~~~~~~

Create a virtualenv::

    $ mkvirtualenv shumgrepper
    $ workon shumgrepper

Install dependencies::

    $ pip install -r requirements.txt
 
   
Run shumgrepper
~~~~~~~~~~~~~~~~~~~~~~~~~~

    $ python runserver.py

Query the database
~~~~~~~~~~~~~~~~~~~~

Query by sha1sum::

   In a browser, visit http://localhost:5000/sha1sum/<sha1sum>

Query by sha256sum::

   In a browser, visit http://localhost:5000/sha256sum/<sha256sum>

Query by md5sum::

   In a browser, visit http://localhost:5000/md5sum/<md5sum>

Query by tarsum::

   In a browser, visit http://localhost:5000/tarsum/<tarsum>
In a browser, visit http://localhost:5000 to see the docs.
