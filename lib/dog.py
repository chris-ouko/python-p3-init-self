#!/usr/bin/env python3

class Dog:
    pass
    def __init__(self, name, breed=None):
        self.name = name
        self.breed = breed if breed else "Mutt"