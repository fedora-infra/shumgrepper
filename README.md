shumgrepper
===========

A web interface of summershum

Hacking on shumgrepper
----------------------

###Prerequisites
    * virtualenvwrapper
    
#####Install virtualenvwrapper:

    $ sudo yum install -y python-virtualenvwrapper

###Setting up the stack

#####Create a virtualenv:

    $ mkvirtualenv shumgrepper
    $ workon shumgrepper

#####Install dependencies:

    $ pip install -r requirements.txt
 
#####Setting up database:
  
Clone summershum repository https://github.com/fedora-infra/summershum:
    
    $ cd summershum
    $ python setup.py build
    $ python setup.py install
    $ summershum-cli
    
    
###Run shumgrepper

    $ python runserver.py

###Query the database

#####by sha1sum:

In a browser, visit http://localhost:5000/sha1/{sha1sum}

#####by sha256sum:

In a browser, visit http://localhost:5000/sha256/{sha256sum}

#####by md5sum:

In a browser, visit http://localhost:5000/md5/{md5sum}

#####by tarsum:

In a browser, visit http://localhost:5000/tar/{tarsum}
