#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Igalia S.L.
#
# Distributed under terms of the GPLv3 or, at your option,
# under the terms of the Apache 2.0 license.

from ..fs import FSStore
from ..key import normalize
from os import path as P
from dulwich.repo import Repo


class GitStore(FSStore):
    __slots__ = ("_autocommit", "_repo")

    author = "GitStore <git@indicium>"

    def __init__(self, path=".", extension=".data", autocommit=True):
        super(GitStore, self).__init__(path, extension)
        self._autocommit = autocommit
        gitdir = P.join(self._path, ".git")
        if P.isdir(gitdir):
            self._repo = Repo(self._path)
        else:
            self._repo = Repo.init(self._path)

    def commit(self, message, author=None):
        message += "\n\nCommitted by indicium.git.GitStore"
        if author is None:
            author = self.author
        author = author.encode()
        self._repo.do_commit(committer=author, author=author,
                message=message.encode())

    def put(self, key, value):
        super(GitStore, self).put(key, value)
        self._repo.stage([self.path_for_key(key)])
        if self._autocommit:
            self.commit("put: {!s}".format(normalize(key)))

    def delete(self, key):
        path = self.path_for_key(key)
        if not P.exists(P.join(self._path, path)):
            return
        super(GitStore, self).delete(key)
        self._repo.stage([path])
        if self._autocommit:
            self.commit("delete: {!s}".format(normalize(key)))
