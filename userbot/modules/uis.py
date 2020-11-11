from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"uis ?(.*)"))
async def ues(event):
    giveVar = event.text
    a = giveVar[5:]
    try:
        new_update = await borg.get_entity(int(a))
    except ValueError:
        new_update = await borg.get_entity('me')
    await event.edit(new_update.stringify())
