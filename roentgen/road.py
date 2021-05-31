"""
Road shape drawing.
"""
from typing import List

import numpy as np

from flinger import Flinger, angle
from osm_reader import OSMNode


class RoadPart:
    """
    Line part of the road.
    """
    def __init__(self, point_1: np.array, point_2: np.array):
        self.point_1 = point_1
        self.point_2 = point_2

    @classmethod
    def from_nodes(
        cls, node_1: OSMNode, node_2: OSMNode, flinger: Flinger
    ) -> "RoadPart":
        """
        Construct road part from OSM nodes.
        """
        return cls(
            flinger.fling(node_1.coordinates),
            flinger.fling(node_2.coordinates)
        )

    def get_angle(self) -> float:
        """
        Get an angle between line and x axis.
        """
        return angle(self.point_1, self.point_2)


class Intersection:
    """
    An intersection of the roads, that is described by its parts.  All first
    points of the road parts should be the same.
    """
    def __init__(self, parts: List[RoadPart]):
        self.parts: List[RoadPart] = sorted(parts, key=lambda x: x.get_angle())