====================
 Indicium Git Store
====================

.. image:: https://img.shields.io/travis/aperezdc/indicium-git.svg?style=flat
   :target: https://travis-ci.org/aperezdc/indicium-git
   :alt: Build Status

.. image:: https://img.shields.io/coveralls/aperezdc/indicium-git/master.svg?style=flat
   :target: https://coveralls.io/r/aperezdc/indicium-git?branch=master
   :alt: Code Coverage

A Git-based key-value store backend for `Indicium
<https://github.com/aperezdc/indicium>`_.


Usage
=====

.. code-block:: python

    # Instantiate and write some data.
    from indicium.git import GitStore
    store = GitStore("./data", autocommit=False)
    store.put("/the-answer", b"10")

    # Not needed with autocommit=True
    store.commit("Note down the answer to everything")

    # Create a new commit with the correct answer.
    store.put("/the-answer", b"42")
    store.commit("Fix the answer to everything")

The ``./data`` directory will contain a Git repository which can be inspected
with ``git``. Every call to ``.commit()`` adds a commit to it or, with the
auto-commit mode enabled, every call to ``.put()`` and ``.delete()`` will
implicitly add a commit.


Installation
============

All stable releases are uploaded to `PyPI <https://pypi.python.org>`_, so you
can install them and upgrade using ``pip``::

    pip install indicium-git

Alternatively, you can install the latest development code —at your own risk—
directly from the Git repository::

    pip install git://github.com/aperezdc/indicium-git


Development
===========

If you want to contribute, please use the usual GitHub workflow:

1. Clone the repository.
2. Hack on your clone.
3. Send a pull request for review.

If you do not have programming skills, you can still contribute by `reporting
issues <https://github.com/aperezdc/indicium-git/issues>`__ that you may
encounter. Contributions to the documentation are very welcome, too!
