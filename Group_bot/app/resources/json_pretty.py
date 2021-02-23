import json


async def prettiefer(your_json: str):
    parsed = json.loads(your_json)
    return json.dumps(parsed, indent=2, sort_keys=True)
