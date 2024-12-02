import Foundation

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

