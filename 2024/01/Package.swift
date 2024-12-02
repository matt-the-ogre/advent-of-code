// swift-tools-version: 6.0
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "2024Day01",
    dependencies: [],
    targets: [
        .executableTarget(
            name: "2024Day01",
            dependencies: []),
        .testTarget(
            name: "2024Day01Tests",
            dependencies: ["2024Day01"]),
    ]
)