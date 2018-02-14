#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

# skin, skin, skin, skin
# skin 2rd, skin 2rd, skin 2rd, skin 2rd,
# eye, eye 2nd, mouth
# hair, hair(white)
# ear, ear
# patch(1f3cc)
original_colors = (
    '#FBC11B', '#FBC21A', '#FCC21B', '#FAC01B', '#FAC036',
    '#E48C15', '#E8A23D', '#E59600', '#E59900', '#E49500',
    '#C07B47', '#444444', '#513F35',
    '#6D4C41', '#E0E0E0',
    '#E49500', '#E39400',
    '#FFB300'
)
replace_colors = (
    ('1f3fb', (
    '#FADCBC', '#FADCBC', '#FADCBC', '#FADCBC', '#FADCBC',
    '#DBA689', '#DBA689', '#DBA689', '#DBA689', '#DBA689',
    '#C17B47', '#444444', '#513F35',
    '#312D2D', '#E0E0E0',
    '#DBA689', '#DBA689',
    '#FFCF9D')),
    ('1f3fc', (
    '#E0BB95', '#E0BB95', '#E0BB95', '#E0BB95', '#E0BB95',
    '#C48E6A', '#C48E6A', '#C48E6A', '#C48E6A', '#C48E6A',
    '#C17B47', '#5D4037', '#513F35',
    '#BFA055', '#E0E0E0',
    '#C48E6A', '#C48E6A',
    '#DAAE81')),
    ('1f3fd', (
    '#BF8F68', '#BF8F68', '#BF8F68', '#BF8F68', '#BF8F68',
    '#99674F', '#99674F', '#99674F', '#99674F', '#99674F',
    '#704324', '#5D4037', '#49362E',
    '#704324', '#E0E0E0',
    '#99674F', '#99674F',
    '#B78156')),
    ('1f3fe', (
    '#9B643C', '#9B643C', '#9B643C', '#9B643C', '#9B643C',
    '#7A4C32', '#7A4C32', '#7A4C32', '#7A4C32', '#7A4C32',
    '#42312C', '#42312C', '#352620',
    '#47352D', '#BDBDBD',
    '#7A4C32', '#7A4C32',
    '#885834')),
    ('1f3ff', (
    '#70534A', '#70534A', '#70534A', '#70534A', '#70534A',
    '#35201A', '#35201A', '#35201A', '#35201A', '#35201A',
    '#232020', '#232020', '#261819',
    '#232020', '#BDBDBD',
    '#563E37', '#563E37',
    '#60473F')),
)

filename = sys.argv[1]
fnbase = os.path.splitext(filename)[0]

spl_200d = fnbase.split('_200d_', 1)
if len(spl_200d) == 1:
    fnbase += '_%s.svg'
else:
    fnbase = '%s_%%s_200d_%s.svg' % tuple(spl_200d)

svg = open(filename, 'r', encoding='utf-8').read()

for modifier, colors in replace_colors:
    with open(fnbase % modifier, 'w', encoding='utf-8') as w:
        modified = svg
        for orig, var in zip(original_colors, colors):
            modified = modified.replace(orig, var)
            modified = modified.replace(orig.lower(), var)
        w.write(modified)
