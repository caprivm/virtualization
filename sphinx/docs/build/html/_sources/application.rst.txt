Application Package
###################

.. contents::
   :local:
   :depth: 2

The application package contains the main application code. It's the entry point to the application. It contains the **code documentation** and the **functional documentation** of each `submodule` that belongs to the project.

Functional Documentation
************************

In this part, the user will see the **functional documentation** of the application package. This documentation must to be added to the :code:`__init__.py` file of the package (in this case, the :code:`__init__.py` file that is under the :code:`application` folder), and it must to be written in `reStructuredText` format. 

.. automodule:: application
   :members:
   :undoc-members:
   :show-inheritance:

Submodules
**********

The application package contains the following submodules.

.. toctree::
   :maxdepth: 4

   application.module1
   application.utils
