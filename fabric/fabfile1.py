from fabric.api import local, settings, abort
from fabric.contrib.console import confirm

def test():
  with settings(warn_only=True):
    result = local('reboot', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
      abort("Aborting at user request.")
