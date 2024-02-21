#!/usr/bin/python3
''' Testing tempp'''

import os
import sys
import models
import unittest
import pep8
from io import StringIO
from tempp import HBNBCommand
from unittest.mock import create_autospec


class test_console(unittest.TestCase):
    ''' Testing tempp'''

    def test_pep8_console(self):
        """testing pep8"""
        desgn = pep8.StyleGuide(quiet=False)
        makos = 0
        hld = (["tempp.py"])
        makos = makos + desgn.check_files(hld).total_errors
        self.assertEqual(makos, 0, 'Need to fix Pep8')

    def setUp(self):
        '''testing setup'''
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        '''testing teardown'''
        sys.stdout = self.backup

    def create(self):
        ''' testing create'''
        return HBNBCommand()

    def test_quit(self):
        ''' testing quit'''
        tempp = self.create()
        self.assertTrue(tempp.onecmd("quit"))

    def test_EOF(self):
        ''' testing EOF'''
        tempp = self.create()
        self.assertTrue(tempp.onecmd("EOF"))

    def test_all(self):
        ''' testing all'''
        tempp = self.create()
        tempp.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "won't work in db")
    def test_show(self):
        '''testing show'''
        tempp = self.create()
        tempp.onecmd("create User")
        kitamblsho = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        tempp.onecmd("show User " + kitamblsho)
        cer = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(isinstance(cer, str))

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "won't work in db")
    def test_show_class_name(self):
        '''testing class name'''
        tempp = self.create()
        tempp.onecmd("create User")
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        tempp.onecmd("show")
        cer = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** class name missing **\n", cer)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "won't work in db")
    def test_show_class_name(self):
        '''Test id'''
        tempp = self.create()
        tempp.onecmd("create User")
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        tempp.onecmd("show User")
        cer = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** instance id missing **\n", cer)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "won't work in db")
    def test_show_no_instance_found(self):
        '''Test n inst'''
        tempp = self.create()
        tempp.onecmd("create User")
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        tempp.onecmd("show User " + "124356876")
        cer = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", cer)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "won't work in db")
    def test_create_fileStorage(self):
        '''testing create'''
        tempp = self.create()
        tempp.onecmd("create User")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_class_name(self):
        '''testing classname'''
        tempp = self.create()
        tempp.onecmd("create")
        cer = (self.capt_out.getvalue())
        self.assertEqual("** class name missing **\n", cer)

    def test_class_name_doest_exist(self):
        '''testing classname'''
        tempp = self.create()
        tempp.onecmd("create Binita")
        cer = (self.capt_out.getvalue())
        self.assertEqual("** class doesn't exist **\n", cer)
