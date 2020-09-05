# OutOfContextScreenshotBot
Discord bot for screenshots of outofcontext.party lobbies.

This Discord bot was written using [discord.py](https://discordpy.readthedocs.io/en/latest/).
Setup your own Discord application as shown in https://realpython.com/how-to-make-a-discord-bot-python/
and save your own token in a `.env` file.

Once you add the bot to your Discord server use 
```
pipenv install
pipenv shell
python bot.py
```
in the repo directory to run the bot and
```
ooc_screenshot <lobby> [channel]
```
in some text channel of your Discord server to get a screenshot of the specified lobby in the specified text channel.
Providing the text channel is optional, if you omit it the screenshot will be posted in the same channel the command was sent to.

For example, write
```
ooc_screenshot 2a5t
```
to get a screenshot of the lobby https://www.outofcontext.party/lobby/2a5t in the current channel.
