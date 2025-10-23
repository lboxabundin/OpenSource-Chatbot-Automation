import json
import re
from typing import Tuple, Dict


class ChatEngine:
def __init__(self, rules_path: str):
with open(rules_path) as f:
self.rules = json.load(f)


def process(self, text: str) -> Tuple[str, str, Dict]:
text_lower = text.lower()
for rule in self.rules.get('rules', []):
for pattern in rule.get('patterns', []):
if re.search(pattern, text_lower):
resp = rule.get('response', '')
meta = rule.get('meta', {})
return rule.get('name'), resp, meta
return 'unknown', self.rules.get('default_response','Sorry.'), {}
