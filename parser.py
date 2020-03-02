from display import *
from matrix import *
from draw import *


def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    lines = f.readlines()
    lines = [s.strip() for s in lines]
    i = 0
    while (i < len(lines)):
        if lines[i] == "line":
            i = i + 1
            endpoints = lines[i].split(" ")
            endpoints = [int(x) for x in endpoints]
            add_edge(points, endpoints[0], endpoints[1], endpoints[2], endpoints[3], endpoints[4], endpoints[5])
        if lines[i] == "ident":
            ident(transform)
        if lines[i] == "scale":
            i = i + 1
            args = lines[i].split(" ")
            args = [int(x) for x in args]
            new = make_scale(args[0], args[1], args[2])
            matrix_mult(new, transform)
        if lines[i] == "move":
            i = i + 1
            args = lines[i].split(" ")
            args = [int(x) for x in args]
            new = make_translate(args[0], args[1], args[2])
            matrix_mult(new, transform)
        if lines[i] == "rotate":
            i = i + 1
            args = lines[i].split(" ")
            theta = int(args[1])
            # print(theta)
            if args[0] == "x":
                new = make_rotX(theta)
            if args[0] == "y":
                new = make_rotY(theta)
            if args[0] == "z":
                new = make_rotZ(theta)
            matrix_mult(new, transform)
        if lines[i] == "apply":
            matrix_mult(transform, points)
        if lines[i] == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        if lines[i] == "save":
            i = i + 1
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_ppm(screen, "image.ppm")
            save_extension(screen, lines[i])
        if lines[i] == "quit":
            break
        i = i + 1
    f.close()
