"""
Themes/Font Definitions
=======================

.. seealso::

   `Material Design spec, The type system <https://material.io/design/typography/the-type-system.html>`_
"""

from kivy.core.text import LabelBase

from kivymd import fonts_path

fonts = [
    {
        "name": "Roboto",
        "fn_regular": fonts_path + "MiSans-Normal.ttf",
        "fn_bold": fonts_path + "MiSans-Normal.ttf",
        "fn_italic": fonts_path + "MiSans-Normal.ttf",
        "fn_bolditalic": fonts_path + "MiSans-Normal.ttf",
    },
    {
        "name": "RobotoThin",
        "fn_regular": fonts_path + "MiSans-Normal.ttf",
        "fn_italic": fonts_path + "MiSans-Normal.ttf",
    },
    {
        "name": "RobotoLight",
        "fn_regular": fonts_path + "MiSans-Normal.ttf",
        "fn_italic": fonts_path + "MiSans-Normal.ttf",
    },
    {
        "name": "RobotoMedium",
        "fn_regular": fonts_path + "MiSans-Normal.ttf",
        "fn_italic": fonts_path + "MiSans-Normal.ttf",
    },
    {
        "name": "RobotoBlack",
        "fn_regular": fonts_path + "MiSans-Normal.ttf",
        "fn_italic": fonts_path + "MiSans-Normal.ttf",
    },
    {
        "name": "Icons",
        "fn_regular": fonts_path + "materialdesignicons-webfont.ttf",
    },
]

for font in fonts:
    LabelBase.register(**font)

theme_font_styles = [
    "H1",
    "H2",
    "H3",
    "H4",
    "H5",
    "H6",
    "Subtitle1",
    "Subtitle2",
    "Body1",
    "Body2",
    "Button",
    "Caption",
    "Overline",
    "Icon",
]
"""
.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/font-styles-2.png
"""
