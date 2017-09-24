from aiotg import Bot, Chat

from mailtrackingbot.config import config

bot = Bot(api_token=config.get('telegram', 'api_token'))


@bot.command(r"/echo (.+)")
def echo(chat: Chat, match):
    return chat.reply(match.group(1))


if __name__ == '__main__':
    bot.run()
