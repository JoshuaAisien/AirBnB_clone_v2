#!/usr/bin/python3
from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
    """
    Fabric script that generates a .tgz archive from the contents of the web_static folder.
    Returns the archive path if successful, otherwise None.
    """
    # Create the versions directory if it doesn't exist
    if not os.path.exists('versions'):
        os.makedirs('versions')

    # Generate the archive name with a timestamp
    date_format = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = f'versions/web_static_{date_format}.tgz'
    command = f'tar -cvzf {archive_path} web_static'

    # Execute the command
    result = c.local(command, hide=True)

    # Return the path if successful, otherwise None
    if result.ok:
        return archive_path
    else:
        return None
