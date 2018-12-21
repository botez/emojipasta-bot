import discord
from discord.ext import commands
from random import randint
from discord.ext.commands.cooldowns import BucketType
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import urllib.request
from util.functions import Functions


class Frames():
    def __init__(self, client):
        self.client = client

# meme frames
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame zucc1 zucc2 zucc3 zucc4")
    async def zucc(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def zucc1(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def zucc2(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def zucc3(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def zucc4(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def ifunny(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def funwaa(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def ss(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame idub1 idub2 idub3 idub4 idub5 idub6")
    async def idub(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def idub1(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def idub2(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def idub3(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def idub4(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def idub5(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def idub6(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame swear1 swear2")
    async def swear(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def swear1(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def swear2(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def shutterstock(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def commie(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def gay(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def kek(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def preg(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def trigger(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def cat(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def kim(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def sonic(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def tp(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def gag(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def knuckle(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def liberal(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def pickle(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def sb(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def nut(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def altright(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def buzzfeed(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def die(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def cry(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def dick(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def unlock(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def hillary(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def shrek(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def mark(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def memri(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def wish(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def porn(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def sam(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def wasted(self):
        pass

#music frames

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame coil1 coil2")
    async def coil(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def coil1(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def coil2(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def dg(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def viper(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def lrd(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def nmh(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def television(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def blond(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def ac(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def vu(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def lilpeep(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def lilpump(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def madvillainy(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def beatles(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def bjork(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def can(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def qotsa(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def swans(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def sy(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def damn(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def rh(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def wtc1(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def wtc2(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def dole(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def cnid(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def jf1(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def bann(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def bulge(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def jempy(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def shapiro(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="template 35 48 229 190")
    async def garf1(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def fuckyou(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def funeral(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def blood(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def clash(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def wedding(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def comic1(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def comic2(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def conway(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def crosshair(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def garf2(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def garf3(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def garf4(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def gccx1(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def gccx2(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def general(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def grinch(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def mars(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def picard(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def piss(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def science(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def socks(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def spaghett(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def vine1(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def warcrime(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def acab(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def al(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def amouranth(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def bop(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def brazzers(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def cj1(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def cooper1(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def cooper2(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def cruz(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def dab1(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def elon(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def garf5(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def hhill(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def jf2(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def jones(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def meme1(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def n64(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def obama1(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def obama2(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def parental(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def sketch(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def son(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def spongebob(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def tmay(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def trump(self):
        pass

# film frames
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def cowboy(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def lynch(self):
        pass

# func thinggy
    async def on_command(self, command, ctx):
        if not command.description:
            return
        split = command.description.split()
        if split[0] == "frame":
            if len(split) > 1:
                rand = randint(1, len(split) - 1)
                frame_name = split[rand]
            else:
                frame_name = str(command)
            background_offset = (0, 0)
            background_resize = None
        elif split[0] == "template":
            if len(split) != 5:
                return
            frame_name = str(command)
            try:
                x, y, width, height = [int(x) for x in split[1:]]
            except ValueError:
                return
            background_offset = (x, y)
            background_resize = (width, height)
        else:
            return
        frame_path = "frames/"+frame_name+".png"
        picture_path = str(ctx.message.channel.id)+'.png'
        await self.client.send_message(ctx.message.channel, "**processing...**")
        await self.filtered_image(ctx, picture_path, frame_path, background_offset, background_resize)
        await self.client.send_file(ctx.message.channel, picture_path)

    async def filtered_image(self, ctx, picture_path, chosen_filter, background_offset=(0, 0), background_resize=None):
        await self.get_attachment_images(ctx)
        # "background" is the image to edit, "foreground" is the frame
        background = Image.open(picture_path)
        foreground = Image.open(chosen_filter)
        if background_resize:
            background.resize(background_resize, Image.ANTIALIAS)
            # like a fucked up sandwich we paste the image over the frame, and then the frame again over the result
            foreground_copy = foreground.copy()
            foreground.paste(background, background_offset)
            foreground.paste(foreground_copy, (0, 0), foreground_copy)
            foreground.save(picture_path)
        else:
            w, h = background.size
            foreground = foreground.resize((w, h), Image.ANTIALIAS)
            background.paste(foreground, (0, 0), foreground)
            background.save(picture_path)

    async def get_attachment_images(self, ctx):
        last_attachment = None
        async for m in self.client.logs_from(ctx.message.channel, before=ctx.message, limit=20):
            if m.attachments:
                if len(m.attachments) > 0 and 'url' in m.attachments[0]:
                    last_attachment = m.attachments[0]['url']
                    if not Functions.is_image(last_attachment):
                        continue
                    else:
                        break
                else:
                    continue
            elif m.embeds:
                if len(m.embeds) > 0 and 'url' in m.embeds[0]:
                    last_attachment = m.embeds[0]['url']
                    if not Functions.is_image(last_attachment):
                        continue
                    else:
                        break
                else:
                    continue
        picture_path = str(ctx.message.channel.id)+'.png'
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        f = urllib.request.Request(url=last_attachment,headers=headers)
        f = urllib.request.urlopen(f)
        with open(picture_path, "wb") as c:
            c.write(f.read())


def setup(client):
    client.add_cog(Frames(client))
