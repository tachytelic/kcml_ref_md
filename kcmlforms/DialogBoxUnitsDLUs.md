Dialog Box Units

Dialog Box Units or DBUs are computed from the height and width of the current system font. This will resize forms automatically to a sensible size irrespective of the font in use (many display drivers support several DPI scalings of points to pixels). However you should be careful about creating forms as big as will fit on the screen as they may not fit on a screen with a bigger fonts. Sarting with the 6.00 client KCML will attempt to resize the font automatically to scale such forms to fit without clipping.

To get the number of pixels in a vertical DBU take the system font base height and divide by eight. To get the number in a horizontal DBU take the average width and divide by four. The default system font for US Windows is 8pt MS Sans Serif.
