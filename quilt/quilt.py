#!/usr/bin/env python3

"""
Stanford CS106A Quilt Project
"""

import sys
from drawcanvas import DrawCanvas


def draw_bars(canvas, left, top, width, height, n):
    """
    Draw bars in the given canvas at left, top, with width, height, n
    """
    canvas.draw_rect(left, top, width, height, color='lightblue')
    # calculation of width between each of the lines
    lnw = (width - 1)/(n - 1)
    # loop that creates lines for amount n
    for i in range(n):
        canvas.draw_line(left + (lnw * i), top, left + (lnw * i), top + height)


def draw_eye(canvas, left, top, width, height, n):
    """
    Draw eye in the given canvas at left, top with width, height, n
    """
    canvas.draw_rect(left, top, width, height, color='lightblue')
    canvas.fill_oval(left, top, width, height, color='yellow')
    # calculation of width between each of the lines
    lnw = (width - 1)/(n - 1)
    # loop that creates lines starting at center distributed evenly across bottom
    for i in range(n):
        canvas.draw_line(left + (width - 1)/2, top + (height - 1)/2, left + (lnw * i), top + height)


def draw_bowtie(canvas, left, top, width, height, n):
    """
    Draw bowtie in the given canvas at left, top, with width, height, n
    """
    canvas.draw_rect(left, top, width, height, color='lightblue')
    # calculate height of separation between lines
    lnh = (height -1) / (n -1)
    # loop that draws lines for bowtie design
    for i in range(n):
        canvas.draw_line(left, top + (lnh * i), left + width - 1, top + height - 1 - (lnh * i), color='red')


def draw_power(canvas, left, top, width, height, n):
    """
    Draw power patch at the given left, top, with width, height, n.
    """
    canvas.draw_rect(left, top, width, height, color='lightblue')

    # draws combination of bowtie and eye designs in diagonal pattern
    draw_bowtie(canvas, left, top, width/2, height/2, n)
    draw_eye(canvas, left + (width - 1)/2, top + (height - 1)/2, width/2, height/2, n)


def draw_quilt(width, height, n):
    """
    Create a canvas of width, height and draw the whole
    quilt on it. Draw a n by n grid of patches.
    """
    canvas = DrawCanvas(width, height, title="Quilt")


    patch_width = width / n
    patch_height = height / n

    # loop that goes through each box and assigns a quilt pattern
    for row in range(n):
        for col in range(n):
            left = col * patch_width
            top = row * patch_height
            choice = (row + col) % 4
            if choice == 0:
                draw_bars(canvas, left, top, patch_width, patch_height, n)
            if choice == 1:
                draw_eye(canvas, left, top, patch_width, patch_height, n)
            if choice == 2:
                draw_power(canvas, left, top, patch_width, patch_height, n)
            if choice == 3:
                draw_bowtie(canvas, left, top, patch_width, patch_height, n)


# main() code is complete.
# There are 5 command lines that work here,
# with width/height/n being positive integers.
#  -bars width height n
#  -eye width height n
#  -bowtie width height n
#  -power width height n
#  -quilt width height n
# e.g. run like this in the terminal:
#  python3 quilt.py -bars 600 400 10


def main():
    # main() code is complete.
    # This main() is not a great example of command line processing,
    # as this application has some unusual issues.

    args = sys.argv[1:]
    if len(args) != 4:
        print('usage: (one of -bars -eye -bowtie -power -quilt) width height n')
        return

    # Parse width/height/n from command line, giving a helpful
    # error message if it fails.
    try:
        window_width = int(args[1])
        window_height = int(args[2])
        n = int(args[3])
    except Exception:
        print("Error parsing int width/height/n from command line:" + ' '.join(args))
        return

    # Width/height of one patch
    width = window_width / 2
    height = window_height / 2

    # Tricky: we do all the drawing in a try, so that if it takes an exception,
    # we can still do the mainloop() at the end. If we do not do this, an exception
    # causes no graphics output to appear which makes debugging hard.
    try:
        if args[0] == '-bars':
            canvas = DrawCanvas(window_width, window_height, fast_draw=True, title='Quilt')
            # Can change to fast_draw=False .. drawing plays out more slowly
            draw_bars(canvas, 0, 0, width, height, n)
            draw_bars(canvas, width, height, width, height, n)

        if args[0] == '-eye':
            canvas = DrawCanvas(window_width, window_height, fast_draw=True, title='Quilt')
            draw_eye(canvas, 0, 0, width, height, n)
            draw_eye(canvas, width, height, width, height, n)

        if args[0] == '-bowtie':
            canvas = DrawCanvas(window_width, window_height, fast_draw=True, title='Quilt')
            draw_bowtie(canvas, 0, 0, width, height, n)
            draw_bowtie(canvas, width, height, width, height, n)

        if args[0] == '-power':
            canvas = DrawCanvas(window_width, window_height, fast_draw=True, title='Quilt')
            draw_power(canvas, 0, 0, width, height, n)
            draw_power(canvas, width, height, width, height, n)

        if args[0] == '-quilt':
            draw_quilt(window_width, window_height, n)

    # Print out exception from draw
    except Exception as e:
        print(e)

    DrawCanvas.mainloop()


if __name__ == '__main__':
    main()
