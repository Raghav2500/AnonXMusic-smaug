from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode
import config
from ..logging import LOGGER
proxy = {
    "scheme": "http",  # "socks4", "socks5" and "http" are supported
    "hostname": "proxy.proxyverse.io",
    "port": 9200,
    "username": "country-in",
    "password": "9b01816d-048c-42e7-8686-411f91665d28"
}
class Anony(Client):
    def init(self):
        LOGGER(name).info(f"Starting Bot...")
        super().init(
            name="AnonXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            proxy=proxy,
            in_memory=True,
            max_concurrent_transmissions=7,
        )
    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention
        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>   {self.mention}  ^y  ^o  ^{ s  ^{  ^ ^  ^{  ^g  ^e :<>
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(name).error(
                "Bot has failed to access the log group/channel. Make sure that you ha>
            )
            exit()
        except Exception as ex:
            LOGGER(name).error(
                f"Bot has failed to access the log group/channel.\n  Reason : {type(ex>
            )
            exit()
        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(name).error(
                "Please promote your bot as an admin in your log group/channel."
            )
            exit()
        LOGGER(name).info(f"Music Bot Started as {self.name}")
    async def stop(self):
        await super().stop()
`
