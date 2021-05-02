
import bs4
import time
import random
import logging
import pprint
import atexit

from selenium import webdriver
from pyvirtualdisplay import Display

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from mediumbot.basicConfig import basicConfig
from mediumbot.loggerConfig import loggerConfig

class Bot(basicConfig, loggerConfig):

    username = "hackermotto"
    email = "root@hackermotto.com"
    password = None
    phone = None
    login_service = "Twitter"
    cookies = []
    driver = "Firefox"
    headless = True

    post_black_list = ["Sex", "Drugs", "Child Labor"]

    clap_for_posts = True
    randomize_clapping_for_posts = False
    max_claps_for_post = 50
    min_claps_for_post = 10

    comment_on_posts = True
    randomize_commenting_on_posts = False
    comments = [
        "Great read!",
        "Good work keep it up!",
        "Really enjoyed the content!",
        "Very interesting!",
    ]

    follow_users = True
    randomize_following_users = False

    unfollow_users = False
    randomize_unfollowing_users = False
    unfollow_users_black_list = ["DontUnfollowMe"]

    use_related_topics = True
    posts_per_topic = 50
    verbose = True

    max_sleep = 15
    min_sleep = 10

    logging_level = "INFO"
    logging_datefmt = "%m/%d/%Y %H:%M:%S"
    logging_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging_file = "mediumbot.log"

    def __init__(self, *args, **kwargs):
        # atexit.register(self.TearDown)
        pass

    def Lunch(self):
        logger = self.startLogger()
        logger.info("Lunching ...")
        self.StartBrowser(logger)
        self.startVirtualDisplay(logger)

    def startVirtualDisplay(self, logger):
        display = Display(visible=0, size=(800,600))
        display.start()

    def StartBrowser(self, logger):
        logger.info("Starting Browser ...")

        DriverType = self.driver.lower()

        if DriverType == "chrome":
            options = ChromeOptions()
            if self.headless:
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-gpu")
            browser = webdriver.Chrome(options=options)

        elif DriverType == "firefox":
            options = FirefoxOptions()
            if self.headless:
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-gpu")
            browser = webdriver.Firefox(options=options)

        if self.SignInToService(browser, logger):
            self.MediumBot(browser, logger)

        self.TearDown(browser, logger)

    def TearDown(self, browser, logger):
        browser.quit()

    def MediumBot(self, browser, logger):
        logger.info("Starting MediumBot ...")

        if self.comment_on_posts or self.clap_for_posts or self.follow_users:

            postsUrls = []
            topicsUrls = []

            topicsUrls = self.ScrapeTopicsUrls(browser, logger)

            random.shuffle(topicsUrls)

            for topicUrl in topicsUrls:
                postsUrls = self.ScrapePostsUrlsOffTopicsPage(browser, logger, topicUrl)

            random.shuffle(postsUrls)

            for postUrl in postsUrls:
                self.ClapCommentAndFollowOnPost(browser, logger, postUrl)

        if self.unfollow_users:
            while True:
                self.UnFollow(browser, logger)

    def SignInToService(self, browser, logger):
        logger.info("Signing in to service ...")

        SignInWith = self.login_service.lower()
        SignedIn = False

        if self.cookies is not None:
            SignedIn = self.SignInWithCookies(browser, logger)

        if not SignedIn:

            browser.get("https://medium.com/m/signin?redirect=https%3A%2F%2Fmedium.com%2F")
            self.sleep(logger)

            if SignInWith == "google":
                SignedIn = self.SignInToGoogle(browser, logger)

            elif SignInWith == "twitter":
                SignedIn = self.SignInToTwitter(browser, logger)

            elif SignInWith == "facebook":
                SignedIn = self.SignInToFacebook(browser, logger)

            if SignedIn:
                logger.info("Sign In Cookies: {}".format(browser.get_cookies()))

        return SignedIn

    def SignInWithCookies(self, browser, logger):

        SignedIn = False

        try:
            browser.get("https://medium.com")
            self.sleep(logger)

            if len(self.cookies) > 0:
                logger.info("Setting Cookies ..")
                for cookie in self.cookies:
                    browser.add_cookie(cookie)

            browser.get("https://medium.com/me/")
            self.sleep(logger)

            if browser.title != "Medium":
                SignedIn = True
                logger.info("Signed In with Cookies.")

            else:
                logger.info("Can't Sign In with Cookies.")

        except:
            logger.error("Signed In with Cookies Failed.")

        return SignedIn

    def SignInToTwitter(self, browser, logger):
        logger.info("Signing in to Twitter ...")

        SignedIn = False

        try:
            browser.find_element_by_id("susi-modal-twitter-button").click()
            self.sleep(logger)

            browser.find_element_by_id("username_or_email").send_keys(self.username)
            browser.find_element_by_id("password").send_keys(self.password)
            browser.find_element_by_id("allow").click()
            self.sleep(logger)

            SignedIn = True

        except:
            logger.error("Signing in to Twitter Failed.")

        return SignedIn

    def SignInToGoogle(self, browser, logger):
        logger.info("Signing in to Google ...")

        SignedIn = False

        try:
            browser.find_element_by_id("susi-modal-google-button").click()
            self.sleep(logger)

            browser.find_element_by_id("identifierId").send_keys(self.email)
            browser.find_element_by_id("identifierNext").click()
            self.sleep(logger)

            browser.find_element_by_name("password").send_keys(self.password)
            browser.find_element_by_id("passwordNext").click()
            self.sleep(logger)

            SignedIn = True

        except:
            logger.error("Signing in to Google Failed.")

        return SignedIn

    def SignInToFacebook(self, browser, logger):
        logger.info("Signing in to Facebook ...")

        SignedIn = False

        try:
            browser.find_element_by_id("susi-modal-facebook-button").click()
            self.sleep(logger)

            browser.find_element_by_id("email").send_keys(self.email)
            browser.find_element_by_id("pass").send_keys(self.password)
            browser.find_element_by_name("login").click()
            self.sleep(logger)

            SignedIn = True

        except:
            logger.error("Signing in to Facebook Failed.")

        return SignedIn

    def ScrapeTopicsUrls(self, browser, logger):
        logger.info("Scraping topics URLs ...")
        try:

            topicsUrls = []

            browser.get("https://medium.com/me/following/topics")
            self.sleep(logger)

            if self.use_related_topics:
                TopicsElementsXpath = "//*[contains(@class, 'u-flexCenter')]//button[contains(@class, 'is-active')]/parent::*//a"
            else:
                TopicsElementsXpath = (
                    "//*[contains(@class, 'u-flexCenter')]//button/parent::*//a"
                )

            for link in browser.find_elements_by_xpath(TopicsElementsXpath):
                topicsUrls.append(link.get_attribute("href"))

            # soup = bs4.BeautifulSoup(browser.page_source, "html.parser")

            # for div in soup.find_all('div', class_="u-flexColumn u-flex0 u-borderBox u-width280 u-height280 u-borderBlackLightest u-marginHorizontal15 u-marginBottom30 js-sectionItem"):
            # 	for a in div.find_all('a'):
            # 		if a["href"] not in topicsUrls:
            # 			topicsUrls.append(a["href"])

            logger.info(topicsUrls)
            return topicsUrls

        except:
            logger.error("Scraping topics URLs Failed.")

    def ScrapePostsUrlsOffTopicsPage(self, browser, logger, topicUrl):
        logger.info("Scraping posts URLs ...")
        try:

            postsUrls = []

            browser.get(topicUrl)
            self.sleep(logger)

            logger.info("Visiting '{}' ".format(browser.title))

            soup = bs4.BeautifulSoup(browser.page_source, "html.parser")

            while len(postsUrls) < self.posts_per_topic:

                self.ScrollToBottomAndWaitForLoad(browser, logger)
                self.sleep(logger)

                for a in soup.find_all("a"):
                    if a["href"] not in postsUrls:
                        postsUrls.append(a["href"])

            logger.info(postsUrls)
            return postsUrls

        except:
            logger.error("Scraping posts URLs Failed.")

    def ClapCommentAndFollowOnPost(self, browser, logger, postUrl):
        logger.info("Clap Comment and Follow the post ...")
        try:
            if postUrl.startswith("/"):
                postUrl = "https://medium.com{}".format(postUrl)

            browser.get(postUrl)
            self.sleep(logger)

            logger.info("Visiting '{}' ".format(browser.title))

            if browser.title not in self.post_black_list:

                if self.clap_for_posts:
                    if not self.randomize_clapping_for_posts:
                        self.ClapForPost(browser, logger)
                    elif random.choice([True, False]):
                        self.ClapForPost(browser, logger)

                if self.follow_users:
                    if not self.randomize_following_users:
                        self.Follow(browser, logger)
                    elif random.choice([True, False]):
                        self.Follow(browser, logger)

                if self.comment_on_posts:
                    if not self.randomize_commenting_on_posts:
                        self.CommentOnPost(browser, logger)
                    elif random.choice([True, False]):
                        self.CommentOnPost(browser, logger)

        except:
            logger.error("Clap Comment and Follow Failed.")

    def ClapForPost(self, browser, logger):
        logger.info("Clapping ...")
        try:
            self.ScrollToBottomAndWaitForLoad(browser, logger)
            self.sleep(logger)

            ClapButtonXpath = "(//*[@aria-label='clap']/parent::*)[1]"
            element = browser.find_element_by_xpath(ClapButtonXpath)

            claps = random.randint(self.min_claps_for_post, self.max_claps_for_post)
            for clap in range(claps):
                element.click()
                logger.info("Clapped.")

            self.sleep(logger)

        except:
            logger.error("Clapping Failed.")

    def CommentOnPost(self, browser, logger):
        logger.info("Commenting ...")
        try:
            alreadyCommented = False

            comment = random.choice(self.comments)
            self.ScrollToBottomAndWaitForLoad(browser, logger)
            self.sleep(logger)

            CommentButtonXpath = "(//*[@aria-label='responses']/parent::*)[1]"
            element = browser.find_element_by_xpath(CommentButtonXpath)
            element.click()
            self.sleep(logger)

            try:
                CommentedXparh = "//*[contains(text(),'Responses')]/parent::*/parent::*/parent::*//div[text()='YOU']"
                alreadyCommented = browser.find_element_by_xpath(
                    CommentedXparh
                ).is_displayed()
                self.sleep(logger)

            except:
                pass

            if not alreadyCommented:

                CommentTextXpath = "//span[text()='What are your thoughts?']/parent::*"
                element = browser.find_element_by_xpath(CommentTextXpath)
                element.click()
                self.sleep(logger)

                actions = ActionChains(browser)
                actions.send_keys(comment)
                actions.perform()
                self.sleep(logger)

                RespondButtonXpath = "//button[text()='Respond']"
                element = browser.find_element_by_xpath(RespondButtonXpath)
                element.click()
                self.sleep(logger)

                logger.info("Commented.")
            else:
                logger.info("Already Commented.")

        except:
            logger.error("Commenting Failed.")

    def Follow(self, browser, logger):
        logger.info("Following ...")
        try:
            FollowButtonXpath = "(//*[text()='Follow'])[1]"
            browser.find_element_by_xpath(FollowButtonXpath).click()
            logger.info("Followed.")
            self.sleep(logger)

        except:
            logger.error("Following Failed.")

    def UnFollow(self, browser, logger):
        logger.info("UnFollowing ...")
        try:

            browser.get("https://medium.com/me")
            self.sleep(logger)

            browser.get("{}/following".format(browser.current_url))
            self.sleep(logger)

            # Unfollow People
            PeopleXpath = "//h4[text()='People']"
            element = browser.find_element_by_xpath(PeopleXpath)
            element.click()

            PeopleList = "//ul//li"
            PeopleElements = browser.find_elements_by_xpath(PeopleList)

            while True:
                self.ScrollToBottomAndWaitForLoad(browser, logger)
                self.sleep(logger)

                for AuthorElement in PeopleElements:
                    PeopleUnFollowButton = "//button[text()='Following']"
                    element = AuthorElement.find_element_by_xpath(PeopleUnFollowButton)
                    element.click()

            # Unfollow Publications
            PublicationsXpath = "//h4[text()='Publications']"
            element = browser.find_element_by_xpath(PublicationsXpath)
            element.click()

            PublicationsList = "//ul//li"
            PublicationsElements = browser.find_elements(By.XPATH, PublicationsList)

            while True:
                self.ScrollToBottomAndWaitForLoad(browser, logger)
                self.sleep(logger)

                for PublicationElement in PublicationsElements:
                    self.sleep(logger)

                    try:
                        PublicationFollowButton = (
                            "//button/div[text()='Following']/parent::*"
                        )
                        # PublicationFollowButton = "//*[@aria-labelledby='collectionFollowPopover']"
                        element = PublicationElement.find_element(
                            By.XPATH, PublicationFollowButton
                        )
                        element.click()

                        # WebDriverWait(browser, 20).until(
                        # 	EC.element_to_be_clickable((By.XPATH, PublicationFollowButton))
                        # 	).click()

                    except:
                        logger.info("Error clicking Following button.")
                        pass

                    try:
                        PublicationUnFollowButton = (
                            "//button[text()='Unfollow publication']/parent::*"
                        )
                        element = PublicationElement.find_element(
                            By.XPATH, PublicationUnFollowButton
                        )
                        element.click()
                    except:
                        logger.info("Error clicking Unfollow publication button.")

            logger.info("UnFollowed.")
            self.sleep(logger)

        except:
            logger.error("UnFollowing Failed.")

    def ScrollToBottomAndWaitForLoad(self, browser, logger):
        logger.info("Scrolling ...")
        try:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        except:
            logger.error("Scrolling Failed.")

    def sleep(self, logger):
        logger.info("Sleeping ...")
        try:
            SleepingTime = random.randint(self.min_sleep, self.max_sleep)
            logger.info("Sleeping for {}".format(SleepingTime))
            time.sleep(SleepingTime)

        except:
            logger.error("Sleeping Failed.")
