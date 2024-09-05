from fabric.api import run, env, local
import os

env.hosts = ['54.167.94.80', '100.25.10.251']
env.key_filename = '~/.ssh/id_rsa'

def do_clean(number=0):
    """
    Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.
    """
    number = int(number)

    if number <= 1:
        number = 1

    # Local cleanup (versions folder)
    archives = sorted(os.listdir("versions"))
    archives_to_delete = archives[:-number]

    print("Local archives to delete:", archives_to_delete)

    for archive in archives_to_delete:
        local("rm -rf versions/{}".format(archive))

    # Remote cleanup (/data/web_static/releases folder)
    for host in env.hosts:
        with run("ls -tr /data/web_static/releases") as result:
            archives = result.split()
            archives = [a for a in archives if "web_static_" in a]
            archives_to_delete = archives[:-number]

            print("Remote archives to delete:", archives_to_delete)

            for archive in archives_to_delete:
                run("rm -rf /data/web_static/releases/{}".format(archive))

