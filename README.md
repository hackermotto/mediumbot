
# MediumBot

# Instalation
```sh
$ pip3 install mediumbot/
```

# Configuration File
> mediumbot.yaml
```yaml
USERNAME: 'hackermotto'
EMAIL: 'mediumbot@hackermotto.com'
PASSWORD: 'p@ssw0rd'
PHONE: '+201122333444'
LOGIN_SERVICE: 'Twitter'
COOKIES: ''
DRIVER: 'Firefox'
HEADLESS: True

POST_BLACK_LIST:
  - 'Sex'
  - 'Drugs'
  - 'Child Labor'

CLAP_FOR_POSTS: True
RANDOMIZE_CLAPPING_FOR_POSTS: False
MAX_CLAPS_FOR_POST: 50
MIN_CLAPS_FOR_POST: 50

COMMENT_ON_POSTS: True
RANDOMIZE_COMMENTING_ON_POSTS: False
COMMENTS: 
  - 'Great post.'
  - 'Great read!'
  - 'Good work keep it up!'
  - 'Really enjoyed the content!'
  - 'Very interesting!'

FOLLOW_USERS: True
RANDOMIZE_FOLLOWING_USERS: False

UNFOLLOW_USERS: False
RANDOMIZE_UNFOLLOWING_USERS: False
UNFOLLOW_USERS_BLACK_LIST: 
  - 'DontUnFollowMe'

USE_RELATED_TOPICS: True
POSTS_PER_TOPIC: 50
VERBOSE: True

MAX_SLEEP: 15
MIN_SLEEP: 10
```

# Running
```sh
mediumbot -c mediumbot.yaml
```

# Information

says the daily follow limit for Medium is 125.

# Webdrivers
1. https://github.com/mozilla/geckodriver/releases
2. https://sites.google.com/a/chromium.org/chromedriver/downloads
3. https://api.bitbucket.org/2.0/repositories/ariya/phantomjs/
4. https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
5. https://webkit.org/blog/6900/webdriver-support-in-safari-10/

# References
1. https://selenium-python.readthedocs.io/installation.html