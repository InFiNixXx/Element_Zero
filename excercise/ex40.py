#!/usr/bin/python

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy Birthday To You",
                  "I don't Want To Get Sued",
                  "So, I'll Stop Right There"])


bulls_on_parade = Song(["They Rally Around The Family",
                        "With Pockets Full of Shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
