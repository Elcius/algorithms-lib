import unittest, math
import tsplib_parser
from result import TSPResult

MAX = 1000

class SearchTests(unittest.TestCase):

    def setUp(self):
        self.Vector = [1, 2]
        self.TSP = []
        self.TSP.insert(0, [7542, tsplib_parser.readData('TSPLIB/berlin52.tsp'), 'Berlin52'])
        self.TSP.insert(1, [26524, tsplib_parser.readData('TSPLIB/kroa150.tsp'), 'Kroa150'])
        self.TSP.insert(2, [22141, tsplib_parser.readData('TSPLIB/krob100.tsp'), 'Krob100'])
        self.TSP.insert(3, [44303, tsplib_parser.readData('TSPLIB/pr107.tsp'), 'Pr107'])
        self.TSP.insert(4, [108159, tsplib_parser.readData('TSPLIB/pr76.tsp'), 'Pr76'])

    def tearDown(self):
        self.Vector = []

    def testVariableNeighborhoodSearch(self):
        test_sum = 0
        from algorithms.vns import search
        # Algorithm Configuration
        maxNoImprove = MAX # 50
        maxNoImproveLocal = 70 # 70
        neighborhoods = range(1, 20)  # since we want 20 runs for neighborhood starting with 1

        # Execute the algorithm
        result_list = []
        rpd_list = []
        for x in range(len(self.TSP)):
            for y in range(1, 11):
                result = search(self.TSP[x][1], neighborhoods, maxNoImprove, maxNoImproveLocal)
                result_list.insert(0, result["cost"])
                tspResult = TSPResult(self.TSP[x][0], "VNS Results", self.TSP[x][2], y)
                rpd_list.insert(0, tspResult.getRPD(result))
                print(tspResult.FormattedOutput(result))

            print('-' * 30)
            print("Media dos resultados:", int(sum(result_list) / len(result_list)))
            print("Media do RPD:", sum(rpd_list) / len(rpd_list))

    def testGreedyRandomizedAdaptiveSearch(self):
        from algorithms.grasp import search
        # Algorithm Configuration
        maxNoImprove = 500 # 50
        maxIterations = MAX # 50
        greedinessFactor = 0.2  # should be in the range [0,1]. 0 is more greedy and 1 is more generalized

        # Execute the algorithm
        result_list = []
        rpd_list = []
        for x in range(len(self.TSP)):
            for y in range(1, 11):
                result = search(self.TSP[x][1], maxIterations, maxNoImprove, greedinessFactor)
                result_list.insert(0, result["cost"])
                tspResult = TSPResult(self.TSP[x][0], "GRASP Results", self.TSP[x][2], y)
                rpd_list.insert(0, tspResult.getRPD(result))
                print(tspResult.FormattedOutput(result))

            print('-' * 30)
            print("Media do Tour Cost:", int(sum(result_list) / len(result_list)))
            print("Media do RPD:", sum(rpd_list) / len(rpd_list))

    def testTabuSearch(self):
        from algorithms.tabu_search import search
        # Algorithm Configuration
        maxIterations = MAX # 50
        maxTabuCount = 15
        maxCandidates = 50

        # Execute the algorithm
        result_list = []
        rpd_list = []
        for x in range(len(self.TSP)):
            for y in range(1, 11):
                result = search(self.TSP[x][1], maxIterations, maxTabuCount, maxCandidates)
                result_list.insert(0, result["cost"])
                tspResult = TSPResult(self.TSP[x][0], "Tabu Search Results", self.TSP[x][2], y)
                rpd_list.insert(0, tspResult.getRPD(result))

                print(tspResult.FormattedOutput(result))
            print('-' * 30)
            print("Media dos resultados:", int(sum(result_list) / len(result_list)))
            print("Media do RPD:", sum(rpd_list) / len(rpd_list))

if __name__ == "__main__":
    unittest.main()
