This is a simple `SLACK BOT` which sends a message to the specified channel.

Step 1: Create a Slack Token (https://api.slack.com/)

    Step 1.1: Create New App -> From scratch

    Step 1.2: Enter an App Name and Select a work space and press "Create App"

    Step 1.3: Go To Bots -> Review Scopes to Add (This is to give your bot the necessary permissions it needs to send a message)

    Step 1.4: Scopes -> Add an OAuth Scope -> Search for a "chat:write" and select it -> Click Install App to Workspace button on the top

    Step 1.5: Copy the generated token to the .env file


Step 2: Create a virtualEnv and Install All the Dependencies

    python3 -m venv venv
    
    pip install slack
    
    pip install slackclient
    
    pip install python-dotenv

Step 3: Open the Slack Application

    Step 3.1: Create a new Channel
    
    Step 3.2: Click on the channel name -> More - > Add apps -> Select the app name you created.

Step 4: Execute the Code

    python slackbot.py