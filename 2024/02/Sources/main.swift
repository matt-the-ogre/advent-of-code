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

func convertInputToReportArray(input: String) -> [[Int]] {
    // Split the input into lines
    let lines = input.split(separator: "\n")
    
    // Convert each line into an array of integers
    let arrayOfArrays = lines.map { line in
        line.split(separator: " ").compactMap { Int($0) }
    }
    
    return arrayOfArrays
}

func isReportSafe(_ report: [Int]) -> Bool {
    let isMonotonic = checkIfIncreasingOrDecreasing(report)
    let hasValidDifference = checkMinimumAbsoluteDifference(report)
    return isMonotonic && hasValidDifference
}

func checkIfIncreasingOrDecreasing(_ report: [Int]) -> Bool {
    guard report.count > 1 else { return true }
    
    var isIncreasing = true
    var isDecreasing = true
    
    for i in 1..<report.count {
        if report[i] > report[i - 1] {
            isDecreasing = false
        } else if report[i] < report[i - 1] {
            isIncreasing = false
        }
    }
    
    return isIncreasing || isDecreasing
}

func checkMinimumAbsoluteDifference(_ report: [Int]) -> Bool {
    guard report.count > 1 else { return true }
    
    var minDifference = Int.max
    var maxDifference = Int.min
  
    for i in 1..<report.count {
        let difference = abs(report[i] - report[i - 1])
        if difference < minDifference {
            minDifference = difference
        }
        if difference > maxDifference {
            maxDifference = difference
        }
    }
    
    return minDifference >= 1 && maxDifference <= 3
}

func createSafeArray(from reportArray: [[Int]]) -> [Bool] {
    return reportArray.map { report in
        isReportSafe(report)
    }
}

func doubleCheckUnsafeReports(reportArray: [[Int]], safeArray: [Bool]) -> [Bool] {
    var updatedSafeArray = safeArray
    for (index, isSafe) in safeArray.enumerated() {
        if !isSafe {
            updatedSafeArray[index] = performAdditionalCheck(on: reportArray[index])
        }
    }
    return updatedSafeArray
}

func performAdditionalCheck(on report: [Int]) -> Bool {
    // New condition: Check if removing one element would make the report safe
    for i in 0..<report.count {
        var modifiedReport = report
        modifiedReport.remove(at: i)
        if isReportSafe(modifiedReport) {
            return true
        }
    }
    return false
}

// Get command line arguments
let arguments = CommandLine.arguments
let testMode = arguments.contains("test=true")

let input = readInputFile(testMode: testMode)
let reportArray: [[Int]] = convertInputToReportArray(input: input)
let safeArray = createSafeArray(from: reportArray)
let finalSafeArray = doubleCheckUnsafeReports(reportArray: reportArray, safeArray: safeArray)

print("Safe Array from part one:")
print(Array(safeArray[0..<min(10, safeArray.count)]))
print("Count of True values in Safe Array from part one:")
print(safeArray.filter { $0 }.count)

print("Final Safe Array after additional checks:")
print(Array(finalSafeArray[0..<min(10, finalSafeArray.count)]))
print("Count of True values in Final Safe Array:")
print(finalSafeArray.filter { $0 }.count)
