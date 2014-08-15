Overview
========

Shumgrepper queries from summershum's database which collects the md5sum, sha1sum,
sha256sum of every file present in every package in Fedora. Shumgrepper will allow you to
query by shum values like sha1sum, sha256sum, md5sum and tar_sum, find the files bundled within
a package, compare different packages and tarballs, search for a package and get the
history of a package.

User Interface
==============

Query by hashes
---------------
This will return all the files in all the package matching this hash sum.

sha1sum
```````

The **/sha1/<sha1sum>** endpoint will returns files matching this sha1sum.

Example::

    /sha1/f83618056ae5601b74a75db03739dd3ec24292f5


sha256sum
`````````

The **/sha1/<sha256sum>** endpoint will returns files matching this sha256sum.

Example::

    /sha256/e77b543aefd1595f159e541041a403c48a240913bc65ca5c4267df096f775eb6


tarsum
``````

The **/tar_sum/<tar_sum>** endpoint will returns files matching this tar_sum.

Example::

    /tar_sum/4a31a53097eaf029df45dd36ab622a57


md5sum
``````

The **/md5/<md5sum>** endpoint will returns files matching this md5sum.

Example::

    /md5/f4aafb270c2f983f35b365aad5fe8870


Packages List
-------------

The **/packages** endpoint will list all the packages where each package
links to its overview page.


Package Overview
----------------

The **/package/<package>** endpoint will give the package overview by displaying
the different versions of the package.

Example::

    /package/fotoxx


Files within a package
----------------------

The **/package/<package>/filenames** determines the files bundled within a package.
It returns file names for the files contained within a package.

Example::

    /package/felix-gogo-command/filenames


Files of a package version
--------------------------

In order to get the files of a specific package version, you will have to query
by tarball. The **/tarball/<tarball>/filenames** endpoint returns file names for
the files contained within a tarball.

Example::

    /tarball/fotoxx-14.05.1.tar.gz/filenames


Query by filename
-----------------

The **/filename/<filename>** endpoint will return all the file details matching this filename.

Example::

    /filename/appstream-glib-0.1.1%2Fdocs%2Fapi%2Fhtml%2FAsRelease.html


History of a package
--------------------

The **/history/<package>** endpoint will give you the evolution of a package across its different versions. This will return a table
which will display the files that are common to different versions and files that have changed along with
their sha256sum.

Example::

    /history/fedora-repos


Compare two or more tarballs
-----------------------------

Common files
````````````

It compares two or more tarballs by comparing the sha256sum of the filenames
present in all the tarballs and returns common files present in them along with their sha256sum::

    /compare/common?tarball={tarball1}&tarball={tarball2}

Example::

    /compare/common?tarball=fedora-release-21.tar.bz2& \
        tarball=fedora-release-22.tar.bz2

It will return a table with common sha256sum values and the filenames corresponding to each
package matching that sha256sum.


Different files
```````````````

It compares two or more tarballs by comparing sha256sum values of the filenames
present in all the packages and returns different files present in them::

    /compare/difference?tarball={tarball1} \
        tarball={tarball2}


It returns a table where each column represents a tarball and one column contains different
sha256sum. If a tarball contains that sha256sum, then filename will be listed corresponding
to that shasum otherwise it is left blank.

Example::

    /compare/difference?tarball=fedora-release-21.tar.bz2& \
        tarball=fedora-release-22.tar.bz2

