## A telegram bot that sends images from [rule34](https://rule34.xxx).

### Installation:

**1- Install [requirements.txt](requirements.txt).**

**2- Replace the value of "BotToken" on the first line of [main.py](main.py) with your bot token.**

### The bot works like this:
**If the command "/rule34" is typed, the bot will send a random image of the tag selected in the "Preference" variable in the second line of [main.py](main.py) (There is no preference by default so it will send a completely random image by default).**

**If the command "/rule34 somebody" is typed, the bot will send a random image of the tag "somebody" instead of the preferenced tag.**

### Usage examples:

> **User**: /rule34
>
> **Bot**: "Sends a picture of the preferenced tag"
>
> **User**: /rule34 makima
>
> **Bot**: "Sends a picture of Makima"
