#
# Copyright (C) 2020, Toshinao Ishii <padoauk@gmail.com> All Rights Reserved.
#


import os
import sys
import re
import logging
import yaml
import inkex
import requests

TAG_PREFIX='_bs_'

KEY_ID =   f'{TAG_PREFIX}id'
ENV_CONFIG = 'AFD_CONFIG'
LOGFILE = '/tmp/afd.log'

class Afd(inkex.EffectExtension):

    def add_arguments(self, pars):
        pars.add_argument("--tab")

        return

    def config(self):
        self.doAssociate = False
        cpath = os.environ.get(ENV_CONFIG) # config file path
        self.url = 'http://localhost:2813' # "afd".to_i(16) == 2813
        if cpath != None:
            try:
                with open(cpath, 'r') as file:
                    yml = yaml.safe_load(file)
                    if "url" in yml:
                        self.url = yml["url"]
            except Exception as e:
                logging.error(f'Exception occurred while loading YAML {cpath} {e}')

        return

    # query consists all key-value of the node propreties plus svgnode={type of node}
    def make_query(self, node):
        q = dict()
        q['svgnode'] = f'{node}'
        for item in node.items():
            q[item[0]] = f'{item[1]}'

        return q

    def request(self, node):
        q = self.make_query(node)
        try:
            #res = requests.get(self.url, params=q)
            res = requests.post(self.url, params=q)
        except Exception as e:
            logging.error(f'{e}')
            return None

        return res

    def associate(self, node, res):
        if node == None or res == None:
            return None
        kv = dict()
        try:
            json = res.json()
            # set all attribute that matches f'^{TAG_PREFIX}' but nothing else
            for key in json:
                m = re.search(f'^{TAG_PREFIX}', key)
                if m:
                    node.set(key, json[key])
                    kv[key] = json[key]
            logging.info(f'updated: {kv}')
        except Exception as e:
            logging.error(f'{e}')

        return kv

    def effect(self):
        logging.debug(f'doAssociate: {self.doAssociate}')
        for node in self.svg.get_selected():
            res = self.request(node)
            if self.doAssociate:
                self.associate(node, res)

        return

    def modeAssociate(self):
        self.doAssociate = True

        return

if __name__ == '__main__':
    logging.basicConfig(filename=LOGFILE,
                        level=logging.INFO,
                        format='%(asctime)s [%(levelname)s(%(levelno)s)]\tcode: %(pathname)s(%(lineno)s), fn: %(funcName)s, %(message)s')
    afd = Afd()
    afd.config()
    for p in sys.argv:
        if p == '--tab=associate_tab':
            afd.modeAssociate()
    afd.run()

    sys.exit()
