from ..globals import extractors as _extractors_context
from ..globals import plugin_ies as _plugin_ies_context

# Sirf YouTube extractors ko import kar rahe hain (GenericIE completely removed)
from .youtube import (
    YoutubeIE,
    YoutubePlaylistIE,
    YoutubeTabIE,
    YoutubeSearchIE,
    YoutubeSearchURLIE,
    YoutubeSearchDateIE,
    YoutubeShortsTabIE,
    YoutubeClipIE,
    YoutubeTruncatedIDIE,
    YoutubeTruncatedURLIE,
)

# Yeh tumhari mini-library ka naya aur clean extractor list hai
_MINI_EXTRACTORS = [
    YoutubeIE,
    YoutubePlaylistIE,
    YoutubeTabIE,
    YoutubeSearchIE,
    YoutubeSearchURLIE,
    YoutubeSearchDateIE,
    YoutubeShortsTabIE,
    YoutubeClipIE,
    YoutubeTruncatedIDIE,
    YoutubeTruncatedURLIE,
]


def import_extractors():
    """ 
    Original code yahan 'extractors.py' load karta tha.
    Bypass kar diya gaya hai.
    """
    pass


def gen_extractor_classes():
    """ Return a list of supported extractors. """
    return _MINI_EXTRACTORS


def gen_extractors():
    """ Return a list of an instance of every supported extractor. """
    return [klass() for klass in gen_extractor_classes()]


def list_extractor_classes(age_limit=None):
    """Return a list of extractors that are suitable for the given age, sorted by extractor name"""
    # GenericIE ka logic yahan se bhi hata diya gaya hai
    yield from sorted(filter(
        lambda ie: ie.is_suitable(age_limit),
        gen_extractor_classes()), key=lambda ie: ie.IE_NAME.lower())


def list_extractors(age_limit=None):
    """Return a list of extractor instances that are suitable for the given age, sorted by extractor name"""
    return [ie() for ie in list_extractor_classes(age_limit)]


def get_info_extractor(ie_name):
    """Returns the info extractor class with the given ie_name"""
    for ie in gen_extractor_classes():
        if ie.__name__ == f'{ie_name}IE':
            return ie
    return None
    
