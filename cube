#!/usr/bin/env python
from scurve import hilbert
import cubictemp

"""
    This program outputs a POV-Ray definition file. 

    We render the curve into a 100x100 cube, with the mid-point of the cube at
    the origin. You may have to fiddle with the resulting file to adjust the
    camera location to suit the resulting image.

    You can render it with a command like the following:
        
        povray -W500 -H500 -Q10 +A0.8 +Q11 +P ./file.pov
"""


pov = """
global_settings { 
    assumed_gamma 2.2 
}

camera {
    up 1
    right 1
    location  <50, 50, -200>
    look_at   <0, 0, 0>
    rotate z*270
    rotate x*25
    rotate y*10
}

background { color red 0 green 0 blue 0 }

light_source { 
    <50, 30, -200> color red 1 green 1 blue 1 
}

blob {
  threshold 0.5
  <!--(for i in lines)-->
    cylinder { 
        <@!i[0][0]!@, @!i[0][1]!@, @!i[0][2]!@>, 
        <@!i[1][0]!@, @!i[1][1]!@, @!i[1][2]!@>, 
        4, 1
    }
    sphere { 
        <@!i[0][0]!@, @!i[0][1]!@, @!i[0][2]!@>, 
        4, 1
    }
  <!--(end)-->
    sphere { 
        <@!lines[0][0][0]!@, @!lines[0][0][1]!@, @!lines[0][0][2]!@>, 
        6, 1
        pigment { color red 0.5 green 0.5 blue 1 }
    }
  pigment { color red 0.5 green 0.5 blue 1 }
  finish { ambient 0.2 diffuse 0.8 phong 1 }
}
"""

# Size of the PovRay cube
SIZE = float(100)


def maken(n, scale):
    lines = []
    current = None
    for v in n:
        v = [i*scale-SIZE/2 for i in v]
        if not current:
            current = v
            continue
        lines.append((current, v))
        current = v
    return lines


def main():
    from optparse import OptionParser, OptionGroup
    parser = OptionParser(
                usage = "%prog [options] output",
                version="%prog 0.1",
            )
    parser.add_option(
        "-o", "--order", action="store",
        type="int", dest="order", default=3
    )
    options, args = parser.parse_args()
    if len(args) != 1:
        parser.error("Please specify output file.")

    c = hilbert.Hilbert(3, options.order)
    scale = SIZE/c.dimensions()[0]
    t = cubictemp.Template(
            pov,
            lines = maken(c, scale),
            scale = scale
        )
    f = open(args[0], "w")
    f.write(str(t))


main()
