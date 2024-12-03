import Foundation

enum ColumnError: Error {
    case invalidLineFormat
}

func readInputFile(testMode: Bool) -> String {
    let fileManager = FileManager.default

    // Determine the input file based on the test parameter
    let filename = testMode ? "test.txt" : "input.txt"
    let homeDirectory = fileManager.homeDirectoryForCurrentUser
    let inputFilePath = homeDirectory.appendingPathComponent("src/advent-of-code/2024/02/\(filename)")

    do {
        // Read the file contents
        let fileContents = try String(contentsOf: inputFilePath, encoding: .utf8)
        return fileContents
    } catch {
        print("Error reading input file: \(error)")
        return ""
    }
}

func convertInputToArrayOfArrays(input: String) -> [[Int]] {
    // Split the input into lines
    let lines = input.split(separator: "\n")
    
    // Convert each line into an array of integers
    let arrayOfArrays = lines.map { line in
        line.split(separator: " ").compactMap { Int($0) }
    }
    
    return arrayOfArrays
}

func checkIfIncreasingOrDecreasing(_ level: [Int]) -> Bool {
    guard level.count > 1 else { return true }
    
    var isIncreasing = true
    var isDecreasing = true
    
    for i in 1..<level.count {
        if level[i] > level[i - 1] {
            isDecreasing = false
        } else if level[i] < level[i - 1] {
            isIncreasing = false
        }
    }
    
    return isIncreasing || isDecreasing
}

func checkMinimumAbsoluteDifference(_ level: [Int]) -> Bool {
    guard level.count > 1 else { return true }
    
    var minDifference = Int.max
    var maxDifference = Int.min
  
    for i in 1..<level.count {
        let difference = abs(level[i] - level[i - 1])
        if difference < minDifference {
            minDifference = difference
        }
        if difference > maxDifference {
            maxDifference = difference
        }
    }
    
    return minDifference >= 1 && maxDifference <= 3
}

func createSafeArray(from inputArray: [[Int]]) -> [Bool] {
    return inputArray.map { level in
        let isMonotonic = checkIfIncreasingOrDecreasing(level)
        let hasValidDifference = checkMinimumAbsoluteDifference(level)
        return isMonotonic && hasValidDifference
    }
}

// Get command line arguments
let arguments = CommandLine.arguments
let testMode = arguments.contains("test=true")

let input = readInputFile(testMode: testMode)
let inputArray: [[Int]] = convertInputToArrayOfArrays(input: input)
let safeArray = createSafeArray(from: inputArray)

print("Safe Array:")
print(Array(safeArray[0..<min(10, safeArray.count)]))
print("Count of True values in Safe Array:")
print(safeArray.filter { $0 }.count)
