import Foundation
import XCTest

// Unit Tests
class AdventOfCodeTests: XCTestCase {
    func testCalculateTotalDistance() {
        let column1 = [10, 20, 30]
        let column2 = [40, 50, 60]
        let distanceArray = calculateDistanceArray(column1: column1, column2: column2)
        let totalDistance = calculateTotalDistance(distanceArray)
        XCTAssertEqual(totalDistance, 90, "Total distance should be 90")
    }

    func testCalculateSimilarityArray() {
        let column1 = [10, 20, 30, 10]
        let column2 = [10, 20, 30, 40]
        let similarityArray = calculateSimilarityArray(column1: column1, column2: column2)
        XCTAssertEqual(similarityArray, [20, 20, 30, 20], "Similarity array should be [20, 20, 30, 20]")
    }

    func testParseAndSortColumns() throws {
        let input = "10 20\n30 40\n50 60"
        let (column1, column2) = try parseAndSortColumns(input)
        XCTAssertEqual(column1, [10, 30, 50], "Column 1 should be sorted as [10, 30, 50]")
        XCTAssertEqual(column2, [20, 40, 60], "Column 2 should be sorted as [20, 40, 60]")
    }

    func testInvalidLineFormat() {
        let input = "10 20\n30"
        XCTAssertThrowsError(try parseAndSortColumns(input)) { error in
            XCTAssertEqual(error as? ColumnError, ColumnError.invalidLineFormat, "Should throw invalidLineFormat error")
        }
    }

    func testGivenInputValues() {
        let input = readInputFile()
        do {
            let (sortedColumn1, sortedColumn2) = try parseAndSortColumns(input)
            let distanceArray = calculateDistanceArray(column1: sortedColumn1, column2: sortedColumn2)
            let totalDistance = calculateTotalDistance(distanceArray)
            let similarityArray = calculateSimilarityArray(column1: sortedColumn1, column2: sortedColumn2)
            let similarityTotal = similarityArray.reduce(0, +)

            XCTAssertEqual(totalDistance, 2264607, "Total distance should be 2264607")
            XCTAssertEqual(similarityTotal, 19457120, "Similarity total should be 19457120")
        } catch {
            XCTFail("Unexpected error: \(error)")
        }
    }
}

// Run Tests
AdventOfCodeTests.defaultTestSuite.run()
