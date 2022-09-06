"""Entry point for element drawing: nodes, ways, and relations."""
import argparse
from pathlib import Path

from map_machine.element.grid import Grid
from map_machine.osm.osm_reader import Tags, OSMNode


def draw_node(tags: Tags, path: Path):
    """Draw separate node."""
    grid: Grid = Grid(show_credit=False, margin=3.5)
    grid.add_node(tags, 0, 0)
    grid.draw(path)


def draw_way():
    """Draw way."""
    pass


def draw_area(tags: Tags, path: Path):
    """Draw closed way that should be interpreted as an area."""
    grid: Grid = Grid(show_credit=False, margin=0.5)
    node: OSMNode = grid.add_node({}, 0, 0)
    nodes: list[OSMNode] = [
        node,
        grid.add_node({}, 0, 1),
        grid.add_node({}, 1, 1),
        grid.add_node({}, 1, 0),
        node,
    ]
    grid.add_way(tags, nodes)
    grid.draw(path)


def draw_element(options: argparse.Namespace):
    """Entry point for element drawing."""
    tags_description: Tags = {
        x.split("=")[0]: x.split("=")[1] for x in options.tags.split(",")
    }
    if options.type == "area":
        draw_area(tags_description, Path(options.output_file))
    elif options.type == "node":
        draw_node(tags_description, Path(options.output_file))
