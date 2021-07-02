httpie-snapdsocket
==================

Snapd socket transport plugin for `HTTPie <https://httpie.io>`_.


Installation
------------

.. code-block:: bash

    $ python -m pip install --upgrade httpie-snapdsocket


Example usage
-------------

To query ``open-syobon-action`` package details:

.. code-block:: bash

    $ http snapd:///v2/find?name=open-syobon-action

Have a look at the `Snapd REST API documentation <https://snapcraft.io/docs/snapd-api>`_ for more information.


Requirements
------------

- `requests-unixsocket <https://github.com/msabramo/requests-unixsocket/>`_