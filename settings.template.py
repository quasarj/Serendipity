REDDIT_LOGIN = ''
REDDIT_PASSWORD = ''

SUBREDDIT_NAME = ''

# Only pull random links from a subreddit who has at least this many
# subscribers. Too low and the subreddits may not be of real value yet. Too
# high and they aren't niche enough.
MINIMUM_SUBSCRIBER_COUNT = 1000

# When Serendipity pulls a link, it will take a random one from the top N
# stories so that it's not just the absolute-top link getting exposure.
HOT_STORY_COUNT = 5

VERSION = '1.2a'
UA = 'Serendipity %s' % VERSION

BLACKLISTED_SUBREDDITS = frozenset([
    # Defaults
    'funny',
    'pics',
    'announcements',
    'blog',
    'askreddit',
    'worldnews',
    'gaming',
    'todayilearned',
    'politics',
    'science',
    'iama',
    'wtf',
    'videos',
    'technology',
    'music',
    'atheism',
    'adviceanimals',
    'aww',
    'movies',
    'bestof',
    'explainlikeimfive',

    # Mod Requests
    'abrathatfits',
    'transtimelines',
    'firstimpression',
    'gonenatural',
    'subredditdrama',
])
