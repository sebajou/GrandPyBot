import string
import re
import pickle


class Parser:
    """ This class parse message from front input from user and return it to API"""

    def __init__(self):
        """Initial attribut for Paser"""
        with open('GrandPyBotApp/functions/fr_stop_word_data', 'rb') as fr_stop_word_file:
            my_unpickler = pickle.Unpickler(fr_stop_word_file)
            self.fr_stop_word = my_unpickler.load()
        # List of piece of word, for target french verb.
        self.list_pattern_beginning = ['veu', 'part', 'voul', 'voudr']
        self.list_pattern_end = ['ons', 'ez', 'ent', 'x', 't', 'ais', 'ait', 'us', 'ut', 'ûmes', 'ûtes', 'urent']

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
        list_message_from_front = []
        for word in message_from_front:
            for pattern_beginning in self.list_pattern_beginning:
                for pattern_end in self.list_pattern_end:
                    pattern = pattern_beginning + pattern_end
                    if not re.match(pattern, word):
                        list_message_from_front.append(word)
                        list_message_from_front = list(set(list_message_from_front))
        return list_message_from_front

    def parse_message_from_front(self, message_from_front):
        """
        Parse the message from front user input, return parse message for API by using method from Parser
        """
        # Use method from Parser class
        list_message_from_front = self.format_message(message_from_front)
        parse_message_from_front = self.format_verb(list_message_from_front)

        # Remove stopWord from parse_message_from_front
        word = [word for word in parse_message_from_front if not word in self.fr_stop_word]

        """if len(word) > 0:
            for element in word:
                word = str(word)
                word = word + ' ' + element

        print(word)"""

        return word
