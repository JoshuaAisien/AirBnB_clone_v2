#!/usr/bin/python3
from fabric.api import run, put, env
import os
"""
2-d-_deploy_web_static file
"""

# define your servers
env.hosts = ['54.167.94.80','100.25.10.251' ]
env.user = 'ubuntu'
env.key_filename = '~/ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distribute an archive to web servers remotely.
    :param archive_path: path to the archive file.
    :return True is all operations are successful otherwise return false.
    """
    if not os.path.exists(archive_path):
        return False

    # get the basename from the archive_path
    basename = os.path.basename(archive_path)
    archive_name = basename.split('.')[0]
    try:
        # upload the archive into /tmp/ directory on the webserver
        put(archive_path, '/tmp/')

        # create the target directory on the remote server
        run(f'mkdir -p /data/web_static/releases/{archive_name}')

        # uncompress and extract the archive to the target directory just created above
        run(f"tar -xvf /tmp/{basename} -C /data/web_static/releases/{archive_name}")

        # delete the archive from the server
        run(f'rm -rf /tmp/{basename}')

        # delete the symbolic link
        run(f'ln -sfn /data/web_static/releases/{archive_name}  /data/web_static/current')

        return True
    except Exception as e:
        print(f'deployment failed: {e}')
        return False