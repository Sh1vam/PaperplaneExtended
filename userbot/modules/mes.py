from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"mes ?(.*)"))
async def mes(event):
    new_update = await borg.get_entity('me')
    await event.edit(new_update.stringify())
