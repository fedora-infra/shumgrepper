Overview
""""""""

Shumgrepper queries from summershum's database which collects the md5sum, sha1sum,
sha256sum of every file present in every package in Fedora. Shumgrepper will allow you to
query by shum values like sha1sum, sha256sum, md5sum and tar_sum, find the files bundled within
a package, compare different packages and tar_files, detect how many different copies of GPL license
are present.

User Interface
""""""""""""""

Query by hashes
```````````````
This will return all the files in all the package matching this hash sum.

sha1sum
```````
.. code-block:: javascript

    http://209.132.184.120/sha1/<sha1sum>

sha256sum
`````````

.. code-block:: javascript

    http://209.132.184.120/sha256/<sha256sum>

tarsum
``````

.. code-block:: javascript

    http://209.132.184.120/tar_sum/<tarsum>

md5sum
``````
.. code-block:: javascript

    http://209.132.184.120/md5/<md5sum>

Packages List
`````````````

This will list all the packages where each package links to its overview page.

.. code-block:: javascript

    http://209.132.184.120/packages

Package Overview
""""""""""""""""

It will give the package overview by displaying the different versions of the package::

    http://209.132.184.120/package/<package>

Files within a package
""""""""""""""""""""""

It determines the files bundled within a package. It returns
file names for the files contained within a package::

    http://209.132.184.120/package/<package>/filenames

Files of a package version
""""""""""""""""""""""""""

In order to get the files of a specific package version, you will have to query
by tar_file. It returns file names for the files contained within a tar_file::

    http://209.132.184.120/tar_file/<tar_file>/filenames

Query by filename
"""""""""""""""""

It will return all the file details matching this filename::

    http://209.132.184.120/filename/<filename>



Compare two or more tar_files
"""""""""""""""""""""""""""""

Common files
````````````

It compares two or more tar_files by comparing the sha256sum of the filenames
present in all the tar_files and returns common files present in them along with their sha256sum::

    http://209.132.184.120/compare/common?tar_file={tar_file1}& \
        tar_file={tar_file2}

Example::

    http://localhost:5000/compare/common?tar_file=fedora-release-21.tar.bz2& \
        tar_file=fedora-release-22.tar.bz2

It will return a table with common sha256sum values and the filenames corresponding to each
package matching that sha256sum.

Different files
```````````````

It compares two or more tar_files by comparing sha256sum values of the filenames
present in all the packages and returns different files present in them::

    http://209.132.184.120/compare/difference?tar_file={tar_file1} \
        tar_file={tar_file2}


It returns a table where each column represents a tar_file and one column contains different
sha256sum. If a tar_file contains that sha256sum, then filename will be listed corresponding
to that shasum otherwise it is left blank.

Example::

    http://localhost:5000/compare/difference?tar_file=fedora-release-21.tar.bz2& \
        tar_file=fedora-release-22.tar.bz2
