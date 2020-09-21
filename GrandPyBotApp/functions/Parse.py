import string
import pickle


class Parser:
    """ This class parse message from front input from user and return it to API"""

    def __init__(self):
        """Initial attribute for Parser"""
        with open('GrandPyBotApp/functions/fr_stop_word_data', 'rb') as fr_stop_word_file:
            my_unpickler = pickle.Unpickler(fr_stop_word_file)
            self.fr_stop_word = my_unpickler.load()
        # List of piece of word, for target french verb.
        self.list_pattern_beginning = ['part', 'all', 'veu', 'part', 'voul', 'voudr', 'ir']
        self.list_pattern_end = ['ons', 'ez', 'ent', 'x', 't', 'ais', 'ai', 'ait', 'us', 'ut',
                                 'ûmes', 'ûtes', 'urent', 'é', 'ir']

    @staticmethod
    def format_message(message_from_front):
        """Format message from front user input"""
        # Parse input message
        message_from_front = message_from_front.lower()
        message_from_front = message_from_front.strip(string.punctuation)
        message_from_front = message_from_front.replace("\'", " ")
        message_from_front = message_from_front.replace(",", "")
        message_from_front = message_from_front.replace(".", "")
        message_from_front = message_from_front.strip()
        message_from_front = message_from_front.split(" ")
        return message_from_front

    def format_verb(self, message_from_front):
        """Format message from front user input by removing verb"""
        list_verb_pattern = []
        for pattern_beginning in self.list_pattern_beginning:
            for pattern_end in self.list_pattern_end:
                pattern = pattern_beginning + pattern_end
                list_verb_pattern.append(pattern)

        # Remove list_message_from_front from message_from_front
        list_message_from_front = [word for word in message_from_front if word not in list_verb_pattern]

        return list_message_from_front

    def parse_message_from_front(self, message_from_front):
        """
        Parse the message from front user input, return parse message for API by using method from Parser
        """
        # Use method from Parser class
        list_message_from_front = self.format_message(message_from_front)
        parse_message_of_front = self.format_verb(list_message_from_front)

        # Remove stopWord from parse_message_from_front
        word = [word for word in parse_message_of_front if word not in self.fr_stop_word]

        return word
