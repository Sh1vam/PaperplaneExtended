#Plugin Made by @Reborn_Eldorado & @NOOB_GUY_OP (less contribution)

import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRINGZ = [
  "inspirational-wallpaper",
  "inspirational-wallpaper-for-iphone",
  "inspirational-phone-wallpaper",
  "inspirational-wallpaper-for-my-desktop",
  "inspirational-iphone-6-wallpaper",
  "study-motivation-wallpaper",
  "athlete-motivation-wallpapers",
  "gym-motivation-wallpaper",
  "phone-wallpaper-quotes",
  "pretty-wallpapers-with-quotes",
  "nike-quotes-wallpaper"
]

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGZ) - 1)

    pack = COLLECTION_STRINGZ[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("http://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@borg.on(admin_cmd(pattern="motivedp ?(.*)"))

async def main(event):

    await event.edit("**Starting Motivative Profile Pics [i.e ]...\n\nDone !!! Check Your DP\n Plugin will be UPDATED SOON !! ") #Owner @Reborn_Eldorado, Fixed By @NOOB_GUY_OP

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(60) #Edit this to your required needs
