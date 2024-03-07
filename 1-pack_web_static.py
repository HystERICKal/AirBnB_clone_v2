#!/usr/bin/python3
"""generating a .tgz archive"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """generating a .tgz archive"""

    on_the_clock = datetime.now()
    temp = 'web_static_' + on_the_clock.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    devp = local('tar -cvzf versions/{} web_static'.format(temp))
    if devp is not None:
        return temp
    else:
        return None
