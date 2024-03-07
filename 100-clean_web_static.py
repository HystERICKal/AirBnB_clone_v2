#!/usr/bin/python3
"""deleting out of date archives"""

import os
from fabric.api import *

env.hosts = ['52.87.155.66', '54.89.109.87']


def do_clean(number=0):
    """deleting out of date archives"""

    if (int(number) == 0):
        number = 1
    else:
        int(number)

    the_sortd_vers = sorted(os.listdir("versions"))

    for i in range(number):
        the_sortd_vers.pop()

    with lcd("versions"):
        for a in the_sortd_vers:
            local("rm ./{}".format(a))

    with cd("/data/web_static/releases"):
        the_sortd_vers = run("ls -tr").split()
        the_sortd_vers = [a for a in the_sortd_vers if "web_static_" in a]

        for i in range(number):
            the_sortd_vers.pop()

        for a in the_sortd_vers:
            run("rm -rf ./{}".format(a))
