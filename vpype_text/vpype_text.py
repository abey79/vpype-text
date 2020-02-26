import logging

import click
from vpype.model import LineCollection
from vpype.decorators import generator
from vpype.utils import Length
import axi

FONTS = {
    "astrology": axi.hershey_fonts.ASTROLOGY,
    "cursive": axi.hershey_fonts.CURSIVE,
    "cyrilc_1": axi.hershey_fonts.CYRILC_1,
    "cyrillic": axi.hershey_fonts.CYRILLIC,
    "futural": axi.hershey_fonts.FUTURAL,
    "futuram": axi.hershey_fonts.FUTURAM,
    "gothgbt": axi.hershey_fonts.GOTHGBT,
    "gothgrt": axi.hershey_fonts.GOTHGRT,
    "gothiceng": axi.hershey_fonts.GOTHICENG,
    "gothicger": axi.hershey_fonts.GOTHICGER,
    "gothicita": axi.hershey_fonts.GOTHICITA,
    "gothitt": axi.hershey_fonts.GOTHITT,
    "greek": axi.hershey_fonts.GREEK,
    "greekc": axi.hershey_fonts.GREEKC,
    "greeks": axi.hershey_fonts.GREEKS,
    "japanese": axi.hershey_fonts.JAPANESE,
    "markers": axi.hershey_fonts.MARKERS,
    "mathlow": axi.hershey_fonts.MATHLOW,
    "mathupp": axi.hershey_fonts.MATHUPP,
    "meteorology": axi.hershey_fonts.METEOROLOGY,
    "music": axi.hershey_fonts.MUSIC,
    "rowmand": axi.hershey_fonts.ROWMAND,
    "rowmans": axi.hershey_fonts.ROWMANS,
    "rowmant": axi.hershey_fonts.ROWMANT,
    "scriptc": axi.hershey_fonts.SCRIPTC,
    "scripts": axi.hershey_fonts.SCRIPTS,
    "symbolic": axi.hershey_fonts.SYMBOLIC,
    "timesg": axi.hershey_fonts.TIMESG,
    "timesi": axi.hershey_fonts.TIMESI,
    "timesib": axi.hershey_fonts.TIMESIB,
    "timesr": axi.hershey_fonts.TIMESR,
    "timesrb": axi.hershey_fonts.TIMESRB,
}


@click.command(name="text")
@click.argument("string", type=str)
@click.option(
    "-f", "--font", type=click.Choice(FONTS.keys()), default="futural", help="Font to use."
)
@click.option("-s", "--size", type=Length(), default=18, help="Text size (default: 18).")
@click.option(
    "-p",
    "--position",
    nargs=2,
    type=Length(),
    default=[0, 0],
    help="Position of the text (default: 0, 0).",
)
@click.option(
    "-a",
    "--align",
    type=click.Choice(["left", "right", "center"]),
    default="left",
    help="Text alignment with respect to position (default: left).",
)
@generator
def vpype_text(string, font, size, position, align):
    """
    Generate text using a Hershey font.
    """

    # skip if text is empty
    if string.strip() == "":
        return LineCollection()

    lines = axi.text(string, font=FONTS[font])
    lc = LineCollection()
    for line in lines:
        lc.append([x + 1j * y for x, y in line])

    # by default, axi's font appear to be approx 18px size
    scale_factor = size / 18.
    lc.scale(scale_factor, scale_factor)

    min_x, _, max_x, _ = lc.bounds()
    if align == "left":
        lc.translate(-min_x, 0)
    elif align == "center":
        lc.translate(-(max_x - min_x) / 2, 0)
    elif align == "right":
        lc.translate(-max_x, 0)
    else:
        logging.warning(f"text: unknown align parameters: {align}")

    lc.translate(position[0], position[1])

    return lc


vpype_text.help_group = "Plugins"
