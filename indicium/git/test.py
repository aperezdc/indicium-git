#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Igalia S.L.
#
# Distributed under terms of the GPLv3 or, at your option,
# under the terms of the Apache 2.0 license.

from ..test.test_base import TestStoreMethodsMixin, TestStoreOperationsMixin
from ..test.test_fs import TestFSStoreMixin
from indicium.base import BytesSerializer, Serializer
from indicium.git import GitStore
import unittest, tempfile, shutil


class TestGitStoreAutocommit(unittest.TestCase,
        TestStoreMethodsMixin,
        TestStoreOperationsMixin,
        TestFSStoreMixin):

    autocommit = True

    def setUp(self):
        self.tmpdir_path = tempfile.mkdtemp(prefix="indicium-gitstore")
        self.s = BytesSerializer(GitStore(self.tmpdir_path,
            extension=".foo", autocommit=self.autocommit))

    def tearDown(self):
        super(TestGitStoreAutocommit, self).tearDown()
        shutil.rmtree(self.tmpdir_path, ignore_errors=True)


class TestGitStore(TestGitStoreAutocommit):
    autocommit = False

    def tearDown(self):
        self.s.child.commit("Commit message")
        super(TestGitStore, self).tearDown()

class TestExistingStoreDir(unittest.TestCase):
    def setUp(self):
        self.tmpdir_path = tempfile.mkdtemp(prefix="indicium-gitstore")

    def tearDown(self):
        shutil.rmtree(self.tmpdir_path, ignore_errors=True)

    def test_reopen(self):
        GitStore(self.tmpdir_path).put("/answer", b"42")
        self.assertEqual(b"42", GitStore(self.tmpdir_path).get("/answer"))
