import Foundation
import XCTest

enum ColumnError: Error {
    case invalidLineFormat
}

func readInputFile() -> String {
    let fileManager = FileManager.default

    // Construct the path to the input file
    let homeDirectory = fileManager.homeDirectoryForCurrentUser
    let inputFilePath = homeDirectory.appendingPathComponent("src/advent-of-code/2024/01/input.txt")

    do {
        // Read the file contents
        let fileContents = try String(contentsOf: inputFilePath, encoding: .utf8)
        return fileContents
    } catch {
        print("Error reading input file: \(error)")
        return ""
    }
}

func parseAndSortColumns(_ input: String) throws -> ([Int], [Int]) {
    var column1: [Int] = []
    var column2: [Int] = []

    let lines = input.split(separator: "\n")
    for line in lines {
        let numbers = line.split(separator: " ").compactMap { Int($0) }
        if numbers.count != 2 {
            throw ColumnError.invalidLineFormat
        }
        column1.append(numbers[0])
        column2.append(numbers[1])
    }

    column1.sort()
    column2.sort()

    return (column1, column2)
}

func calculateDistanceArray(column1: [Int], column2: [Int]) -> [Int] {
    return zip(column1, column2).map { abs($0 - $1) }
}

func calculateTotalDistance(_ distanceArray: [Int]) -> Int {
    return distanceArray.reduce(0, +)
}

func calculateSimilarityArray(column1: [Int], column2: [Int]) -> [Int] {
    return column1.map { value in
        value * column2.filter { $0 == value }.count
    }
}

// Example usage
do {
    let input = readInputFile()
    let (sortedColumn1, sortedColumn2) = try parseAndSortColumns(input)
    let distanceArray = calculateDistanceArray(column1: sortedColumn1, column2: sortedColumn2)
    let totalDistance = calculateTotalDistance(distanceArray)
    let similarityArray = calculateSimilarityArray(column1: sortedColumn1, column2: sortedColumn2)

    print("Sorted Column 1:")
    print(Array(sortedColumn1[0..<min(10, sortedColumn1.count)]))
    print("Sorted Column 2:")
    print(Array(sortedColumn2[0..<min(10, sortedColumn2.count)]))
    print("Distance Array:")
    print(Array(distanceArray[0..<min(10, distanceArray.count)]))
    print("Total Distance:")
    print(totalDistance)
    print("Similarity Array:")
    print(Array(similarityArray[0..<min(10, similarityArray.count)]))

    // Print the solution to part two
    let similarityTotal = similarityArray.reduce(0, +)
    print("Solution to part two:")
    print(similarityTotal)

} catch ColumnError.invalidLineFormat {
    print("Error: Input line does not contain exactly two integers. Exiting program.")
    exit(1)
} catch {
    print("An unexpected error occurred: \(error)")
    exit(1)
}

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
