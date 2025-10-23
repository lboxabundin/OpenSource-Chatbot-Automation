import importlib
import logging
from example_tasks import send_test_webhook


log = logging.getLogger(__name__)


class AutomationRunner:
def __init__(self):
pass


def run(self, automation_spec, context=None):
"""Simple runner that supports built-in task types."""
t = automation_spec.get('type')
if t == 'http_call':
# execute an HTTP call (non-blocking recommended)
return send_test_webhook(automation_spec, context)
elif t == 'shell':
# run a shell command
return self._run_shell(automation_spec, context)
else:
log.warning('Unknown automation type: %s', t)
return None


def _run_shell(self, automation_spec, context):
import subprocess
cmd = automation_spec.get('cmd')
if not cmd:
return None
proc = subprocess.Popen(cmd, shell=True)
return proc.pid
