import GrandPyBotApp.functions.RandomMessage as Script
import pytest


class TestRandom:

    @staticmethod
    def test_random_message():

        assert str(Script.TheRandomMessage.random_message())
