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
        frames = ['ac', 'acab', 'al', 'amouranth', 'bann', 'beatles', 'bjork', 'blond',
                  'blood', 'bop', 'brazzers', 'bulge', 'can', 'cat', 'cj1', 'cnid',
                  'coil1', 'coil2', 'comic1', 'comic2', 'commie', 'conway', 'cooper1', 'cooper2', 'cowboy',
                  'crosshair', 'cry', 'dab1', 'damn', 'dg', 'dick', 'die', 'dole', 'elon', 'fuckyou',
                  'funwaa', 'gag', 'garf2', 'garf3', 'garf4', 'garf5', 'gay',
                  'general', 'grinch', 'hhill', 'hillary', 'idub1', 'idub2', 'idub3', 'idub4', 'idub5', 'idub6',
                  'ifunny', 'jempy', 'jf1', 'jf2', 'kim', 'knuckle', 'liberal', 'lilpeep', 'lilpump',
                  'lrd', 'lynch', 'madvillainy', 'mark', 'meme1', 'nmh',
                  'obama2', 'parental', 'pickle', 'piss', 'preg', 'qotsa', 'rh', 'sam',
                  'sb', 'shapiro', 'shrek', 'shutterstock', 'sketch', 'socks', 'sonic', 'spaghett',
                  'spongebob', 'ss', 'swans', 'swear1', 'swear2', 'sy', 'television', 'testframe', 'tmay',
                  'tp', 'trigger', 'trump', 'unlock', 'vine1', 'vu', 'warcrime', 'wasted', 'wish',
                  'wtc2', 'zucc', 'zucc1', 'zucc2', 'zucc3', 'zucc4']
        templates =[
            ('altright', 9, 195, 888, 492),
            ('buzzfeed', 16, 86, 571, 330),
            ('calvin', 0, 0, 300, 28),
            ('clash', 59, 0, 283, 225),
            ('cruz', 75, 26, 384, 318),
            ('funeral', 46, 55, 310, 128),
            ('garf1', 35, 48, 229, 190),
            ('gccx1', 0, 49, 640, 382),
            ('gccx2', 0, 19, 259, 154),
            ('jones', 503, 0, 684, 717),
            ('mars', 204, 0, 330, 246),
            ('memri', 28, 9, 633, 288),
            ('n64', 119, 67, 258, 258),
            ('nut', 0, 87, 714, 546),
            ('obama1', 7, 90, 441, 288),
            ('picard', 0, 0, 600, 307),
            ('porn', 15, 82, 761, 420),
            ('rapper', 0, 66, 522, 444),
            ('science', 0, 147, 1000, 686),
            ('son', 0, 86, 569, 527),
            ('wedding', 158, 12, 236, 245),
            ('wtc1', 0, 0, 300, 238)
        ]
        for frame in frames:
            @commands.cooldown(1, 5, commands.BucketType.user)
            @commands.command(name=frame, description="frame")
            async def cmd():
                pass

            self.client.add_command(cmd)

        for template, x, y, width, height in templates:
            @commands.cooldown(1, 5, commands.BucketType.user)
            @commands.command(name=template, description="template {} {} {} {}".format(x, y, width, height))
            async def cmd():
                pass

            self.client.add_command(cmd)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="addframe")
    async def addtestframe(self):
        pass

# func thinggy
    async def on_command(self, command, ctx):
        if not command.description:
            return
        split = command.description.split()
        picture_path = str(ctx.message.channel.id)+'.png'
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
        elif split[0] == "addframe":
            await self.get_attachment_images(ctx)
            test_image = Image.open(picture_path)
            test_image.convert("RGBA").save("frames/testframe.png")
            await self.client.send_message(ctx.message.channel, "Changed test frame")
            return
        else:
            return
        frame_path = "frames/"+frame_name+".png"
        await self.client.send_message(ctx.message.channel, "**processing...**")
        await self.filtered_image(ctx, picture_path, frame_path, background_offset, background_resize)
        await self.client.send_file(ctx.message.channel, picture_path)

    async def filtered_image(self, ctx, picture_path, chosen_filter, background_offset=(0, 0), background_resize=None):
        await self.get_attachment_images(ctx)
        # "background" is the image to edit, "foreground" is the frame
        background = Image.open(picture_path)
        foreground = Image.open(chosen_filter)
        if background_resize:
            background = background.resize(background_resize, Image.ANTIALIAS)
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
