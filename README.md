
# MediumBot

# Instalation
```sh
$ pip3 install mediumbot/
```

# Configuration File
Configuration File Example mediumbot.yaml

```yaml

username: 'hackermotto'
email: 'root@hackermotto.com'
password: 'p@ssw0rd'
phone: '+20112233444'
login_service: 'Twitter'
cookies: ''
driver: 'Firefox'
headless: true

post_black_list:
  - 'Sex'
  - 'Drugs'
  - 'Child Labor'

clap_for_posts: true
randomize_clapping_for_posts: false
max_claps_for_post: 45
min_claps_for_post: 20

comment_on_posts: true
randomize_commenting_on_posts: false
comments: 
  - 'Great Post.'
  - 'Great Read!'
  - 'Good work keep it up!'
  - 'Really enjoyed the content!'
  - 'Very interesting!'

follow_users: true
randomize_following_users: false

unfollow_users: false
randomize_unfollowing_users: false
unfollow_users_black_list: 
  - 'DontUnfollowMe'

use_related_topics: true
posts_per_topic: 50
verbose: true

max_sleep: 50
min_sleep: 30

logging_level: "INFO"
logging_datefmt: "%m/%d/%Y %H:%M:%S"
logging_format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging_file: "mediumbot.log"

```

# Running
```sh
mediumbot -c mediumbot.yaml
```

# Running On the Background
```sh
tmux
mediumbot -c mediumbot.yaml
```

Press `CTRL+b` then `d`

```sh
tmux list-sessions
tmux attach-sessions -t 0

```

# Running on Linux with Gui

## Installing GUI on VPS

```sh
sudo apt-get install lubuntu-desktop
sudo apt-get install tightvncserver
vncserver
```

After installing you can connect to your server by pointing your VNC client to your external IP at port 5901 (Ex. 196.168.0.1:5901).

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
2. https://www.section.io/engineering-education/install-a-gui-on-an-ubuntu-server-1804/