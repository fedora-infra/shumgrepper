Requesting data by hashes
-------------------------

It returns the files with the specified hash sum. The files retrieved contain the values of filename, package name,
md5sum, sha1sum, sha256sum, tar_sum, tar_file matching that particular hash sum.

sha1sum
"""""""

.. code-block:: javascript

    http://209.132.184.120/api/sha1/<sha1sum>

Sample Results
""""""""""""""

Querying files data by sha1sum::

    http://209.132.184.120/api/sha1/e0ec2c54e7a4fabb2f7e8c78d711efc0ed5f4f43

.. code-block:: javascript

    [
        {
            "filename": "/appstream-glib-0.1.5/libappstream-glib/Makefile.in", 
            "md5sum": "d3c107b29d2ed94b8db1cd3d42bf8f71", 
            "pkg_name": "libappstream-glib", 
            "sha1sum": "e0ec2c54e7a4fabb2f7e8c78d711efc0ed5f4f43", 
            "sha256sum": "a0ceb8c8f1f3316562e0370ee280789d626813458fc1da69102b9575a63fabb1", 
            "tar_file": "appstream-glib-0.1.5.tar.xz", 
            "tar_sum": "a84aeb3560b4813ba3a7533728ed4a69"
        }
    ]


sha256sum
"""""""""

.. code-block:: javascript

    http://209.132.184.120/api/sha256/<sha256sum>

Sample Results
""""""""""""""

Querying files data by sha256sum::

    http://209.132.184.120/api/sha256/e77b543aefd1595f159e541041a403c48a240913bc65ca5c4267df096f775eb6

.. code-block:: javascript

    [
        {
            "filename": "/Jinja2-2.7.3/jinja2/compiler.py", 
            "md5sum": "8a0591fb2854f14dd3a3f9e173482a03", 
            "pkg_name": "python-jinja2", 
            "sha1sum": "eb651ef64e5579c6bb7ed0a72de9ed48684be73b", 
            "sha256sum": "e77b543aefd1595f159e541041a403c48a240913bc65ca5c4267df096f775eb6", 
            "tar_file": "Jinja2-2.7.3.tar.gz", 
            "tar_sum": "b9dffd2f3b43d673802fe857c8445b1a"
        }
    ]

tarsum
""""""

.. code-block:: javascript

    http://209.132.184.120/api/tar_sum/<tarsum>

Sample Results
""""""""""""""

Querying files data by tarsum::

    http://209.132.184.120/api/tar_sum/4a31a53097eaf029df45dd36ab622a57

.. code-block:: javascript

    [
        {
            "filename": "/kpty-4.100.0/autotests/CMakeLists.txt", 
            "md5sum": "af80de26762735799e289ab1feeec33d", 
            "pkg_name": "kf5-kpty", 
            "sha1sum": "2f765e6141ec886bac5472236f65c723826f6670", 
            "sha256sum": "28bc93bbcfc71b259ed5d10355b6fc947d15c6dd954a87002eaa6c1fc7b027a4", 
            "tar_file": "kpty-4.100.0.tar.xz", 
            "tar_sum": "4a31a53097eaf029df45dd36ab622a57"
        },
        {
            "filename": "/kpty-4.100.0/autotests/kptyprocesstest.cpp", 
            "md5sum": "ac5d96770e99f7101271c555da8d067c", 
            "pkg_name": "kf5-kpty", 
            "sha1sum": "d4d2ecfd58f8fe89488e5c6a72786ef0cdb18492", 
            "sha256sum": "ed505ab705f85274d128a1bcd1908c7829677d2bcbc3ff8358bb8f56c08d0303", 
            "tar_file": "kpty-4.100.0.tar.xz", 
            "tar_sum": "4a31a53097eaf029df45dd36ab622a57"
        }, 
        {
            "filename": "/kpty-4.100.0/autotests/kptyprocesstest.h", 
            "md5sum": "07cc3cc8365c5bad601ba3c06384d4fd", 
            "pkg_name": "kf5-kpty", 
            "sha1sum": "29dd10eb6d7c335555a1ffa3ffbd8d1610a5d1de", 
            "sha256sum": "e8be8630423f26a7714c413cf8aa663b8e798195c36cfbc097fc7da0d721adba", 
            "tar_file": "kpty-4.100.0.tar.xz", 
            "tar_sum": "4a31a53097eaf029df45dd36ab622a57"
        },
    ]


md5sum
""""""

.. code-block:: javascript

    http://209.132.184.120/md5/<md5sum>

Sample Results
""""""""""""""

Querying data by md5sum::

    http://209.132.184.120/api/md5/bf6f8d7c7022b27534011c4ad8334e2a

.. code:: javascript

    [
        {
            "filename": "/kpty-4.100.0/po/hi/kpty5.po", 
            "md5sum": "bf6f8d7c7022b27534011c4ad8334e2a", 
            "pkg_name": "kf5-kpty", 
            "sha1sum": "8f8d90a0ad5c3ad706b8874fb7e690096f697337", 
            "sha256sum": "e94e37d0bf22eea94d1a118da712f96608b8be150ac616c0a03e9cd3d58594dd", 
            "tar_file": "kpty-4.100.0.tar.xz", 
            "tar_sum": "4a31a53097eaf029df45dd36ab622a57"
        }
    ]

Package Details
---------------

It will display the details of the package. It will return versions of the package present::

    http://209.132.184.120/api/package/<package>

Sample Results
""""""""""""""

.. code-block:: javascript

    http://209.132.184.120/api/package/fotoxx

.. code-block:: javascript

    [
    "fotoxx-14.05.tar.gz", 
    "fotoxx-14.04.2.tar.gz", 
    "fotoxx-14.05.1.tar.gz", 
    "fotoxx-14.04.tar.gz"
    ]


Files of a package
------------------

It determines the files bundled within a package. It returns
file names for the files contained within a package::

    http://209.132.184.120/api/package/<package>/filenames

Sample Results
""""""""""""""

.. code-block:: javascript

    http://209.132.184.120/api/package/felix-gogo-command/filenames

.. code-block:: javascript

    [
        "/org.apache.felix.gogo.command-0.14.0/src/main/java/org/apache/felix/gogo/command/OBR.java", 
        "/org.apache.felix.gogo.command-0.14.0/pom.xml", 
        "/org.apache.felix.gogo.command-0.14.0/NOTICE", 
        "/org.apache.felix.gogo.command-0.14.0/DEPENDENCIES", 
        "/org.apache.felix.gogo.command-0.14.0/LICENSE", 
        "/org.apache.felix.gogo.command-0.14.0/doc/changelog.txt", 
        "/org.apache.felix.gogo.command-0.14.0/src/main/java/org/apache/felix/gogo/command/Activator.java", 
        "/org.apache.felix.gogo.command-0.14.0/src/main/java/org/apache/felix/gogo/command/Inspect42.java", 
        "/org.apache.felix.gogo.command-0.14.0/src/main/java/org/apache/felix/gogo/command/Inspect.java", 
        "/org.apache.felix.gogo.command-0.14.0/src/main/java/org/apache/felix/gogo/command/Base64Encoder.java", 
        "/org.apache.felix.gogo.command-0.14.0/src/main/java/org/apache/felix/gogo/command/Basic.java", 
        "/org.apache.felix.gogo.command-0.14.0/src/main/java/org/apache/felix/gogo/command/Files.java", 
        "/org.apache.felix.gogo.command-0.14.0/src/main/java/org/apache/felix/gogo/command/Util.java"
    ]


Compare two or more packages
----------------------------

Common files
""""""""""""

It compares two or more packages given by user and compare their sha256sum
and returns the common files present in all the packages::

    http://209.132.184.120/api/compare/packages/common \
        packages=={package1} \
        packages=={package2}

Sample Results
""""""""""""""

.. code-block:: javascript

    http://209.132.184.120/api/compare/packages/common \
        packages==epiphany \
        packages==libappstream-glib

.. code-block:: javascript

    [
        [
            {
                "filename": "/epiphany-3.12.1/po/Makefile.in.in",
                "md5sum": "c1882e57d8e6f87823863424e87926e0",
                "pkg_name": "epiphany",
                "sha1sum": "a225ba8bb2118afc96523149d854868e29277cc2",
                "sha256sum": "4b81add6870a96c75ad55b0a7f1d92bd42bdad184a9246e51f5d46219f149c0c",
                "tar_file": "epiphany-3.12.1.tar.xz",
                "tar_sum": "48d1ae142c41c55d62183456d4527d3d"
            }
        ],
        [
            {
                "filename": "/appstream-glib-0.2.1/po/Makefile.in.in",
                "md5sum": "c1882e57d8e6f87823863424e87926e0",
                "pkg_name": "libappstream-glib",
                "sha1sum": "a225ba8bb2118afc96523149d854868e29277cc2",
                "sha256sum": "4b81add6870a96c75ad55b0a7f1d92bd42bdad184a9246e51f5d46219f149c0c",
                "tar_file": "appstream-glib-0.2.1.tar.xz",
                "tar_sum": "e1bd0a1cdd7b2495a8a3b3bab8f193b2"
            }, 
            {
                "filename": "/appstream-glib-0.2.0/po/Makefile.in.in",
                "md5sum": "c1882e57d8e6f87823863424e87926e0",
                "pkg_name": "libappstream-glib",
                "sha1sum": "a225ba8bb2118afc96523149d854868e29277cc2",
                "sha256sum": "4b81add6870a96c75ad55b0a7f1d92bd42bdad184a9246e51f5d46219f149c0c",
                "tar_file": "appstream-glib-0.2.0.tar.xz",
                "tar_sum": "12256fed43fb8de30ddfebec9ff29140"
            }
        ]
    ]


Uncommon files
""""""""""""""

It compares two or more packages given by user and compare their sha256sum
and returns the uncommon files present in all the packages::

    http://209.132.184.120/api/compare/packages/uncommon \
        packages=={package1} \
        packages=={package2}

It will return a list of list where each list is a list of dictionary containing
uncommon file details package wise. Details contain the values of the file's sha1sum,
sha256sum, md5sum, package name which is same for a list and tar file to which it belongs
to and its tar sum.

Results will be similar to the one shown above in case of uncommon files.
