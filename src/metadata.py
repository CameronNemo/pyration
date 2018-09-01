import re
import mutagen

class PyrationMetaData(object):
    orig = ""
    container = ""
    artist = ""
    title = ""
    other = ""

    def __init__(self, orig):
        # save the given value
        self.orig = orig
        by_dots = orig.split('.')
        # break the media container out
        self.container = by_dots.pop(-1)
        by_dash = '.'.join(by_dots).split('-')
        # TODO: handle dashes in artist or title
        self.artist = by_dash[0].strip()
        self.title = by_dash[1].strip()
        self.other = by_dash[2:]

    def to_path(self):
        return "{}/{}.{}".format(self.artist, self.title, self.container)

    def write_metadata(self, path):
        m = mutagen.File(path, easy=True)
        m["artist"] = self.artist
        m["title"] = self.title
        m.save()
