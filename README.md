# PatternScript Compiler 
 
A complete compiler implementation for the **PatternScript** domain-specific language, designed for numerical pattern generation. Built as part of CS4031 - Compiler Construction course. 
 
## Features 
 
- **Custom Language**: PatternScript for generating Fibonacci, Arithmetic, and Geometric sequences 
- **Full Compiler Pipeline**: All 6 phases of compilation implemented 
- **Pattern Generation**: Create mathematical sequences with simple syntax 
- **Array Access**: Direct access to pattern elements using `pattern[index]` 
- **Mathematical Operations**: Support for +, -, *, / operations 
- **Optimization**: Basic constant folding and optimization 
 
## Usage 
 
```bash 
# Run with default example 
python main.py 
 
# Run with specific test file 
python main.py test1.txt 
python main.py test2.txt 
python main.py test3.txt 
``` 
 
## Test Cases 
 
**test1.txt** - Fibonacci sequence: 
```patternscript 
generate fibonacci with steps = 8 
value = fibonacci[7] 
print value 
# Output: 13 
``` 
 
**test2.txt** - Arithmetic sequence: 
```patternscript 
generate arithmetic with steps = 6 
result = arithmetic[5] * 2 
print result 
# Output: 10 
``` 
 
**test3.txt** - Mixed patterns: 
```patternscript 
generate fibonacci with steps = 10 
generate geometric with steps = 5 
answer = fibonacci[4] + geometric[3] 
print answer 
# Output: 11 
``` 
 
## Project Structure 
 
``` 
patternscript-compiler/ 
|-- lexer.py           # Lexical analysis 
|-- parser.py          # Syntax analysis 
|-- semantic.py        # Semantic analysis && execution 
|-- intermediate.py    # Intermediate code generation 
|-- optimizer.py       # Basic optimization 
|-- main.py           # Main compiler driver 
|-- test1.txt         # Fibonacci test case 
|-- test2.txt         # Arithmetic test case 
|-- test3.txt         # Mixed patterns test case 
|-- language_spec.txt # Language specification 
`-- README.md         # Project documentation 
``` 
 
## Team 
 
- Nawal Salman 22k-4236 
- Hafsa Atiqi 22k-4584 
- Raaiha Syed 22k-4460 
 
**Course**: CS4031 - Compiler Construction 
**Semester**: Fall 2025
