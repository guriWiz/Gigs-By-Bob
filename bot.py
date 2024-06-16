from dotenv import load_dotenv
import os
import discord
from discord import Embed, ButtonStyle, Interaction
from discord.ext import tasks
from bob.logger import LOGGER
from discord.ui import View, Button, button

load_dotenv()
from bob.freelancer import FreelancerBob

class BobBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def send_gig(self, gig, gig_ch):
        pj_curr = gig["pj_curr"]
        pj_user = gig["pj_user"]

        gig_msg = ""
        gig_msg += f"**URL** - {gig['pj_url']} \n\n"
        gig_msg += f"**Type** - {gig['pj_type']} \n"
        gig_msg += f"**Bid Period** - {gig['bid_p']} \n"
        gig_msg += f"**Total Bids** - {gig['bids']} \n"
        gig_msg += f"**Budget** - {pj_curr} {gig['pj_min_bdg']} to {pj_curr} {gig['pj_max_bdg']} \n"
        gig_msg += f"**Avg. Bid Price** - {pj_curr} {gig['avg_bid']} \n\n"
        gig_msg += f"**Description :** \n"
        gig_msg += f"```{gig['pj_desc']}``` \n"
        gig_msg += f"**Submitted On** - {gig['submit_dt']} \n"
        gig_msg += f"**Updated At** - {gig['update_dt']} \n"

        gig_embed = Embed(
            title=f"**[{gig['pj_id']}] {gig['pj_title']}**",
            description=gig_msg,
            color=discord.Color.random()
        )

        gig_embed.set_author(
            name=f"[{pj_user["u_id"]}] {pj_user["u_name"]}",
            url=pj_user["u_url"],
            icon_url=pj_user["u_avatar"]
        )
        # gig_embed.set_footer(text=gfi_data["labels"], icon_url=gfi_data["avatar_url"])

        await gig_ch.send(embed=gig_embed)

    async def on_ready(self):
        LOGGER.info(f"{bob_client.user} has connected to discord!")

        fb = FreelancerBob()
        gig_data = fb.fetch_projects()

        gig_ch = bob_client.get_channel(int(GUILD_ID))
        await gig_ch.purge(limit=1000) # Purges the last 1000 messages from the channel

        for gig in gig_data:
            await self.send_gig(gig, gig_ch)

if __name__ == '__main__':

    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    GUILD_ID = os.getenv("GUILD_ID")

    bob_client = BobBot(intents=discord.Intents.default())
    bob_client.run(DISCORD_TOKEN)