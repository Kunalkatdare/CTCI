class Jukebox(object):
    def __init__(self, songs):
        self.songs = {}
        for song in songs:
            self.songs[song.title] = song
        self.playing = None

    def play_song(self, title):
        if self.playing:
            self.stop_song()
        self.playing = self.songs[title]
        self.playing.play()

    def stop_song(self):
        if self.playing:
            self.playing.stop()


class Song(object):
    def __init__(self, title, data):
        self.title, self.data = title, data
        self.play_count = 0

    def play(self):
        self.is_playing = True
        self.play_count += 1

    def stop(self):
        self.is_playing = False

    import unittest

    class Test(unittest.TestCase):
        def test_jukebox(self):
            song1 = Song("Just Dance", "312312312")
            song2 = Song("Cold", "21321312")
            jukebox = Jukebox([song1, song2])
            jukebox.play_song("Paradise")

        if __name__ == "__main__":
            unittest.main()
