Requesting data by hashes
-------------------------

It returns the files with the specified hash sum. The files retrieved contain the values of filename, package name,
md5sum, sha1sum, sha256sum, tar_sum, tar_file matching that particular hash sum.

sha1sum
"""""""
The **/api/sha1/<sha1sum>** endpoint will return files matching this sha1sum.

**Sample Results:**

Querying files data by sha1sum::

    /api/sha1/e0ec2c54e7a4fabb2f7e8c78d711efc0ed5f4f43

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

The **/api/sha256/<sha256sum>** endpoint will return files matching the sha256sum.

**Sample Results:**

Querying files data by sha256sum::

    /api/sha256/e77b543aefd1595f159e541041a403c48a240913bc65ca5c4267df096f775eb6

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

tar_sum
"""""""

The **/api/tar_sum/<tar_sum>** endpoint will return files matching the tar_sum.

**Sample Results:**


Querying files data by tarsum::

    /api/tar_sum/4a31a53097eaf029df45dd36ab622a57

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

The **/api/md5/<md5sum>** endpoint will return files matching the md5sum.

**Sample Results:**

Querying data by md5sum::

    /api/md5/bf6f8d7c7022b27534011c4ad8334e2a

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

The **/api/package/<package>** endpoint will display the details of the package. It will return
all the available versions of the package.

**Sample Results:**

.. code-block:: javascript

    /api/package/fotoxx

.. code-block:: javascript

    [
    "fotoxx-14.05.tar.gz", 
    "fotoxx-14.04.2.tar.gz", 
    "fotoxx-14.05.1.tar.gz", 
    "fotoxx-14.04.tar.gz"
    ]


Files of a package
------------------

The **/api/package/<package>/filenames** endpoint determines the files bundled within a package.
It returns file names for the files contained within a package.

**Sample Results:**

.. code-block:: javascript

    /api/package/felix-gogo-command/filenames

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


Files of a package version
--------------------------

The **/api/tar_file/<tar_file>/filenames** endpoint determines the files bundled within a particular
package version. To get the filenames of a specific package version, you will have to query by tar_file.
It returns file names for the files contained within a tar_file.

**Sample Results:**

.. code-block:: javascript

    /api/tar_file/fedora-release-22.tar.bz2/filenames

.. code-block:: javascript

    [
        "/fedora-release-22/fedora-release.spec", 
        "/fedora-release-22/Makefile", 
        "/fedora-release-22/LICENSE", 
        "/fedora-release-22/Fedora-Legal-README.txt", 
        "/fedora-release-22/fedora-release.spec", 
        "/fedora-release-22/Makefile", 
        "/fedora-release-22/LICENSE", 
        "/fedora-release-22/Fedora-Legal-README.txt", 
        "/fedora-release-22/80-server.preset", 
        "/fedora-release-22/fedora-release.spec", 
        "/fedora-release-22/Makefile", 
        "/fedora-release-22/LICENSE", 
        "/fedora-release-22/Fedora-Legal-README.txt"
    ]


Compare two or more packages
----------------------------

Common files
""""""""""""

It compares two or more packages by comparing sha256sum values of the filenames
present in all the packages and returns the common files present in them along with their sha256sum values::

    /api/compare/package/common \
        package=={package1} \
        package=={package2}

**Sample Results:**

.. code-block:: javascript

    /api/compare/package/common \
        package==ark \
        package==baloo

Each dictionary lists the common files corresponding to a package with sha256sum as keys and filename as values.

.. code-block:: javascript

    [
        {
            "fb7be8c7f3e0669a87e63fbcf825b257efe5f67f9a70ac5a7b252a6c84e58b4d": "/ark-4.13.3/app/icons/CMakeLists.txt"
        },
        {
            "fb7be8c7f3e0669a87e63fbcf825b257efe5f67f9a70ac5a7b252a6c84e58b4d": "/baloo-4.13.3/icons/CMakeLists.txt"
        }
    ]


Different files
"""""""""""""""

It compares two or more packages by comparing sha256sum values of the filenames
present in all the packages and returns different files present in them::

    /api/compare/package/difference \
        package=={package1} \
        package=={package2}

It returns a list of dictionaries where each dictionary contains the filenames and their
sha256sum value which are not common to all the packages. Number of dictionaries will be equal
to the total number of packages.


**Sample Results:**

.. code-block:: javascript

    /api/compare/package/difference \
        package==kamera \
        package==fedora-release

.. code-block:: javascript

    [
    {
        "00b89abcd9cf529345404f8a67d41e703cae441ae2d7854b20beaf089baae36e": "/kamera-4.13.3/ConfigureChecks.cmake", 
        "0436e83123eea5ac095a77f64d10519a6074b078c1d15ab781aa348e4ba4ed35": "/kamera-4.13.3/kioslave/camera.protocol", 
        "07f41b28b17911be8490525f412697da62a3e7b2e189ca29dadb263e20f29256": "/kamera-4.13.3/kcontrol/kameradevice.cpp", 
        "18421505064b4a2cd773e9a2bf98c64db34c83bcabf6ec7387ec95c458ce9173": "/kamera-4.13.3/README", 
        "18974988f11f677c4baa5c752752847fb9b87b1fc6d36c5beb3a9c3a79ac6a18": "/kamera-4.13.3/solid_camera.desktop", 
        "24135307a386caee34a88eab36169f0fd43b0ad5da6090f5ffb53d0964d3c1fa": "/kamera-4.13.3/config-kamera.h.cmake", 
        "4bd2e0b0c578306d16b8060c2e043531362292bdf9b2a41aca5624b4e4d35be2": "/kamera-4.13.3/doc/index.docbook", 
        "56976e64523fa1e68db4e6f464f5b2cb89d7d08f54b1d012e317b8db286b3faf": "/kamera-4.13.3/COPYING.DOC", 
        "6dbb2b780afb1a31a1286d175a2c0d8c7d15ed04b60a37f03c7e586bec41f3bc": "/kamera-4.13.3/kcontrol/kamera.cpp", 
        "74d81bbf3efede0c7e0b105322c5a1ec53fa2ed46b0e3649b53a1d8ede4ecc2b": "/kamera-4.13.3/AUTHORS", 
        "7a0f87979094421ff2b32c231b35d76e02f64d944ded2753e409efbda2dd8884": "/kamera-4.13.3/kioslave/kamera.h", 
        "86dc01e58023906382d67889d421b499afd3e1fe998fdebb139b804dc85fa71b": "/kamera-4.13.3/kcontrol/CMakeLists.txt", 
        "8a749a77786068db7eb1392f4785ca281599a1f9b5605573e545031572700d9e": "/kamera-4.13.3/CMakeLists.txt", 
        "976dddb7a9a7dd8c88588278f156799cf0b4adf6cf53314728ae6b50f6cb8c39": "/kamera-4.13.3/kcontrol/kamera.h", 
        "a03643d17e1f766f6ddf8922053507c6f4e96e4f1a78f6b124435ffaf1f34aa4": "/kamera-4.13.3/kcontrol/kameradevice.h", 
        "a10fcef4334a09ec9f45b518d7ea2b23cb76ad38d081a26a473e50fd00dc0e11": "/kamera-4.13.3/kcontrol/kameraconfigdialog.h", 
        "a4fa6ed9786722eadb722d8fa7c2a26caf0f8fcaf46ea09b6b99b52b69dadb05": "/kamera-4.13.3/doc/CMakeLists.txt", 
        "ab15fd526bd8dd18a9e77ebc139656bf4d33e97fc7238cd11bf60e2b9b8666c6": "/kamera-4.13.3/COPYING", 
        "b7062b4fb6531c8bcdf49582edbec32b7e5fa0c67e58d5547369a25330e4a817": "/kamera-4.13.3/kioslave/kamera.cpp", 
        "b7c2e27003fa276cea1c9d1218f2cd2881c906f2c002be0ad07b4c540b36d1a5": "/kamera-4.13.3/kcontrol/kameraconfigdialog.cpp", 
        "e37329f9d650ad37393223a2c49c727a22014219ba1a64beebd8aa67ae504e57": "/kamera-4.13.3/kcontrol/Messages.sh", 
        "e5663efdce52de170537e86f65a46bf338f8dde63d412b6c88ff7a68bfaf6974": "/kamera-4.13.3/kcontrol/kamera.desktop", 
        "fb92a8a46407311a9c6bca0a8376c589733551821f93fc59ae679b2528d2501d": "/kamera-4.13.3/kioslave/CMakeLists.txt"
    }, 
    {
        "08a3f0726b7562259d5913f52f5dae29edc31986f03b90fa1cb5d4b464f09c70": "/fedora-release-21/fedora-release.spec", 
        "41144e81097272725f6866e7a25d443e7e3881e5ebfa7d3c206589db07726e63": "/fedora-release-21/fedora-release.spec", 
        "427c375983767f2afd5bdbf103e64c004245cad62987e6b5daf084be0f5b2869": "/fedora-release-21/fedora-release.spec", 
        "47e0837b90b20cb593037ec60d631ad3eae5c4b04cf710f02d883dc8ce923288": "/fedora-release-21/fedora-release.spec", 
        "57a1002eb36716ae9aaa9dfbb3ad331c6fce9a7685541af80bf85cbd6ecb2bb8": "/fedora-release-22/Fedora-Legal-README.txt", 
        "5bcfc800b563957a4332042a2b32a3ba3db16fab08b5dfca425ca48b78140191": "/fedora-release-22/fedora-release.spec", 
        "9e0458e08253a702d9fc12ffa0ef841c0acb5ef73a9cc2015d35f38c4d7d55e6": "/fedora-release-22/fedora-release.spec", 
        "a5a42fa9aca797bfefeb0120336d787e754bc1f3ae088d474a4a057152eb1bda": "/fedora-release-22/Makefile", 
        "af5ef1c4c9b745b8b5ee61c0b2d45b0348f7caa3d6a010e272bfbcc2ffd43752": "/fedora-release-21/80-server.preset", 
        "c7e0766a598fc83ef9c7512c1641e51ce238745f0448d3cf90781a1d77a09d6f": "/fedora-release-22/80-server.preset", 
        "c91a4cd38e5e7bb5923951a6cb9bab407381d5ab6b0f1e9013795c04725f7fe7": "/fedora-release-22/fedora-release.spec", 
        "e98708047560db5a5bcf7495c3108709760cbf6202df7b216cbd7918725e7d0f": "/fedora-release-22/LICENSE"
    }
    ]


Compare two or more tar_files
-----------------------------

Common files
""""""""""""

It compares two or more tar_files by comparing the sha256sum of the filenames
present in all the tar_files and returns common files present in them along with their sha256sum::

    /api/compare/tar_file/common \
        tar_file=={tar_file} \
        tar_file=={tar_file}

**Sample Results:**

.. code-block:: javascript

    /api/compare/tar_file/common \
        tar_file==fedora-release-21.tar.bz2 \
        tar_file==fedora-release-22.tar.bz2

.. code-block:: javascript

    [
        {
            "57a1002eb36716ae9aaa9dfbb3ad331c6fce9a7685541af80bf85cbd6ecb2bb8": "/fedora-release-21/Fedora-Legal-README.txt",
            "a5a42fa9aca797bfefeb0120336d787e754bc1f3ae088d474a4a057152eb1bda": "/fedora-release-21/Makefile",
            "e98708047560db5a5bcf7495c3108709760cbf6202df7b216cbd7918725e7d0f": "/fedora-release-21/LICENSE"
        },
        {
            "57a1002eb36716ae9aaa9dfbb3ad331c6fce9a7685541af80bf85cbd6ecb2bb8": "/fedora-release-22/Fedora-Legal-README.txt",
            "a5a42fa9aca797bfefeb0120336d787e754bc1f3ae088d474a4a057152eb1bda": "/fedora-release-22/Makefile",
            "e98708047560db5a5bcf7495c3108709760cbf6202df7b216cbd7918725e7d0f": "/fedora-release-22/LICENSE"
        }
    ]


Different files
```````````````

It compares two or more tar_files by comparing sha256sum values of the filenames
present in all the packages and returns different files present in them::

    /api/compare/package/difference \
        package=={package1} \
        package=={package2}

It returns a list of dictionaries where each dictionary contains the filenames and their
sha256sum value which are not common to all the packages. Number of dictionaries will be equal
to the total number of packages.


**Sample Results**

.. code-block:: javascript

    /api/compare/tar_file/difference \
        tar_file==fedora-release-21.tar.bz2 \
        tar_file==fedora-release-22.tar.bz2

.. code-block:: javascript

    [
        {
            "08a3f0726b7562259d5913f52f5dae29edc31986f03b90fa1cb5d4b464f09c70": "/fedora-release-21/fedora-release.spec", 
            "41144e81097272725f6866e7a25d443e7e3881e5ebfa7d3c206589db07726e63": "/fedora-release-21/fedora-release.spec", 
            "427c375983767f2afd5bdbf103e64c004245cad62987e6b5daf084be0f5b2869": "/fedora-release-21/fedora-release.spec", 
            "47e0837b90b20cb593037ec60d631ad3eae5c4b04cf710f02d883dc8ce923288": "/fedora-release-21/fedora-release.spec", 
            "af5ef1c4c9b745b8b5ee61c0b2d45b0348f7caa3d6a010e272bfbcc2ffd43752": "/fedora-release-21/80-server.preset"
        },
        {
            "5bcfc800b563957a4332042a2b32a3ba3db16fab08b5dfca425ca48b78140191": "/fedora-release-22/fedora-release.spec", 
            "9e0458e08253a702d9fc12ffa0ef841c0acb5ef73a9cc2015d35f38c4d7d55e6": "/fedora-release-22/fedora-release.spec", 
            "c7e0766a598fc83ef9c7512c1641e51ce238745f0448d3cf90781a1d77a09d6f": "/fedora-release-22/80-server.preset", 
            "c91a4cd38e5e7bb5923951a6cb9bab407381d5ab6b0f1e9013795c04725f7fe7": "/fedora-release-22/fedora-release.spec"
        }
    ]

