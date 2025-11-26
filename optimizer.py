class Optimizer:
    def optimize(self, code):
        optimized = []
        for line in code:
            if '=' in line:
                parts = line.split('=')
                left = parts[0].strip()
                right = parts[1].strip()
                
                try:
                    if all(c in '0123456789+*-/ ' for c in right):
                        result = eval(right)
                        optimized.append(f"{left} = {result}")
                        continue
                except:
                    pass
            
            optimized.append(line)
        return optimized