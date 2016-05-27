#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def get_line_coef(x1, y1, x2, y2):
    dy = y2 - y1
    dx = x2 - x1
    a = dy
    b = -dx
    c = dx*y1 - dy*x1
    return a, b, c


def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    a1, b1, c1 = get_line_coef(x1, y1, x2, y2)
    a2, b2, c2 = get_line_coef(x3, y3, x4, y4)
    r = a1*b2 - a2*b1
    if r > 0.0000000001:
        x = - (c1*b2 - c2*b1) / r
        y = - (a1*c2 - a2*c1) / r
        return x, y
    else:
        return None, None


def dist(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5


def deg(a):
    return a*180 / math.pi


def rad(a):
    return normalize(a*math.pi / 180)


def normalize(a):
    while a > 2*math.pi:
        a -= 2*math.pi
    while a < 0:
        a += 2*math.pi
    return a


def show_vars(f):
    def tmp(*args, **kwargs):
        print 'sent to', f.__name__, args, kwargs
        return f(*args, **kwargs)
    return tmp


def dir_angle(x1, y1, x2, y2):
    dy = y2 - y1
    dx = x2 - x1
    if dx == 0 and dy == 0:
        return 0
    result = math.acos(abs(dy) / dist(x1, y1, x2, y2))
    if dx < 0 and dy >= 0:
        result = 2*math.pi - result
    elif dx < 0 and dy < 0:
        result = math.pi + result
    elif dx >= 0 and dy < 0:
        result = math.pi - result
    return result


def get_angle(p1, p2, p3):
    a1 = dir_angle(p2[0], p2[1], p1[0], p1[1])
    a2 = dir_angle(p2[0], p2[1], p3[0], p3[1])
    return normalize(a1 - a2)


# @show_vars
def add_point(p1, p2, d, a):
    a1 = normalize(dir_angle(p2[0], p2[1], p1[0], p1[1]))
    a1 -= a + math.pi
    x = round(p1[0] + math.sin(a1) * d, 2)
    y = round(p1[1] + math.cos(a1) * d, 2)
    return [x, y]


def orthogonalize_poly(poly):
    poly1 = poly[:]
    if poly1[0] == poly1[-1]:
        poly1.pop()
    poly1.insert(0, poly1[-1])
    poly1.append(poly[0])

    angles = []
    lens = []
    for p1, p2 in zip(poly, poly[1:]):
        lens.append(dist(p2[0], p2[1], p1[0], p1[1]))

    for p1, p2, p3 in zip(poly1, poly1[1:], poly1[2:]):
        angles.append(deg(get_angle(p1, p2, p3)))

    norm_angles = []
    for a in angles:
        n = round(a / 45, 0)
        norm_angles.append(n*45)

    norm_lens = []
    for l, a, a1 in zip(lens, angles, norm_angles):
        norm_lens.append(l * math.cos(rad(abs(a-a1))))

    new_poly = poly[:2]
    for a, l in zip(norm_angles[1:], norm_lens[1:]):
        new_poly.append(add_point(new_poly[-1], new_poly[-2], l, rad(a)))
    x, y = intersect(new_poly[0][0],new_poly[0][1],
                     new_poly[1][0],new_poly[1][1],
                     new_poly[-2][0],new_poly[-2][1],
                     new_poly[-1][0],new_poly[-1][1])
    if x:
        new_poly[0][0],new_poly[0][1] = x, y
        new_poly[-1][0],new_poly[-1][1] = x, y
    return new_poly

if __name__ == '__main__':
    poly = [[1.0, 1.],
            [1.1, 2.],
            [2., 2.],
            [2., 3.],
            [2., 1.],
            [1.0, 1.]
            ]
    print orthogonalize_poly(poly)
