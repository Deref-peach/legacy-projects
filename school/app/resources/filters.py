from vkwave.bots.core.dispatching.filters.base import BaseEvent, BaseFilter, FilterResult


class MatFilter(BaseFilter):
    async def check(self, event: BaseEvent) -> FilterResult:

        text: str = event.object.object.message.text
        mat: tuple = ("пизд", "хуй", "фак", "бля", "fuck")

        async for word in text.split():
            if word in mat:
                return FilterResult(True)
        return FilterResult(False)


class SetTimeTableFilter(BaseFilter):
    async def check(self, event: BaseEvent) -> FilterResult:
        if event["args"][1] == "-get":
            return FilterResult(True)

        return FilterResult(False)


class SetTimeTableFilter(BaseFilter):
    async def check(self, event: BaseEvent) -> FilterResult:
        if event["args"][1] == "-set":
            return FilterResult(True)

        return FilterResult(False)


class TimeTableFilter(BaseFilter):
    async def check(self, event: BaseEvent) -> FilterResult:

        if event["args"][0] == "!расписание":
            return FilterResult(True)

        return FilterResult(False)
