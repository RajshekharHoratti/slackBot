import os
import slack
from datetime import datetime
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
dotenv_path = BASE_DIR + '/../../.env'
load_dotenv(dotenv_path)


def slack_bot(current_date):
    client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))
    # Normal Message Format
    client.chat_postMessage(channel=os.getenv("SLACK_CHANNEL"), text="This is a test message with any format..!!")

    # Block Message Format
    #NOTE: for other formats check out: https://api.slack.com/messaging/composing/layouts

    client.chat_postMessage(channel=os.getenv("SLACK_CHANNEL"), blocks=[
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Hi This is a test block message..!! \n>Current Date: {current_date}\n have a nice day :)"
            }
        }
    ])
    return True


current_date = datetime.today().strftime('%d-%m-%Y')
slack_bot(current_date)


