class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}
        self.patterns = {}
    
    def generate_fibonacci(self, n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        seq = [0, 1]
        for i in range(2, n):
            seq.append(seq[i-1] + seq[i-2])
        return seq
    
    def generate_arithmetic(self, n):
        return [i for i in range(n)]
    
    def generate_geometric(self, n):
        return [2**i for i in range(n)]
    
    def visit(self, node):
        if node[0] == 'pattern_generate':
            pattern_type = node[1]
            steps = node[2]
            if pattern_type == 'fibonacci':
                self.patterns['fibonacci'] = self.generate_fibonacci(steps)
            elif pattern_type == 'arithmetic':
                self.patterns['arithmetic'] = self.generate_arithmetic(steps)
            elif pattern_type == 'geometric':
                self.patterns['geometric'] = self.generate_geometric(steps)
            print(f"Generated {pattern_type} sequence with {steps} steps: {self.patterns[pattern_type]}")
            return None
        
        elif node[0] == 'array_access':
            array_name = node[1]
            index = self.visit(node[2])
            if array_name in self.patterns:
                if index < len(self.patterns[array_name]):
                    return self.patterns[array_name][index]
                else:
                    raise Exception(f"Index {index} out of bounds for {array_name}")
            else:
                raise Exception(f"Unknown pattern: {array_name}")
        
        elif node[0] == 'assign':
            var_name = node[1]
            value = self.visit(node[2])
            self.symbol_table[var_name] = value
            return value
        
        elif node[0] == 'binop':
            left = self.visit(node[2])
            right = self.visit(node[3])
            if node[1] == '+': return left + right
            elif node[1] == '-': return left - right
            elif node[1] == '*': return left * right
            elif node[1] == '/': return left // right  # integer division
        
        elif node[0] == 'number':
            return node[1]
        
        elif node[0] == 'var':
            if node[1] in self.symbol_table:
                return self.symbol_table[node[1]]
            else:
                raise Exception(f"Undefined variable: {node[1]}")
        
        elif node[0] == 'if':
            cond = self.visit(node[1])
            if cond:
                for stmt in node[2]:
                    self.visit(stmt)
        
        elif node[0] == 'print':
            value = self.visit(node[1])
            print(f"Output: {value}")
        
        elif node[0] == 'condition':
            left = self.visit(node[2])
            right = self.visit(node[3])
            if node[1] == '>': return left > right
    
    def analyze(self, ast):
        for node in ast:
            self.visit(node)
        return self.symbol_table