#!/usr/bin/python3

import os 
import optparse

from mediumbot.bot import Bot

def GetDefaultConfig():
	return os.path.join(os.path.expanduser("~"), ".local", "mediumbot", "mediumbot.yaml")

def main():

	parser = optparse.OptionParser()

	parser.add_option("-u", "--username", dest="username", help="Set Username")
	parser.add_option("-e", "--email", dest="email", help="Set EMail")
	parser.add_option("-p", "--password", dest="password", help="Set Password")
	parser.add_option("--phone", dest="phone", help="Set Phone Number")
	parser.add_option("-s", "--login_service", dest="login_service", help="Set Login Service")
	parser.add_option("--cookies", dest="cookies", help="Set Cookies")
	parser.add_option("-d", "--driver", dest="driver", help=" Set Webdrivers")
	parser.add_option("--headless", dest="headless", help="Set Headless")

	parser.add_option("--post-black-list", dest="post_black_list", help="Post Black List")
	
	parser.add_option("--clap-for-posts", dest="clap_for_posts", help="Clap For Posts")
	parser.add_option("--randomize-clapping-for-posts", dest="randomize_clapping_for_posts", help="Randomize Clapping For Posts")
	parser.add_option("--max-claps-for-post", dest="max_claps_for_post", help="Set Maximum Claps For Post")
	parser.add_option("--min-claps-for-post", dest="min_claps_for_post", help="Set Minimum Claps For Post")

	parser.add_option("--comment-on-posts", dest="comment_on_posts", help="Comment On Posts")
	parser.add_option("--randomize-commenting-on-posts", dest="randomize_commenting_on_posts", help="Randomize Commenting On Posts")
	parser.add_option("--comments", dest="comments", help="Set Comments")

	parser.add_option("--follow-users", dest="follow_users", help="Follow Users")
	parser.add_option("--randomize-following-users", dest="randomize_following_users", help="Randomize Following Users")
	
	parser.add_option("--unfollow-users", dest="unfollow_users", help="Unfollow Users")
	parser.add_option("--randomize-unfollowing-users", dest="randomize_unfollowing_users", help="Randomize Unfollowing Users")
	parser.add_option("--unfollow-users-black-list", dest="unfollow_users_black_list", help="Unfollow Users Black List")

	parser.add_option("--use-related-topics", dest="use_related_topics", help="Use Related Topics")
	parser.add_option("--posts-per-topic", dest="posts_per_topic", help="")
	parser.add_option("--verbose", dest="verbose", help="Verbose")

	parser.add_option("--max-sleep", dest="max_sleep", help="Max Sleep")
	parser.add_option("--min-sleep", dest="min_sleep", help="Min Sleep")

	parser.add_option("--timeout", dest="timeout", help="Timeout")

	parser.add_option("--logging-level", dest="logging_level", help="Set Logging Level")
	parser.add_option("--logging-datefmt", dest="logging_datefmt", help="Set Logging Date Format")
	parser.add_option("--logging-format", dest="logging_format", help="Set Logging Format")
	parser.add_option("--logging-file", dest="logging_file", help="Set Logging File")

	parser.add_option("-c", "--config", dest="config", default=GetDefaultConfig(), help="Pass the configuration file path.")

	(options, args) = parser.parse_args()


	bot = Bot()
	bot.kwargsConfig(options)
	if options.config:
		bot.fileConfig(options.config)
	bot.start()

if __name__ == "__main__":
	main()
