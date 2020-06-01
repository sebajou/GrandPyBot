import GrandPyBotApp.functions.RandomMessage as Script
import pytest


class TestRandom:

    def test_random_message(self):

        assert str(Script.TheRandomMessage.random_message())
