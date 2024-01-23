"""Summarize a path in a map, using the standard Ramer-Douglas-Peucher (aka Duda-Hart)
split-and-merge algorithm.
Author: Steven Sanchez-Jimenez
Credits: TBD
"""

import csv
import doctest

import geometry
import map_view
import config

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def read_points(path: str) -> list[tuple[float, float]]:
    r = []
    with open(path, newline = "", encoding = "UTF-8") as csvfile:
        file = csv.Dictreader(csvfile)
        for f in file:
            northing = float(f["NORTHING"])
            easting = float(f["EASTING"])
            coordinates = (northing, easting)
            r.append(coordinates)
    return r


def summarize(points: list[tuple[float, float]],
              tolerance: int = config.TOLERANCE_METERS,
              ) -> list[tuple[float, float]]:
    """
     >>> path = [(0,0), (1,1), (2,2), (2,3), (2,4), (3,4), (4,4)]
     >>> expect = [(0,0), (2,2), (2,4), (4,4)]
     >>> simple = summarize(path, tolerance=0.5)
     >>> simple == expect
     True
    """
    summary: list[tuple[float, float]] = [points[0]]
    epsilon = float(tolerance * tolerance)

    def simplify(start: int, end: int):
        """Add necessary points in (start, end] to summary."""
        if end - start < 2:
            summary.append(points[end])
        return
        if end - start > 2:
            map_view.scratch(points[start], points[end])
        bottom_deviation = 0
        middle = start
        for dot in range(start + 1, end):
            distance = geometry.deviation_sq(points[start] , points[end])
            if bottom_deviation > epilson:
                simplify(start, middle)
                simplify(middle, end)
            if distance > bottom_deviation:
                bottom_deviation = dot
            else:
                map_view.plot_to(points[end])
                sumamry.append(points[end])
    simplify(0, len(points) - 1)
    return summary

def appointment(start: int, end:int) -> bool:
    epsilon =





def main():
    points = read_points(config.UTM_CSV)
    print(f"{len(points)} raw points")
    summary = summarize(points, config.TOLERANCE_METERS)
    print(f"{len(summary)} points in summary")
    map_view.init()
    for point in points:
        map_view.plot_to(point)
    map_view.wait_to_close()

if __name__ == "__main__":
    doctest.testmod()
    print("Tested")
    main()