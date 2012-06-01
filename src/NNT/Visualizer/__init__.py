"""
Visualization tools

@author:  Hanno Sternberg <hanno@almostintelligent.de>
@version: 1.0.0

"""

import Colors
from graphViz import GraphViz

__all__ = ["Visualizer", "GraphViz"]

def useGraphViz(toolkit, filename, options):
	vis = GraphViz(toolkit)
	vis.visualize(filename, options)
	
def visualize(vis, toolkit, filename, options = {}):
	if (vis == "GraphViz"):
		useGraphViz(toolkit, filename, options = {})
