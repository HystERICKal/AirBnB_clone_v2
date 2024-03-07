#!/usr/bin/python3
"""distro archive to webserver"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.89.109.87', '100.25.190.21']


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
