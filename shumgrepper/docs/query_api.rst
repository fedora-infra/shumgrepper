Prerequisites
-------------

In order to interact with JSON API, you need to install `HTTPie
<https://github.com/jkbr/httpie#httpie-a-cli-curl-like-tool-for-humans>`_ command line tool. 

``$ sudo yum -y install httpie``

Requesting data by hashes
-------------------------

It returns the files having the specified hash-sum. The files contain the values of filename, package name, md5sum, sha1sum, sha256sum, tar_sum, tar_file matching that particular hash-sum.

**sha1sum**::

    $ http get http://localhost:5000/sha1/<sha1sum>

**sha256sum**::

    $ http get http://localhost:5000/sha256/<sha256sum>

**tarsum**::

    $ http get http://localhost:5000/tar/<tarsum>

**md5sum**::

    $ http get http://localhost:5000/md5sum/<md5sum>

Results
-------

Querying files data by sha1sum::

    $ http get http://localhost:5000/sha1/f83618056ae5601b74a75db03739dd3ec24292f5

.. code-block:: javascript

    [
        {
            "filename": "/appstream-glib-0.1.5/docs/api/html/AsRelease.html",
            "md5sum": "2729be6d3a3a9c997a27b33e0ca79ff9",
            "pkg_name": "libappstream-glib",
            "sha1sum": "f83618056ae5601b74a75db03739dd3ec24292f5",
            "sha256sum": "5953834e0eb38282012f6f8c964b89219659e3d3834d9a9edd812e0ad3f1acc7",
            "tar_file": "appstream-glib-0.1.5.tar.xz",
            "tar_sum": "a84aeb3560b4813ba3a7533728ed4a69"
        }
    ]


Files of a package
------------------

It determines the files bundled within a packae.It returns
file-names of the files contained within a package::

    $ http get http://localhost:5000/package/<package>/filenames

Results
-------

.. code-block:: javascript

    $ http get http://localhost:5000/package/tito/filenames

.. code-block:: javascript

    [
        "/tito-0.5.4/wercker.yml", 
        "/tito-0.5.4/titorc.5.asciidoc", 
        "/tito-0.5.4/AUTHORS", 
        "/tito-0.5.4/.gitignore", 
        "/tito-0.5.4/.gitattributes", 
        "/tito-0.5.4/test/functional/__init__.py", 
        "/tito-0.5.4/test/functional/specs/extsrc.spec", 
        "/tito-0.5.4/src/tito/exception.py", 
        "/tito-0.5.4/src/tito/distributionbuilder.py", 
        "/tito-0.5.3/test/functional/builder_tests.py", 
        "/tito-0.5.3/test/functional/build_gitannex_tests.py", 
        "/tito-0.5.3/src/tito/common.py", 
        "/tito-0.5.3/src/tito/cli.py", 
        "/tito-0.5.3/src/tito/buildparser.py", 
        "/tito-0.5.3/src/tito/release/main.py", 
        "/tito-0.5.3/src/tito/release/copr.py", 
        "/tito-0.5.3/src/tito/release/__init__.py", 
        "/tito-0.5.3/hacking/titotest-centos-6.4/Dockerfile", 
        "/tito-0.5.3/hacking/titotest-centos-5.9/Dockerfile", 
        "/tito-0.5.5/src/tito/tagger/zstreamtagger.py", 
        "/tito-0.5.5/src/tito/tagger/rheltagger.py", 
        "/tito-0.5.5/src/tito/tagger/main.py", 
        "/tito-0.5.5/src/tito/tagger/__init__.py", 
        "/tito-0.5.5/src/tito/release/obs.py", 
        "/tito-0.5.5/src/tito/release/main.py", 
        "/tito-0.5.5/src/tito/release/copr.py", 
        "/tito-0.5.5/src/tito/release/__init__.py", 
        "/tito-0.5.5/rel-eng/custom/custom.py", 
        "/tito-0.5.5/hacking/runtests.sh", 
        "/tito-0.5.5/bin/tar-fixup-stamp-comment.pl", 
        "/tito-0.5.5/bin/generate-patches.pl"
    ]

Compare two or more packages
----------------------------

It compares two or more packages given by user and compare their shasum 
and returns the common files present in all the packages::

    $ http get http://localhost:5000/compare \
        packages=={package1} \
        packages=={package2}

Results
-------

.. code-block:: javascript

    $ http get http://localhost:5000/compare \
        packages==libappstream-glib \
        packages==epiphany

.. code-block:: javascript

    [
        "/epiphany-3.12.1/m4/ltversion.m4", 
        "/epiphany-3.12.1/po/Makefile.in.in", 
        "/epiphany-3.12.1/m4/intltool.m4", 
        "/epiphany-3.12.1/help/es/es.stamp", 
        "/epiphany-3.12.1/help/fr/fr.stamp", 
        "/epiphany-3.12.1/help/el/el.stamp", 
        "/epiphany-3.12.1/help/hu/hu.stamp", 
        "/epiphany-3.12.1/help/de/de.stamp", 
        "/epiphany-3.12.1/help/pt_BR/pt_BR.stamp", 
        "/epiphany-3.12.1/help/cs/cs.stamp", 
        "/epiphany-3.12.1/help/ru/ru.stamp", 
        "/epiphany-3.12.1/ltmain.sh", 
        "/epiphany-3.12.1/m4/ltsugar.m4", 
        "/epiphany-3.12.1/m4/ltoptions.m4", 
        "/epiphany-3.12.1/m4/lt~obsolete.m4"
    ]

