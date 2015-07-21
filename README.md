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

    $ python setup.py build

#####Install shumgrepper (if desired)

    $ python setup.py install
 
#####Setting up database:
  
Clone summershum repository https://github.com/fedora-infra/summershum:
    
    $ cd summershum
    $ python setup.py build
    $ python setup.py install
    $ summershum-cli
    
    
###Run shumgrepper

    $ python runserver.py
