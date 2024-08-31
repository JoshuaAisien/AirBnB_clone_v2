from fabric.api import local
from datetime import datetime
import os


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
    archive_name = "versions/web_static_{}.tgz".format(timestamp)

    # Create the archive using the tar command
    command = "tar -czvf {} web_static".format(archive_name)
    result = local(command, capture=True)

    # Check if the archive was successfully created
    if result.succeeded:
        return archive_name
    else:
        return None
