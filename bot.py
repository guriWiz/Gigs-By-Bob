import traceback
from dotenv import load_dotenv
import os
import discord
from discord import Embed
from discord.ext import tasks
from bob.logger import LOGGER

load_dotenv()
from bob.freelancer import FreelancerBob

BOB_SLEEP_MINS = int(os.getenv("BOB_SLEEP_MINS", 5))

class BobBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def notify_err(self, gig_ch, err, tb_msg):
        err_embed = Embed(
            title=f"ERROR: {err}",
            description=f"```{tb_msg}```",
            color=discord.Color.dark_red()
        )

        await gig_ch.send(embed=err_embed)

    async def send_gig(self, gig, gig_ch):
        pj_curr = gig["pj_curr"]
        pj_user = gig["pj_user"]
        pj_atch = gig["pj_atch"]

        # Create attachments message
        gig_atch = ""

        for atch in pj_atch:
            gig_atch += f"- [{atch["atch_name"]}]({atch["atch_url"]}) \n"

        gig_msg = ""
        gig_msg += f"**URL** - {gig['pj_url']} \n\n"
        gig_msg += f"**Type** - {gig['pj_type']} \n"
        gig_msg += f"**Bid Period** - {gig['bid_p']} \n"
        gig_msg += f"**Total Bids** - {gig['bids']} \n"
        gig_msg += f"**Budget** - {pj_curr} {gig['pj_min_bdg']} to {pj_curr} {gig['pj_max_bdg']} \n"
        gig_msg += f"**Avg. Bid Price** - {pj_curr} {gig['avg_bid']} \n\n"
        gig_msg += f"**Description :** \n"
        gig_msg += f"```{gig['pj_desc']}``` \n"

        if pj_atch:
            gig_msg += f"**Attachments :** \n"
            gig_msg += f"{gig_atch} \n"
        
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
        gig_embed.set_footer(text=f"🛠️ {gig["pj_skills"]}")

        await gig_ch.send(embed=gig_embed)

    @tasks.loop(minutes=BOB_SLEEP_MINS)
    async def fetch_gig(self):
        gig_ch = bob_client.get_channel(int(GUILD_ID))

        try:
            gig_data = FreelancerBob().fetch_projects()

            # await gig_ch.purge(limit=1000) # Purges the last 1000 messages from the channel

            for gig in gig_data:
                await self.send_gig(gig, gig_ch)

        except Exception as err:
            err = str(err)[:240]
            tb_msg = traceback.format_exc()[:4000]
            
            LOGGER.error(err)
            LOGGER.error(tb_msg)

            await self.notify_err(gig_ch, err, tb_msg)

    @fetch_gig.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()

    async def on_ready(self):
        LOGGER.info(f"{bob_client.user} has connected to discord!")
        self.fetch_gig.start()

if __name__ == '__main__':

    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    GUILD_ID = os.getenv("GUILD_ID")

    bob_client = BobBot(intents=discord.Intents.default())
    bob_client.run(DISCORD_TOKEN)