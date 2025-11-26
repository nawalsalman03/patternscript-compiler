from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer
from intermediate import IntermediateCodeGenerator
from optimizer import Optimizer
import sys

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            text = f.read()
    else:
        # Default PatternScript program
        text = """
        generate fibonacci with steps = 10
        generate arithmetic with steps = 5
        result = fibonacci[5] + arithmetic[3]
        print result
        """
    
    print("=== PATTERNSCRIPT COMPILER ===")
    print("=== SOURCE CODE ===")
    print(text.strip())
    
    # Phase 1: Lexical Analysis
    print("\n=== 1. LEXICAL ANALYSIS ===")
    lexer = Lexer(text)
    token = lexer.get_next_token()
    token_count = 0
    while token.type != 'EOF' and token_count < 20:  # Limit output
        print(f"Token: {token.type:12} Value: {token.value}")
        token = lexer.get_next_token()
        token_count += 1
    
    # Phase 2: Syntax Analysis
    print("\n=== 2. SYNTAX ANALYSIS ===")
    lexer = Lexer(text)
    parser = Parser(lexer)
    ast = parser.parse()
    print("Abstract Syntax Tree:")
    for i, node in enumerate(ast):
        print(f"  {i+1}: {node}")
    
    # Phase 3: Semantic Analysis
    print("\n=== 3. SEMANTIC ANALYSIS ===")
    semantic = SemanticAnalyzer()
    symbol_table = semantic.analyze(ast)
    print("Final Symbol Table:", symbol_table)
    print("Generated Patterns:", semantic.patterns)
    
    # Phase 4: Intermediate Code
    print("\n=== 4. INTERMEDIATE CODE ===")
    icg = IntermediateCodeGenerator()
    for node in ast:
        icg.generate(node)
    intermediate_code = icg.get_code()
    for i, line in enumerate(intermediate_code):
        print(f"{i+1}: {line}")
    
    # Phase 5: Optimization
    print("\n=== 5. OPTIMIZATION ===")
    optimizer = Optimizer()
    optimized_code = optimizer.optimize(intermediate_code)
    for i, line in enumerate(optimized_code):
        print(f"{i+1}: {line}")
    
    # Phase 6: Execution Results
    print("\n=== 6. EXECUTION RESULTS ===")
    semantic = SemanticAnalyzer()
    semantic.analyze(ast)

if __name__ == '__main__':
    main()