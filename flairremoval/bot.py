import os
import praw
import sys
import json

from dotenv import load_dotenv
from loguru import logger

reddit = None
subreddit = None
bot = None
slack = None

class Reddit:
  reddit = None
  stream = None

  @staticmethod
  def init_reddit(id, secret, username, password, agent):
    try:
      Reddit.reddit = praw.Reddit(client_id=id, client_secret=secret, username=username, password=password, user_agent=agent)
      return True
    except Exception as e:
      logger.error(e)
      return False

  @staticmethod
  def monitor_mod_log():
    try:
      logger.info("Starting mod log monitor...")
      sub_string = "+".join(Settings.active_subs)
      Reddit.stream = praw.models.util.stream_generator(Reddit.reddit.subreddit(sub_string).mod.log, skip_existing=True, attribute_name="id")
      for action in Reddit.stream:
        print(vars(action))
        if action.action == "wikirevise" and "kmtsettings" in action.details:
          logger.info("Monitoring stopped by wiki page edit in %s" % (action.subreddit_name_prefixed))
          break
    except Exception as e:
      logger.error(e)

class Settings:
  flairs = dict()
  active_subs = []

  @staticmethod
  def read_config():
    logger.info("Reading wiki configuration pages...")
    sub_list = os.getenv("SUB_LIST").split(",")
    for sub in sub_list:
      try:
        wiki = Reddit.reddit.subreddit(sub).wiki['kmtsettings']
        json_contents = json.loads(wiki.content_md)
        Settings.flairs[sub] = json_contents
        Settings.active_subs.append(sub)
        logger.info("Sucessfully loaded wiki configuration page for /r/%s" % (sub))
      except Exception as e:
        logger.error("Failed to load wiki configuration page for /r/%S" % (sub))
        logger.error(e)


def main():
  if not initialize():
    sys.exit()

  Settings.read_config()
  Reddit.monitor_mod_log()
  

def initialize():
  global reddit
  global subreddit
  global slack

  load_dotenv()

  logger.add(sys.stdout, format="[{time:HH:mm:ss.SSS}] {message}")

  logger.info("Initalizing Kelly's Mod Tools...")

  CLIENT_ID = os.getenv("CLIENT_ID")
  CLIENT_SECRET = os.getenv("CLIENT_SECRET")
  CLIENT_USERNAME = os.getenv("CLIENT_USERNAME")
  CLIENT_PASSWORD = os.getenv("CLIENT_PASSWORD")
  USER_AGENT = os.getenv("USER_AGENT")

  if not Reddit.init_reddit(CLIENT_ID, CLIENT_SECRET, CLIENT_USERNAME, CLIENT_PASSWORD, USER_AGENT):
    return False

  return True


if __name__ == "__main__":
  main()
