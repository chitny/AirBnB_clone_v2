#!/usr/bin/python3
<<<<<<< HEAD
"""1. Compress before sending"""

from fabric.operations import local
=======
'''Fabric script that generates a .tgz archive'''

from fabric.api import run, local
>>>>>>> cd4c93e33e47d8d47247bb74daae22eff0d3b36b
from datetime import datetime


def do_pack():
<<<<<<< HEAD
    """Function to compress files"""
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if result.failed:
        return None
    return result
=======
    '''for the tgz'''
    try:
        local('mkdir -p versions')
        d_t = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_" + d_t + ".tgz"
        local("tar -cvzf" + filename + " web_static")
        return filename
    except:
        return None
>>>>>>> cd4c93e33e47d8d47247bb74daae22eff0d3b36b
