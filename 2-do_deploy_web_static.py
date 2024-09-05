#!/usr/bin/python3
from fabric.api import env, put, sudo
import os

"""
2-do_deploy_web_static file
"""

# Define your servers
env.hosts = ['54.167.94.80', '100.25.10.251']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """
    Distribute an archive to web servers remotely.
    :param archive_path: path to the archive file.
    return True if all operations are successful, otherwise return False.
    """
    if not os.path.exists(archive_path):
        return False

    # Get the basename from the archive_path
    basename = os.path.basename(archive_path)
    archive_name = basename.split('.')[0]

    try:
        # Upload the archive into /tmp/ directory on the webserver
        put(archive_path, '/tmp/')

        # Create the target directory on the remote server using sudo
        sudo('mkdir -p /data/web_static/releases/{}'.format(archive_name))

        # Uncompress and extract the archive to the target directory using sudo
        sudo('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(basename, archive_name))

        #Remove the /tmp/ file
        sudo(f'rm -rf /tmp/{basename}')

        # delete the symbolic link
        sudo(f'rm -rf /data/web_static/current' )

        # recreate the symbolic pointing to the uncompressed file
        sudo(f'ln -sf /data/web_static/releases/{archive_name}  /data/web_static/current')

        return True

    except Exception as e:
        print(f'deployment failed: {e}')
        return False
