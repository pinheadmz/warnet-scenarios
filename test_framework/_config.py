# Warnet configuration

import os
os.environ['BITCOIND'] = '/usr/local/bin/bitcoind'

class OPTIONS:
    nocleanup = True
    noshutdown = False
    cachedir = ""
    tmpdir = ""
    loglevel = "DEBUG"
    trace_rpc = None
    port_seed = 10000
    coveragedir = None
    descriptors = True
    timeout_factor = 1
    pdbonfailure = False
    usecli = False
    perf = False
    valgrind = False
    randomseed = 1

CONFIG = {
    "environment": {
        "BUILDDIR": "",
        "EXEEXT": "",
        "PACKAGE_BUGREPORT": ""
    }
}
