from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"hii ?(.*)"))
async def hii(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "🌺"
    b = giveVar[7:8]
    if not b:
        b = "✨"
    await event.edit(
        f"{b}{a}{b}{b}{a}{b}{a}{b}\n
		{b}{a}{b}{b}{a}{b}{b}{b}\n
		{b}{a}{a}{a}{a}{b}{a}{b}\n
		{b}{a}{b}{b}{a}{b}{a}{b}\n
		{b}{a}{b}{b}{a}{b}{a}{b}\n
		☁☁☁☁☁☁☁☁"
    )
