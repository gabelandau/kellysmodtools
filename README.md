# Kelly's Mod Tools
Kelly's Mod Tools are a set of Reddit moderation bots and a frontend administration dashboard to configure the system.

Currently, the bots are able to perform the following major functions:
* Monitor the moderation log, looking for special post flairs which are used to remove posts, usernote, ban, etc.
* Monitor new posts on a subreddit, and act if a user is posting over a defined threshold. Actions can include post removal, usernoting, banning, etc. 

## Technical Details
The bot scripts are written in Python using Praw and controlled by Supervisor, interfacing with the admin dashboard via the Supervisor XML-RPC API. The backend of the admin dashboard is written in Python with the Flask framework, and the frontend is Javascript with the Vue framework.

Authentication happens here in two ways. The system itself depends on a master bot account to function, which is defined in the `.env` configuration file. This bot account must be invited as a moderator to subreddits that want to utilize the system. The admin dashboard allows other Reddit accounts to be authenticated for using as the "action" accounts. That way, removals/messages/etc. can come from a custom account.

## Development
In order to develop in this system, you'll need the following pre-requisites setup. If anything here is unclear, you might not be quite ready to work on this system.
* A python 3 virtual environment.
  * Install python dependencies by running `pip install -r requirements.txt` from the project root directory.
* Node 13 with NPM.
  * Install node dependencies for the frontend of the webapp by running `npm install` from the `webapp/frontend` directory.