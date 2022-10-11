#MenuTitle: << Previous Component
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
__doc__="""
Replaces the selected component with the previous one in the components list.
"""
import re

thisFont = Glyphs.font # frontmost font
selectedLayers = thisFont.selectedLayers # active layers of selected glyphs
thisLayer = selectedLayers[0]

for component in thisLayer.components:
	if component.selected == True:
		cName = component.name
		cNum = int(re.search(r'\d+$', cName).group())
		lastNumber = cNum - 1
		lastNumber = str(lastNumber)
		newName = cName[:-(len(str(cNum)))] + lastNumber
		component.name = newName
	else:
		Message("Please select a numbered component (dot_3, tail5…) for the script to work.")
