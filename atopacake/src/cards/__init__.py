# ruff: noqa: F401

# The message is processed in this queue
# If the message block is not initialized here, it will not work

from .tg_messages.cards import init_cards
from .tg_messages.registration import init_registration
