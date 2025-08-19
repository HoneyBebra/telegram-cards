# ruff: noqa: F401

# The message is processed in this queue
# If the message block is not initialized here, it will not work

from .messages.cards import init_cards
from .messages.registration import init_registration
