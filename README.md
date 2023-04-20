## Twitter Complaint Bot for Slow Internet Speed
This is a Python-based Twitter complaint bot that checks the internet speed and tweets from your Twitter account to your internet provider about the low speed you are getting. The bot uses Selenium for web automation and requires the user to provide the path of the ChromeDriver and their Twitter credentials along with the name of their internet provider.

### How to Use the Bot
Clone the repository and navigate to the project directory.

Provide the path of the ChromeDriver and Twitter credentials in the config.ini file.
You can also specify the name of your internet provider in this file.


The bot will first check the internet speed  and then log in to your Twitter account using the provided credentials.

After logging in, the bot will compose a tweet about the slow internet speed and mention your internet provider's Twitter handle.

The tweet will be sent to your internet provider's Twitter handle, and you will receive a confirmation message on the console.


### Notes
This project uses the Chrome web driver for Selenium. You need to provide the path of the ChromeDriver executable 
For security purposes, it is recommended that you create a separate Twitter account for this bot and use its credentials in the config.ini file.
This bot is intended for educational purposes only. Use it at your own risk
