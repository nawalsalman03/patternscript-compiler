import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None
    
    def advance(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    
    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()
    
    def number(self):
        result = ''
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
    
    def identifier(self):
      result = ''
      while self.current_char and self.current_char.isalpha():
          result += self.current_char
          self.advance()
      
      # Only these are true keywords that change program structure
      keywords = ['if', 'print', 'generate', 'with', 'steps']
      if result in keywords:
          return Token(result.upper(), result)
      
      # fibonacci, arithmetic, geometric are treated as regular identifiers
      return Token('ID', result)
    
    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            if self.current_char.isdigit():
                return Token('NUMBER', self.number())
            
            if self.current_char.isalpha():
                return self.identifier()  # Fixed: directly return the token
            
            if self.current_char == '=':
                self.advance()
                return Token('ASSIGN', '=')
            
            if self.current_char == '+':
                self.advance()
                return Token('PLUS', '+')
            
            if self.current_char == '-':
                self.advance()
                return Token('MINUS', '-')
            
            if self.current_char == '*':
                self.advance()
                return Token('MULTIPLY', '*')
            
            if self.current_char == '/':
                self.advance()
                return Token('DIVIDE', '/')
            
            if self.current_char == '(':
                self.advance()
                return Token('LPAREN', '(')
            
            if self.current_char == ')':
                self.advance()
                return Token('RPAREN', ')')
            
            if self.current_char == '{':
                self.advance()
                return Token('LBRACE', '{')
            
            if self.current_char == '}':
                self.advance()
                return Token('RBRACE', '}')
            
            if self.current_char == '>':
                self.advance()
                return Token('GREATER', '>')
            
            if self.current_char == '[':
                self.advance()
                return Token('LBRACKET', '[')
            
            if self.current_char == ']':
                self.advance()
                return Token('RBRACKET', ']')
            
            self.advance()
        
        return Token('EOF', None)