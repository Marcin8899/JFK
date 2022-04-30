from LLVMGenerator import LLVMGenerator

from JFKProjektListener import JFKProjektListener
from JFKProjektParser import JFKProjektParser


class Variable:
    name = ''
    v_type = 'double'

    def __init__(self, name, v_type):
        self.name = name
        self.v_type = v_type


class Value:
    value = ''
    v_type = 'double'

    def __init__(self, value, v_type):
        self.value = value
        self.v_type = v_type


class LLVMActions(JFKProjektListener):

    generator = LLVMGenerator()
    variables = []  # Variable
    stack = []  # Value

    def exitProg(self, ctx: JFKProjektParser.ProgContext):
        print(self.generator.generate())
        pass

    def exitPrint(self, ctx: JFKProjektParser.PrintContext):
        self.stack.pop()
        var_name = ctx.value().getText()
        found_var = self.get_variable(var_name)
        if found_var is not None:
            self.generator.print(var_name, found_var.v_type, id=True)
        else:
            v = self.stack.pop()
            if v is not None:
                self.generator.print(var_name, v.v_type, id=False)
            else:
                RuntimeError("Unknown variable " + var_name)

    def exitAssign(self, ctx: JFKProjektParser.AssignContext):
        ID = ctx.ID().getText()
        v = self.stack.pop()

        if self.get_variable(ID) is None:
            self.variables.append(Variable(ID, v.v_type))
            self.generator.declare(ID, v.v_type)
            self.generator.assign(ID, v.value, v.v_type)
        else:
            self.generator.assign(ID, v.value, v.v_type)
    
    # TODO
    def exitRead(self, ctx: JFKProjektParser.ReadContext):
        var = self.__get_or_declare_variable_if_not_exists(ctx.ID().getText())
        self.generator.scanf(ctx.ID().getText(), var.v_type)
        var.value = f"%{ctx.ID().getText()}"  # Save the register addr instead last value

    def exitInt(self, ctx: JFKProjektParser.IntContext):
        self.stack.append(Value(ctx.INT().getText(), "i32"))

    def exitID(self, ctx:JFKProjektParser.IDContext):
        ID = ctx.ID().getText()
        var = self.get_variable(ID)
        self.generator.load(ID, var.v_type)
        self.stack.append(Value("%" + str(self.generator.reg - 1), var.v_type))

    def exitReal(self, ctx:JFKProjektParser.RealContext):
        self.stack.append(Value(ctx.REAL().getText(), "double"))

    def exitAdd(self, ctx: JFKProjektParser.AddContext):
        self.arithmetic_operation("add")

    def exitMinus(self, ctx: JFKProjektParser.MinusContext):
        self.arithmetic_operation("minus")

    def exitMultiply(self, ctx: JFKProjektParser.MultiplyContext):
        self.arithmetic_operation("multiply")

    def exitDivide(self, ctx: JFKProjektParser.DivideContext):
        self.arithmetic_operation("divide")

    def get_variable(self, var_name):
        for var in self.variables:
            if var.name == var_name:
                return var
        return None

    def arithmetic_operation(self, operation):
        value_2 = self.stack.pop()
        value_1 = self.stack.pop()

        if value_1.v_type != value_2.v_type:
            RuntimeError("Different types of variables cannot be added: " + value_1.name + " " + value_2.name)

        if value_1.v_type == "i32":
            if operation == "add":
                self.generator.add_i32(value_1.value, value_2.value)
            if operation == "minus":
                self.generator.minus_i32(value_1.value, value_2.value)
            if operation == "multiply":
                self.generator.multiply_i32(value_1.value, value_2.value)
            if operation == "divide":
                self.generator.divide_i32(value_1.value, value_2.value)
        else:
            if operation == "add":
                self.generator.add_double(value_1.value, value_2.value)
            if operation == "minus":
                self.generator.minus_double(value_1.value, value_2.value)
            if operation == "multiply":
                self.generator.multiply_double(value_1.value, value_2.value)
            if operation == "divide":
                self.generator.divide_double(value_1.value, value_2.value)

        self.stack.append(Value("%" + str(self.generator.reg - 1), value_1.v_type))
