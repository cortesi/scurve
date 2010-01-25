from distutils.core import setup

version = "0.1"

setup(
        name = "scurve",
        version = version,
        description = "A collection of space-filling curves and related algorithms.",
        author = "Aldo Cortesi",
        author_email = "aldo@corte.si",
        packages = ["scurve"],
        scripts = ["colormap", "cube", "drawcurve", "gray", "testpattern"],
)
