Snapd socket transport plugin for `HTTPie <https://httpie.io>`_
===============================================================

`Snap <https://snapcraft.io/>`_ is an app store for Linux.
Snapd is the custom URL protocol used to talk to that store using their `REST API <https://snapcraft.io/docs/snapd-api>`_.


Installation
------------

.. code-block:: bash

    $ python -m pip install --upgrade httpie-snapdsocket


Example usage
-------------

To query ``httpie`` Snap package details:

.. code-block:: bash

    $ http 'snapd:///v2/find?name=httpie'

Have a look at the `Snapd REST API documentation <https://snapcraft.io/docs/snapd-api>`_ for more information.


Requirements
------------

- `requests-unixsocket <https://github.com/msabramo/requests-unixsocket/>`_

Credits
-------

Based on the original code from @chipaca (`chipaca/httpie-snap <https://github.com/chipaca/httpie-snap>`_).
