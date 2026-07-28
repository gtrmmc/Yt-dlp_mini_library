from ..globals import extractors as _extractors_context
from ..globals import plugin_ies as _plugin_ies_context

# Target Platforms ke Extractors Import
from .generic import GenericIE

# YouTube
from .youtube import (
    YoutubeIE,
    YoutubePlaylistIE,
    YoutubeTabIE,
    YoutubeSearchIE,
    YoutubeSearchURLIE,
    YoutubeClipIE,
    YoutubeTruncatedIDIE,
    YoutubeTruncatedURLIE,
)

# Instagram
from .instagram import InstagramIE, InstagramUserIE, InstagramStoryIE

# Facebook
from .facebook import FacebookIE, FacebookPluginsVideoIE

# TikTok
from .tiktok import TikTokIE, TikTokUserIE, TikTokVMIE

# Twitter / X
from .twitter import TwitterIE

# Snapchat (Exactly matching your file)
from .snapchat import SnapchatSpotlightIE



# Selected Supported Extractors List
_MINI_EXTRACTORS = [
    # YouTube
    YoutubeIE,
    YoutubePlaylistIE,
    YoutubeTabIE,
    YoutubeSearchIE,
    YoutubeSearchURLIE,
    YoutubeClipIE,
    YoutubeTruncatedIDIE,
    YoutubeTruncatedURLIE,
    # Instagram
    InstagramIE,
    InstagramUserIE,
    InstagramStoryIE,
    # Facebook
    FacebookIE,
    FacebookPluginsVideoIE,
    # TikTok
    TikTokIE,
    TikTokUserIE,
    TikTokVMIE,
    # Twitter / X
    TwitterIE,
    # Snapchat
    SnapchatSpotlightIE,
    # Generic Fallback
    GenericIE,
]


def import_extractors():
    """ Dynamic extractors load bypass """
    pass


def gen_extractor_classes():
    """ Return supported extractors list """
    return _MINI_EXTRACTORS


def gen_extractors():
    """ Return instance of every supported extractor """
    return [klass() for klass in gen_extractor_classes()]


def list_extractor_classes(age_limit=None):
    """ Return sorted list of extractors """
    yield from sorted(filter(
        lambda ie: ie.is_suitable(age_limit) and ie != GenericIE,
        gen_extractor_classes()), key=lambda ie: ie.IE_NAME.lower())
    yield GenericIE


def list_extractors(age_limit=None):
    """ Return extractor names list """
    return [ie() for ie in list_extractor_classes(age_limit)]


def get_info_extractor(ie_name):
    """ Return info extractor class by name """
    for ie in gen_extractor_classes():
        if ie.__name__ == f'{ie_name}IE':
            return ie
    return None
