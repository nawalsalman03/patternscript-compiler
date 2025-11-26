class IntermediateCodeGenerator:
    def __init__(self):
        self.temp_count = 0
        self.code = []
    
    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"
    
    def generate(self, node):
        if node[0] == 'pattern_generate':
            pattern_type = node[1]
            steps = node[2]
            self.code.append(f"GENERATE {pattern_type} WITH STEPS = {steps}")
            return f"{pattern_type}_seq"
        
        elif node[0] == 'array_access':
            array_name = node[1]
            index_temp = self.generate(node[2])
            temp = self.new_temp()
            self.code.append(f"{temp} = {array_name}[{index_temp}]")
            return temp
        
        elif node[0] == 'assign':
            result = self.generate(node[2])
            self.code.append(f"{node[1]} = {result}")
            return node[1]
        
        elif node[0] == 'binop':
            left = self.generate(node[2])
            right = self.generate(node[3])
            temp = self.new_temp()
            self.code.append(f"{temp} = {left} {node[1]} {right}")
            return temp
        
        elif node[0] == 'number':
            return str(node[1])
        
        elif node[0] == 'var':
            return node[1]
        
        elif node[0] == 'if':
            cond_temp = self.generate(node[1])
            label = self.new_temp().replace('t', 'L')
            self.code.append(f"IF NOT {cond_temp} GOTO {label}")
            for stmt in node[2]:
                self.generate(stmt)
            self.code.append(f"LABEL {label}")
        
        elif node[0] == 'print':
            value = self.generate(node[1])
            self.code.append(f"PRINT {value}")
        
        elif node[0] == 'condition':
            left = self.generate(node[2])
            right = self.generate(node[3])
            temp = self.new_temp()
            self.code.append(f"{temp} = {left} {node[1]} {right}")
            return temp
    
    def get_code(self):
        return self.code