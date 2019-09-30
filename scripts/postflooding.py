import os
import praw
import sys

from dotenv import load_dotenv
from loguru import logger

reddit = None
subreddit = None
bot = None
slack = None

def run():
  for submission in reddit.redditor('gallowboob').submissions.new(limit=50):
    print(submission.title)


def main():
  if not initialize():
    sys.exit()

  run()
  

def initialize():
  global reddit
  global subreddit
  global slack

  load_dotenv()

  logger.add(sys.stdout, format="[{time:HH:mm:ss.SSS}] {message}")

  CLIENT_ID = os.getenv("CLIENT_ID")
  CLIENT_SECRET = os.getenv("CLIENT_SECRET")
  CLIENT_USERNAME = os.getenv("CLIENT_USERNAME")
  CLIENT_PASSWORD = os.getenv("CLIENT_PASSWORD")
  USER_AGENT = os.getenv("USER_AGENT")

  try:
    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, username=CLIENT_USERNAME, password=CLIENT_PASSWORD, user_agent=USER_AGENT)
  except Exception as e:
    logger.error("Error creating Reddit instance.")
    return False

  return True


if __name__ == "__main__":
  main()
