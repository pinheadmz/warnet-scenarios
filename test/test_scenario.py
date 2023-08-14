#!/usr/bin/env python3

import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')
from test_framework.test_framework import BitcoinTestFramework


class TestScenario(BitcoinTestFramework):
    def set_test_params(self):
        self.setup_clean_chain = True
        self.num_nodes = 1

    def run_test(self):
        print(self.nodes[0].getblockcount())
        print(self.generate(self.nodes[0], 100))
        print(self.nodes[0].createwallet('test0'))
        print(self.nodes[0].getbalances())



if __name__ == '__main__':
    TestScenario().main()
