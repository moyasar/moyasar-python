===============
Moyasar-Python
===============

Moyasar Python language wrapper

--------------
Documentation
--------------




See the `Python API docs. <https://moyasar.com/docs/api/?python>`_

-------------
Requirements
-------------

* Python +3.x

--------------
Installation
--------------

.. code-block:: bash

    pip install moyasar


-------
Usage
-------


.. code-block:: python

    import moyasar
    moyasar.api_key = '<moyasar key>'
    fetch_invoice = moyasar.Invoice.fetch('<invoice id>')
    fetch_invoice.cancel()

-------------
Contributing
-------------

Bug reports and pull requests are welcome on GitHub at https://github.com/[USERNAME]/moyasar. This project is intended to be a safe, welcoming space for collaboration.


--------
License
--------


The library is available as open source under the terms of the `MIT License. <https://opensource.org/licenses/MIT>`_