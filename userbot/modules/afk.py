"""AFK Plugin for DARK COBRA
Syntax: .afk REASON"""
import asyncio
import datetime
from telethon import events
from telethon.tl import functions, types
from userbot.utils import admin_cmd

global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global last_afk_message  # pylint:disable=E0602
USER_AFK = {}
afk_time = None
last_afk_message = {}


@borg.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_afk(event):
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    current_message = event.message.message
    if ".afk" not in current_message and "yes" in USER_AFK:  # pylint:disable=E0602
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PLUGIN_CHANNEL,  # pylint:disable=E0602
                "Mine Owner has gone for some Important work he is very busy😅"
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await borg.send_message(  # pylint:disable=E0602
                event.chat_id,
                "Please set `PLUGIN_CHANNEL` " + \
                "for the proper functioning of afk functionality " + \
                "in @Dark_cobra_support \n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True
            )
        USER_AFK = {}  # pylint:disable=E0602
        afk_time = None  # pylint:disable=E0602

@borg.on(admin_cmd(pattern=r"afk ?(.*)"))

async def _(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global reason
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    reason = event.pattern_match.group(1)
    if not USER_AFK:  # pylint:disable=E0602
        last_seen_status = await borg(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(
                types.InputPrivacyKeyStatusTimestamp()
            )
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()  # pylint:disable=E0602
        USER_AFK = f"yes: {reason}"  # pylint:disable=E0602
        if reason:
            await event.edit(f"My Boss is going afk(away from keyboard), and Reason is {reason}")
        else:
            await event.edit(f"My Boss is Going afk")
        await asyncio.sleep(5)
        await event.delete()
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PLUGIN_CHANNEL,  # pylint:disable=E0602
                f"My Boss Went {reason}"
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  # pylint:disable=E0602


@borg.on(events.NewMessage(  # pylint:disable=E0602
    incoming=True,
    func=lambda e: bool(e.mentioned or e.is_private)
))
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    afk_since = "**     last seen a long time ago..!**"
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_AFK and not (await event.get_sender()).bot:  # pylint:disable=E0602
        if afk_time:  # pylint:disable=E0602
            now = datetime.datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "**Yesterday**"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime('%A')
            elif hours > 1:
                afk_since = f"`{int(hours)}h{int(minutes)}m` **ago**"
            elif minutes > 0:
                afk_since = f"`{int(minutes)}m{int(seconds)}s` **ago**"
            else:
                afk_since = f"`{int(seconds)}s` **ago**"
        msg = None
        message_to_reply = f"𝐌𝐲 𝐦𝐚𝐬𝐭𝐞𝐫 𝐢𝐬 𝐠𝐨𝐧𝐞 𝐟𝐨𝐫 𝐬𝐨𝐦𝐞 𝐛𝐮𝐬𝐲 𝐰𝐨𝐫𝐤 {afk_since}\nWhere He Is: **𝐈 𝐀𝐌 𝐍𝐎𝐓 𝐁𝐎𝐓𝐇𝐄𝐑𝐄𝐃           𝐋𝐚𝐬𝐭 𝐬𝐞𝐞𝐧 𝐚 𝐥𝐨𝐧𝐠 𝐭𝐢𝐦𝐞 𝐚𝐠𝐨..!                          𝐑𝐄𝐀𝐒𝐎𝐍 𝐆𝐈𝐕𝐄𝐍 𝐁𝐄𝐋𝐎𝐖, 𝐈𝐅 𝐍𝐎𝐓 𝐓𝐇𝐄𝐍 𝐈𝐓𝐒 𝐍𝐎𝐍𝐄 𝐎𝐅 𝐌𝐘 𝐁𝐔𝐒𝐒𝐈𝐍𝐄𝐒𝐒 𝐓𝐎 𝐈𝐍𝐓𝐄𝐑𝐅𝐀𝐈𝐑 𝐈𝐍 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑'𝐒 𝐖𝐎𝐑𝐊 𝐒𝐎 𝐁𝐄𝐓𝐓𝐄𝐑 𝐖𝐀𝐈𝐓 𝐅𝐎𝐑 𝐒𝐎𝐌𝐄𝐓𝐈𝐌𝐄 𝐓𝐈𝐋𝐋 𝐇𝐄 𝐂𝐎𝐌𝐄𝐒❤** " + \
            f"\n\n__ I'll back soon!__\n**REASON**: {reason}" \
            if reason \
            else f"**Important Notice**\n\n[This User Is little busy now!...](https://telegra.ph/file/a4821748db331a0c899a0.mp4) "
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(5)
        if event.chat_id in last_afk_message:  # pylint:disable=E0602
            await last_afk_message[event.chat_id].delete()  # pylint:disable=E0602
        last_afk_message[event.chat_id] = msg  # pylint:disable=E0602
