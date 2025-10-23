import httpx
import logging
log = logging.getLogger(__name__)
def send_test_webhook(spec, context=None):
url = spec.get('url')
method = spec.get('method','POST').upper()
payload = {'context': context}
try:
r = httpx.request(method, url, json=payload, timeout=5.0)
return {'status_code': r.status_code, 'text': r.text}
except Exception as e:
log.exception('Webhook failed')
return {'error': str(e)}
