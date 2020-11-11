from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"gws?(.*)"))
async def gws(event):
    giveVar = event.text
    '''m = giveVar[5:-1]
    if not m:'''
    m = " Get Well Soon ! "
    f = giveVar[-1:]
    if f=="s":
        f = "🌹"
    elif not f:
        f = "🌹"
    await event.edit(
        f"{f}{f}{f}{f}{f}{f}{f} \n{f} {m} {f}\n{f}{f}{f}{f}{f}{f}{f}"
    )
