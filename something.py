import argparse
import drawBot as db


def _get_options():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        'fontname'
    )
    ap.add_argument(
        '-m', '--message',
        default="Hello, world!"
    )
    ap.add_argument(
        '-s', '--size',
        default=100
    )

    return ap.parse_args()


def main(opts):
    message = opts.message
    fontname = opts.fontname
    fontsize = opts.size

    if fontname not in db.installedFonts():
        print(f'{fontname} not found')
        print("\n".join(db.installedFonts()))

    db.font(fontname, fontsize)
    wx, ht = db.textSize(message)
    db.newPage(width=wx * 1.25, height=ht * 1.25)
    db.font(fontname, fontsize)
    db.text(message, ((db.width() - wx)/2, db.height() - db.fontAscender()))
    db.saveImage("out.pdf")


if __name__ == '__main__':
    args = _get_options()
    main(args)