import string

class TokenType:
    ASSIGN = 'assign'
    PLUS = 'plus'
    MINUS = 'minus'
    TIMES = 'times'
    DIV = 'div'
    LPAREN = 'lparen'
    RPAREN = 'rparen'
    ID = 'id'
    NUMBER = 'number'
    COMMENT = 'comment'
    EOF = 'eof'

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

def tokenize(input_str):
    tokens = []
    i = 0
    while i < len(input_str):
        if input_str[i] in string.ascii_letters:
            j = i + 1
            while j < len(input_str) and (input_str[j] in string.ascii_letters or input_str[j].isdigit()):
                j += 1
            tokens.append(Token(TokenType.ID, input_str[i:j]))
            i = j
        elif input_str[i].isdigit() or (input_str[i] == '.' and i + 1 < len(input_str) and input_str[i + 1].isdigit()):
            j = i
            while j < len(input_str) and (input_str[j].isdigit() or input_str[j] == '.'):
                j += 1
            tokens.append(Token(TokenType.NUMBER, input_str[i:j]))
            i = j
        elif input_str[i:i+2] == ':=':
            tokens.append(Token(TokenType.ASSIGN, ':='))
            i += 2
        elif input_str[i] == '+':
            tokens.append(Token(TokenType.PLUS, '+'))
            i += 1
        elif input_str[i] == '-':
            tokens.append(Token(TokenType.MINUS, '-')) 
            i += 1
        elif input_str[i] == '*':
            tokens.append(Token(TokenType.TIMES, '*'))
            i += 1
        elif input_str[i] == '/':
            tokens.append(Token(TokenType.DIV, '/'))
            i += 1
        elif input_str[i] == '(':
            tokens.append(Token(TokenType.LPAREN, '('))
            i += 1
        elif input_str[i] == ')':
            tokens.append(Token(TokenType.RPAREN, ')'))
            i += 1
        elif input_str[i:i+2] == '/*':
            j = i + 2
            while j < len(input_str) and input_str[j:j+2] != '*/':
                j += 1
            if j < len(input_str):
                j += 2
            tokens.append(Token(TokenType.COMMENT, input_str[i:j]))
            i = j
        elif input_str[i:i+2] == '//':
            j = i + 2
            while j < len(input_str) and input_str[j] != '\n':
                j += 1
            tokens.append(Token(TokenType.COMMENT, input_str[i:j]))
            i = j
        elif input_str[i] in string.whitespace:
            i += 1
        # else:
        #     raise ValueError('Invalid character at position ' + str(i))
    
    tokens.append(Token(TokenType.EOF, None))
    return tokens

def print_tokens(tokens):
    for token in tokens:
        if token.type != TokenType.EOF:
            print(f'{token.type}: {token.value}')

# Example usage
# example_input = "Celcius := 100.0\nFahrenheit := (9/5)*Celcius + 32"

with open('CompiTech\input.txt', 'r') as file:
    example_input = file.read()
tokens = tokenize(example_input)

print_tokens(tokens)
