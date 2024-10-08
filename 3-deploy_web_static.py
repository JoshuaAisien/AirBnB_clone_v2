from fabric.api import env,put, local, sudo
from datetime import datetime
import os

""" 
This file does the full deployment 
"""
env.hosts = ['54.167.94.80','100.25.10.251' ]
env.key_filename = '~/.ssh/id_rsa'
def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns the archive path if successful, otherwise None.
    """
    # Create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Generate the archive name based on the current date and time
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    # Create the archive using the tar command
    command = "tar -czvf {} web_static".format(archive_path)
    result = local(command, capture=True)

    # Check if the archive was successfully created
    if result.succeeded:
        return archive_path
    else:
        return None


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
        sudo(f'mkdir -p /data/web_static/releases/{archive_name}')

        # uncompress and extract the archive to the target directory just created above
        sudo(f"tar -xvf /tmp/{basename} -C /data/web_static/releases/{archive_name}")

        # delete the archive from the server
        sudo(f'rm -rf /tmp/{basename}')

        # delete the symbolic link
        sudo(f'ln -sfn /data/web_static/releases/{archive_name} /data/web_static/current')

        return True
    except Exception as e:
        print(f'deployment failed: {e}')
        return False

def deploy():
    """
    creates and distributes an archive to the web servers
    :return: True
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)