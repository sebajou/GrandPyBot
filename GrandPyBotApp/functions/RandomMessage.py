import random


class TheRandomMessage:
    """Engine to randomly send sentence from GranPapy with Python back end."""
    def random_message():

        # List of predeterminate messages.
        message = ["A oui ! Je connais bien cet endroit. ",
                   "Je suis allé à cet endroit quand j’avais presque ton âge. ",
                   "C’est un très beau lieu. J’aimais y aller quand j’étais jeune. ",
                   "J’y suis déjà allé. C’était en 1963. Évidemment, depuis ça a changé ! ",
                   "Tu te souviens, mon petit ? ",
                   "Je t’y ai emmené quand tu n’étais pas plus haut que ça. "]

        # Length of the list and random index for the list.
        length = len(message)
        random_index = random.randrange(0, length - 1)

        # Return the message randomly.
        return message[random_index]
