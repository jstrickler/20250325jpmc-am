.. {{cookiecutter.app_name}} documentation master file

..  You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to {{cookiecutter.app_name}}'s documentation!
{{'-' * (cookiecutter.app_name | length + 28)}}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. can be moved to a separate file
.. automodule:: {{cookiecutter.app_slug}}.{{cookiecutter.app_module}}
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
