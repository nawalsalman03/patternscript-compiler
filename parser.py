class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f"Syntax error: expected {token_type}, got {self.current_token.type}")
    
    def factor(self):
        token = self.current_token
        
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return ('number', token.value)
        
        elif token.type == 'ID':
            var_name = token.value
            self.eat('ID')
            
            # Check for array access like fibonacci[5]
            if self.current_token.type == 'LBRACKET':
                self.eat('LBRACKET')
                index = self.expression()
                self.eat('RBRACKET')
                return ('array_access', var_name, index)
            else:
                return ('var', var_name)
        
        elif token.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.expression()
            self.eat('RPAREN')
            return node
        
        else:
            raise Exception(f"Unexpected token in factor: {token.type}")
    
    def term(self):
        node = self.factor()
        
        while self.current_token.type in ('MULTIPLY', 'DIVIDE'):
            token = self.current_token
            if token.type == 'MULTIPLY':
                self.eat('MULTIPLY')
            elif token.type == 'DIVIDE':
                self.eat('DIVIDE')
            
            node = ('binop', token.value, node, self.factor())
        
        return node
    
    def expression(self):
        node = self.term()
        
        while self.current_token.type in ('PLUS', 'MINUS'):
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
            elif token.type == 'MINUS':
                self.eat('MINUS')
            
            node = ('binop', token.value, node, self.term())
        
        return node
    
    def condition(self):
        left = self.expression()
        self.eat('GREATER')
        right = self.expression()
        return ('condition', '>', left, right)
    
    def pattern_generation(self):
      self.eat('GENERATE')
      # Pattern type should be treated as ID, not keyword
      pattern_type = self.current_token.value
      self.eat('ID')  # Changed from pattern_type.upper() to 'ID'
      self.eat('WITH')
      self.eat('STEPS')
      self.eat('ASSIGN')
      steps = self.current_token.value
      self.eat('NUMBER')
      return ('pattern_generate', pattern_type, steps)
      
    def statement(self):
        if self.current_token.type == 'GENERATE':
            return self.pattern_generation()
        
        elif self.current_token.type == 'ID':
            var_name = self.current_token.value
            self.eat('ID')
            self.eat('ASSIGN')
            expr = self.expression()
            return ('assign', var_name, expr)
        
        elif self.current_token.type == 'IF':
            self.eat('IF')
            self.eat('LPAREN')
            cond = self.condition()
            self.eat('RPAREN')
            self.eat('LBRACE')
            body = self.statement_list()
            self.eat('RBRACE')
            return ('if', cond, body)
        
        elif self.current_token.type == 'PRINT':
            self.eat('PRINT')
            expr = self.expression()
            return ('print', expr)
        
        else:
            raise Exception(f"Unexpected token in statement: {self.current_token.type}")
    
    def statement_list(self):
        statements = []
        while self.current_token.type != 'EOF' and self.current_token.type != 'RBRACE':
            statements.append(self.statement())
        return statements
    
    def parse(self):
        return self.statement_list()