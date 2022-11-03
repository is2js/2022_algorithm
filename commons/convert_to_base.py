def convert(number, base):
    share: int
    remainder: int
    share, remainder = divmod(number, base)

    if not share:
        return str(remainder)

    return convert(share, base) + str(remainder)
