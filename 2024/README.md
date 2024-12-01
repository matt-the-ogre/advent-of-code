# Advent of Code 2024

> I'm starting the Advent of Code (Adventofcode.com) coding challenge for 2024. I want to write my code in Swift this year. And I want to use Visual Studio Code. What should I start with on Day 1? I'm going to organize my repo in a directory structure like this: "~/src/adventofcode/2024/01" for Day 1 of 2024. 
>
> What do I need to know about writing, debugging, and running Swift code in VS Code?

Great choice to use Swift for the Advent of Code! Here’s how you can get started with Swift in Visual Studio Code and your planned directory structure:

### 1. **Setting Up Swift in Visual Studio Code**
- **Install Swift Toolchain**: Download and install Swift from [Swift.org](https://swift.org/download/) for your platform.
- **Install VS Code Extensions**: Install the [CodeLLDB](https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb) extension for debugging and the [Swift Language Server](https://marketplace.visualstudio.com/items?itemName=sswg.swift-lang) extension for Swift language support.
- **Verify Swift Installation**: Open a terminal in VS Code and run:
  ```bash
  swift --version
  ```
  This ensures Swift is installed and accessible in your PATH.

### 2. **Day 1 Directory Structure**
For Day 1, navigate to your directory and set up a Swift project:
```bash
mkdir -p ~/src/adventofcode/2024/01
cd ~/src/adventofcode/2024/01
swift package init --type executable
```
This creates a Swift package with a basic executable structure.

### 3. **Writing Your Code**
- Open the `main.swift` file located in `Sources/01/main.swift`.
- Write your solution for Day 1 here.

### 4. **Running Your Code**
From the terminal in your project directory:
```bash
swift run
```

### 5. **Debugging in VS Code**
- Open the `01` directory in VS Code.
- Create a `launch.json` in the `.vscode` directory for debugging:
  ```json
  {
    "version": "0.2.0",
    "configurations": [
      {
        "name": "Debug",
        "type": "lldb",
        "request": "launch",
        "program": "${workspaceFolder}/.build/debug/01",
        "args": [],
        "cwd": "${workspaceFolder}"
      }
    ]
  }
  ```
- Set breakpoints and start debugging with the "Run and Debug" tab.

### 6. **Testing Your Code**
Add tests by editing the files in the `Tests` directory:
```bash
swift test
```

### 7. **Tips for Swift and Advent of Code**
- **Read the Input**: For quick input handling, consider reading from `stdin`:
  ```swift
  if let input = readLine() {
      print("Your input: \(input)")
  }
  ```
- **Use Playgrounds for Prototyping**: Xcode Playgrounds can be helpful for experimenting with Swift snippets before integrating them into your solution.
- **Leverage Swift Features**: Use Swift’s `Array`, `Dictionary`, and functional programming features (`map`, `filter`, `reduce`) to simplify your solutions.

For Day 1, focus on understanding the problem statement, setting up your environment, and writing a simple solution. You're good to go—happy coding!

> My launch.json in the .vscode director is already set up like this:
>
> ```json
> {
>     "configurations": [
>         {
>             "type": "lldb",
>             "request": "launch",
>             "args": [],
>             "cwd": "${workspaceFolder:advent-of-code}/2024/01",
>             "name": "Debug 01 (2024/01)",
>             "program": "${workspaceFolder:advent-of-code}/2024/01/.build/debug/01",
>             "preLaunchTask": "swift: Build Debug 01 (2024/01)"
>         },
>         {
>             "type": "lldb",
>             "request": "launch",
>             "args": [],
>             "cwd": "${workspaceFolder:advent-of-code}/2024/01",
>             "name": "Release 01 (2024/01)",
>             "program": "${workspaceFolder:advent-of-code}/2024/01/.build/release/01",
>             "preLaunchTask": "swift: Build Release 01 (2024/01)"
>         }
>     ]
> }
> ```
>
> How do I complete step 5?

Your `launch.json` is well-configured for debugging and running your Swift code in both Debug and Release modes. To complete **Step 5**, follow these steps in Visual Studio Code:

### 1. **Build Your Project**
Make sure your project is built before running or debugging:
- Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) and type `Run Task`.
- Select the task corresponding to your setup:
  - For Debug: `swift: Build Debug 01 (2024/01)`
  - For Release: `swift: Build Release 01 (2024/01)`

Alternatively, build manually in the terminal:
```bash
swift build   # Debug mode
swift build -c release   # Release mode
```

### 2. **Run the Debugger**
- Open the "Run and Debug" view in VS Code (`Ctrl+Shift+D` or `Cmd+Shift+D` on macOS).
- Choose a configuration from the dropdown:
  - **Debug 01 (2024/01)** for debugging.
  - **Release 01 (2024/01)** for optimized performance.
- Click the green play button (`▶`) or press `F5` to start.

### 3. **Debugging**
- Add breakpoints in your `main.swift` or any other source file by clicking in the gutter next to the line number.
- The debugger will stop execution at the breakpoints, allowing you to inspect variables and step through code.

### 4. **Run Without Debugging**
If you just want to run the program without debugging:
- Press `Ctrl+Shift+D` (or `Cmd+Shift+D`), select the configuration, and then choose `Run Without Debugging` (shortcut: `Ctrl+F5` or `Cmd+F5`).

### 5. **Review the Output**
Your program's output will appear in the Debug Console or Integrated Terminal, depending on the task.

With these steps, you're ready to run and debug your Day 1 solution seamlessly! Let me know if you encounter any issues.

