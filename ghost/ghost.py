#!/usr/bin/env python3

"""
Stanford CS106A Ghost Project
"""

import os
import sys

# This line imports SimpleImage for use here
# This depends on the Pillow package
from simpleimage import SimpleImage


def pix_dist2(pix1, pix2):
    """
    Returns the square of the color distance between 2 pix tuples.
    >>> pix_dist2((2, 2, 2), (1, 1, 1))
    3
    >>> pix_dist2((3, 3, 3), (1, 1, 1))
    12
    """
    red1 = pix1[0]
    green1 = pix1[1]
    blue1 = pix1[2]

    red2 = pix2[0]
    green2 = pix2[0]
    blue2 = pix2[0]

    # uses squared distance eqn (efficiency reasons) to calculate the squared distance between two pixels
    color_dist = ((red1 - red2) ** 2 + (green1 - green2) ** 2 + (blue1 - blue2) ** 2)
    return color_dist

def average_pix(pixs):
    """
    calculates the average pixel given a list of pixels
    >>> average_pix([(1, 4, 3), (9, 5, 6), (2, 3, 6)])
    (4.0, 4.0, 5.0)

    >>> average_pix([(4, 6, 2), (5, 6, 3), (3, 6, 4)])
    (4.0, 6.0, 3.0)
    """
    red = 0
    green = 0
    blue = 0
    length = len(pixs)

    # finds the sum of all the red, green, blue values
    for pix in pixs:
        red += pix[0]
        green += pix[1]
        blue += pix[2]

    # takes the sums and divides them by the length of the pixel list to find the average values
    avg_red = red/length
    avg_green = green/length
    avg_blue = blue/length

    # creates an average pixel tuples with the found average values for red, green, blue
    avg_pix = (avg_red, avg_green, avg_blue)
    return avg_pix


def best_pix(pixs):
    """
    Given a list of 1 or more pix, returns the best pix.
    >>> best_pix([(4, 5, 6), (7, 8, 9), (1, 2, 3)])
    (4, 5, 6)
    >>> best_pix([(6, 8, 9), (70, 81, 40), (1, 2, 3)])
    (6, 8, 9)
    """
    avg_pix = average_pix(pixs)
    # finds the pixel with minimum distance between pix and average pix
    return min(pixs, key=lambda pix: abs(pix_dist2(avg_pix, pix)))


def good_apple_pix(pixs):
    """
    Given a list of 2 or more pix, return the best pix
    according to the good-apple strategy.
    >>> good_apple_pix([(18, 18, 18), (0, 2, 0), (19, 23, 18), (19, 22, 18), (19, 22, 18), (1, 0, 1)])
    (19, 22, 18)
    """
    # uses the calculated average pixel to find the best half of all the pixels
    # using that better half only, calculates the best pixel and returns it
    avg_pix = average_pix(pixs)
    both_pix = sorted(pixs, key=lambda pix: abs(pix_dist2(pix, avg_pix)))
    good_pix = both_pix[:(len(both_pix) // 2)]
    return best_pix(good_pix)

def pixs_at_xy(images, x, y):
    """
    given a list of image objects and an x,y coordinate, return a list of pix
    """
    pix_list = []
    # loops through the images appending each pixel at provided x,y to a pixs list
    for i in range(len(images)):
        image = images[i]
        pix_list.append(image.get_pix(x,y))
    return pix_list


def solve(images, mode):
    """
    Given a list of image objects and mode,
    compute and show a Ghost solution image based on these images.
    Mode will be None or '-good'.
    There will be at least 3 images and they will all be
    the same size.
    """
    # assign width and height based off of first image
    width = images[0].width
    height = images[0].height
    # create a solution output image
    solution = SimpleImage.blank(width, height)
    # loop through the image x,y accessing pixs list for the x,y and based on the mode calculating the best pixel
    # calls either helper best_pix() or good_apple_pix() based on mode
    for y in range(height):
        for x in range(width):
            pixs = pixs_at_xy(images, x, y)
            if mode == '-good':
                best = good_apple_pix(pixs)
            if mode == None:
                best = best_pix(pixs)
            solution.set_pix(x,y,best)
    solution.show()


def jpgs_in_dir(dir):
    """
    (provided)
    Given the name of a directory
    returns a list of the .jpg filenames within it.
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided)
    Given a directory name, reads all the .jpg files
    within it into memory and returns them in a list.
    Prints the filenames out as it goes.
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print(filename)
        image = SimpleImage.file(filename)
        images.append(image)
    return images


def main():
    # (provided)
    args = sys.argv[1:]
    # Command line args
    # 1 arg:  dir-of-images
    # 2 args: -good dir-of-images
    if len(args) == 1:
        images = load_images(args[0])
        solve(images, None)

    if len(args) == 2 and args[0] == '-good':
        images = load_images(args[1])
        solve(images, '-good')


if __name__ == '__main__':
    main()
