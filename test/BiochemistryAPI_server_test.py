# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import requests

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from BiochemistryAPI.BiochemistryAPIImpl import BiochemistryAPI
from BiochemistryAPI.BiochemistryAPIServer import MethodContext
from BiochemistryAPI.authclient import KBaseAuth as _KBaseAuth


import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import requests

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from BiochemistryAPI.BiochemistryAPIImpl import BiochemistryAPI
from BiochemistryAPI.BiochemistryAPIServer import MethodContext
from BiochemistryAPI.authclient import KBaseAuth as _KBaseAuth


class BiochemistryAPITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('BiochemistryAPI'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'BiochemistryAPI',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = BiochemistryAPI(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_BiochemistryAPI_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    def test_get_compounds(self):
        cpds = self.getImpl().get_compounds(self.ctx, {"compounds":
                                            ["48/1/1/compounds/id/cpd00011",
                                             'cpd00002', "cpd00007"]})[0]
        assert len(cpds) == 3
        assert cpds[0]['id'] == 'cpd00011'
        assert cpds[1]['id'] == 'cpd00002'
        print(cpds[0]['aliases'])
        assert cpds[0]['aliases'] == ['"BiGG1:co2"', '"BiGG1:dco2"', '"KEGG:C00011"', '"MetaCyc:CARBON-DIOXIDE"', '"PlantCyc:CARBON-DIOXIDE"', '"BiGG:co2"']
        missing_col = {'name', 'formula', 'charge', 'deltaG', 'deltaGErr',
                       'abbrev', 'aliases'} - set(cpds[0].keys())
        if missing_col:
            raise AssertionError("Missing Columns:", missing_col)

    def test_get_reactions(self):
        rxns = self.getImpl().get_reactions(self.ctx, {"reactions":
                                            ["48/1/1/reactions/id/rxn00011",
                                             'rxn00002', "rxn00007"]})[0]
        assert len(rxns) == 3
        assert rxns[0]['id'] == 'rxn00011'
        assert rxns[1]['id'] == 'rxn00002'
        print(rxns[0]['aliases'])
        assert rxns[0]['aliases'] == ['"KEGG:R00014"', '"KEGGaly:R00014"', '"KEGGath:R00014"', '"KEGGbdi:R00014"', '"KEGGcre:R00014"', '"KEGGeco:R00014"', '"KEGGgmx:R00014"', '"KEGGosa:R00014"', '"KEGGpop:R00014"', '"KEGGsbi:R00014"', '"KEGGvvi:R00014"', '"KEGGzma:R00014"', '"MetaCyc:RXN-12583.c"', '"PlantCyc:RXN-12583.c"']
class BiochemistryAPITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('BiochemistryAPI'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'BiochemistryAPI',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = BiochemistryAPI(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_BiochemistryAPI_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    def test_get_compounds(self):
        cpds = self.getImpl().get_compounds(self.ctx, {"compounds":
                                            ["48/1/1/compounds/id/cpd00011",
                                             'cpd00002', "cpd00007"]})[0]
        assert len(cpds) == 3
        assert cpds[0]['id'] == 'cpd00011'
        assert cpds[1]['id'] == 'cpd00002'
        assert cpds[0]['aliases'] == ['BiGG1:co2', 'BiGG1:dco2',
                                      'KEGG:C00011', 'MetaCyc:CARBON-DIOXIDE',
                                      'PlantCyc:CARBON-DIOXIDE', 'BiGG:co2']
        missing_col = {'name', 'formula', 'charge', 'deltaG', 'deltaGErr',
                       'abbrev', 'aliases'} - set(cpds[0].keys())
        if missing_col:
            raise AssertionError("Missing Columns:", missing_col)

    def test_get_reactions(self):
        rxns = self.getImpl().get_reactions(self.ctx, {"reactions":
                                            ["48/1/1/reactions/id/rxn00011",
                                             'rxn00002', "rxn00007"]})[0]
        assert len(rxns) == 3
        assert rxns[0]['id'] == 'rxn00011'
        assert rxns[1]['id'] == 'rxn00002'
        assert rxns[0]['aliases'] == ['KEGG:R00014', 'MetaCyc:RXN-12583.c',
                                      'PlantCyc:RXN-12583.c']
        assert rxns[0]['enzymes'] == ['1.2.4.1', '2.2.1.6', '4.1.1.1']
        missing_col = {'name', 'direction'} - set(rxns[0].keys())
        if missing_col:
            raise AssertionError("Missing Columns:", missing_col)

    def test_depict_compounds(self):
        svgs = self.getImpl().depict_compounds(
            self.ctx, {'structures': ['C(=O)O', 'CCC']})[0]
        assert len(svgs) == 2
        assert '<svg' in svgs[0]
