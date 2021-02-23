import argparse


async def github_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type=str)
    parser.add_argument('priv', type=bool)
    parser.add_argument('description', type=str)
    parser.add_argument('ret', type=bool, default=True)
    return parser
