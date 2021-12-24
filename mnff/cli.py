import argparse
import asyncio
import sys

from mi.ext import commands
import aiohttp
from mi.http import Route

class MNFF(commands.Bot):
    def __init__(self, args):
        super().__init__('tututuututututu!')
        self.args = args
    
    async def on_ready(self, ws):
        user = await self.get_user(self.args.user_id)
        async with aiohttp.ClientSession() as session:
            async with session.get(user.avatar_url) as resp:
                if resp.status == 404:
                    file = await self.show_file(url=user.avatar_url)
                    await self.remove_file(file.id)
                    await self.http.request(Route('POST', '/api/federation/update-remote-user'), json={'userId': user.id}, auth=True)
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--token')
    parser.add_argument('--url')
    parser.add_argument('--user_id')
    args = parser.parse_args()
    bot = MNFF(args)
    asyncio.run(bot.start(args.url, args.token))
