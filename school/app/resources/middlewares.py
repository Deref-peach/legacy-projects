from vkwave.bots import BotEvent, MiddlewareResult

from .loader import bot


@bot.middleware()
async def event_check(event: BotEvent) -> MiddlewareResult:
    event["message"] = event.object.object.message
    event["text"] = event["message"].text
    event["args"] = event["text"].split()
    event["isday"] = "--day" in event["args"]

    return MiddlewareResult(True)
