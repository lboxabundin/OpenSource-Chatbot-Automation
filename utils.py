# small helpers (logging, config loader) - left intentionally minimal for clarity
import logging

logger = logging.getLogger('os_chatbot')

def setup_logging():
logging.basicConfig(level=logging.INFO)
