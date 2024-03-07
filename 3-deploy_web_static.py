#!/usr/bin/python3
"""distro archive to webserver"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['54.160.77.90', '10.25.190.21']


def do_pack():
    """do pack"""
    try:
        tare = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        nof = "versions/web_static_{}.tgz".format(tare)
        local("tar -cvzf {} web_static".format(nof))
        return nof
    except ImportError:
        return None


def do_deploy(archive_path):
    """distro archive to webserver"""
    if exists(archive_path) is False:
        return False
    try:
        the_file_split = archive_path.split("/")[-1]
        file_split_temp = the_file_split.split(".")[0]
        the_way = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(the_way, file_split_temp))
        run('tar -xzf /tmp/{} -C {}{}/'.format(
            the_file_split, the_way, file_split_temp))
        run('rm /tmp/{}'.format(the_file_split))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(the_way, file_split_temp))
        run('rm -rf {}{}/web_static'.format(the_way, file_split_temp))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(
            the_way, file_split_temp))
        return True
    except ImportError:
        return False


def deploy():
    """deploy"""
    do_pack_obj = do_pack()
    if do_pack_obj is None:
        return False
    return do_deploy(do_pack_obj)
