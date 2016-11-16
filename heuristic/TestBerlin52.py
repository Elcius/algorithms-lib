import unittest
import readtsplib
from Utilities import basinFunction
from ResultHelpers import TSPResult, BasinResult


class SearchTests(unittest.TestCase):

    def setUp(self):
        # berlin52 = self.TSPBEST
        # kroa150 = 26524
        # krob100 = 22141
        # pr107 = 44303
        # pr76 =108159
        self.Vector = [1, 2]
        TSP = []
        TSP.insert(0, readtsplib.readData('TSPLIB/berlin52.tsp'))
        TSP.insert(1, 7542)
        self.TSPDATA = TSP[0]
        self.TSPBEST = TSP[1]

    def tearDown(self):
        self.Vector = []

    def testVariableNeighborhoodSearch(self):
        from algorithms.VariableNeighborhoodSearch import search
        # Algorithm Configuration
        maxNoImprove = 50
        maxNoImproveLocal = 70
        neighborhoods = range(1, 21)  # since we want 20 runs for neighborhood starting with 1

        # Execute the algorithm
        result = search(self.TSPDATA, neighborhoods, maxNoImprove, maxNoImproveLocal)
        tspResult = TSPResult(self.TSPBEST, "Variable Neighborhood Search Results")
        print(tspResult.FormattedOutput(result))

    def testGreedyRandomizedAdaptiveSearch(self):
        from algorithms.GreedyRandomizedAdaptiveSearch import search
        # Algorithm Configuration
        maxNoImprove = 50
        maxIterations = 50
        greedinessFactor = 0.3  # should be in the range [0,1]. 0 is more greedy and 1 is more generalized

        # Execute the algorithm
        result = search(self.TSPDATA, maxIterations, maxNoImprove, greedinessFactor)
        tspResult = TSPResult(self.TSPBEST, "Greedy Randomized Adaptive Search Results")
        print(tspResult.FormattedOutput(result))

    def testTabuSearch(self):
        from algorithms.TabuSearch import search
        # Algorithm Configuration
        maxIterations = 100
        maxTabuCount = 15
        maxCandidates = 50
        # Execute the algorithm
        result = search(self.TSPDATA, maxIterations, maxTabuCount, maxCandidates)
        tspResult = TSPResult(self.TSPBEST, "Tabu Search Results")
        print(tspResult.FormattedOutput(result))

if __name__ == "__main__":
    unittest.main()
