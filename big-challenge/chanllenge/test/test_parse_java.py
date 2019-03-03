import javalang
import plyj.parser as plyj

parser = plyj.Parser()

tree = parser.parse_string('class Foo { }')

# CompilationUnit(package_declaration=None, import_declarations=[],
# type_declarations=[ClassDeclaration(name='Foo', body=[], modifiers=[],
# type_parameters=[], extends=None, implements=[])])

print(tree)

tree = javalang.parse.parse('class Foo { }')

# CompilationUnit
print(tree)
