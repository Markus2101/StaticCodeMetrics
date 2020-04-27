import matplotlib.pyplot as plt
import numpy as np
import sys

# make utility scripts visible
sys.path.append('utils/')
import DataSeriesUtility as dsu


class DistanceIA:
    def __init__(self, dir_path):
        self._dir_path = dir_path
        self._instability_metric = None
        self._abstractness_metric = None
        self._distance = None

    def _calculate_distance(self):
        ''' calculates the distance between Abstractness and Instability of each file/component using
        D = |A+I-1|, with D being in range [0;1] with a
        ...D of 0 indicating that the corresponding file/component lies on the Main Sequence
        ...D of 1 indicating that the corresponding file/component lies far away from the Main Sequence '''
        self._distance = abs(self._abstractness_metric + self._instability_metric - 1)

    def plot_distance(self):
        ''' show a diagram picturing the distance in each components, where
        - y-axis denotes the distance
        - x-axis denotes the different files/components '''
        self._instability_metric, self._abstractness_metric = dsu.get_instability_and_abstractness_metric(self._dir_path)
        self._calculate_distance()

        ind = np.arange(self._distance.size)

        # x = files/components, y = distance
        plt.plot(ind, self._distance, marker='x', linestyle='None')
        plt.xticks(ind, self._instability_metric.index, rotation=45, ha='right')
        plt.ylabel('[D]istance', fontsize=18)

        plt.show()
