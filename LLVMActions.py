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


class Tab:
    name = ''
    v_type = 'double'
    size = None

    def __init__(self, name, v_type, size):
        self.name = name
        self.v_type = v_type
        self.size = size


class LLVMActions(JFKProjektListener):
    generator = LLVMGenerator()
    variables = []  # Variable
    stack = []  # Value
    tabs = []  # Tab

    def exitProg(self, ctx: JFKProjektParser.ProgContext):
        print(self.generator.generate())
        pass

    def exitPrint(self, ctx: JFKProjektParser.PrintContext):
        var_name = ctx.value().getText()
        found_var = self.get_variable(var_name)
        if found_var is None:
            try:
                var_name = ctx.value().ID().getText()
                found_var = self.get_tab(var_name)
            except:
                pass

        if found_var is not None:
            self.stack.pop()
            self.generator.print(var_name, found_var.v_type, id=True)
        else:
            try:
                v = self.stack.pop()
            except:
                raise RuntimeError("Unknown variable " + var_name)

            self.generator.print(var_name, v.v_type, id=False)

    def exitAssign(self, ctx: JFKProjektParser.AssignContext):
        ID = ctx.ID().getText()
        v = self.stack.pop()

        if self.get_variable(ID) is None:
            self.variables.append(Variable(ID, v.v_type))
            self.generator.declare(ID, v.v_type)

        self.generator.assign(ID, v.value, v.v_type)

    def exitRead(self, ctx: JFKProjektParser.ReadContext):
        ID = ctx.ID().getText()

        if self.get_variable(ID) is None:
            self.variables.append(Variable(ID, "double"))
            self.generator.declare(ID, "double")

        self.generator.scanf(ctx.ID().getText(), self.get_variable(ID).v_type)

    def exitTab(self, ctx: JFKProjektParser.TabContext):
        ID = ctx.ID().getText()
        size = ctx.INT().getText()
        type = self.stack.pop()
        self.tabs.append(Tab(ID, type.v_type, size))
        self.generator.declare(ID, "[" + size + " x " + type.v_type + "]")

    def exitTabassign(self, ctx: JFKProjektParser.TabassignContext):
        ID = ctx.ID().getText()
        tab = self.get_tab(ID)
        if tab is None:
            raise RuntimeError("Tab " + ID + " does not exists")
        index = ctx.INT().getText()
        if int(index) < 0 or int(index) >= int(tab.size):
            raise RuntimeError("Invalid index " + index + " in " + ID)

        self.generator.array_ptr(ID, tab.v_type, tab.size, index)

        value = self.stack.pop()

        self.generator.assign(self.generator.reg - 1, value.value, value.v_type)

    def exitTabvalue(self, ctx: JFKProjektParser.TabvalueContext):
        ID = ctx.ID().getText()
        tab = self.get_tab(ID)
        if tab is None:
            raise RuntimeError("Tab " + ID + " does not exists")
        index = ctx.INT().getText()
        if int(index) < 0 or int(index) >= int(tab.size):
            raise RuntimeError("Invalid index " + index + " in " + ID)

        self.generator.array_ptr(ID, tab.v_type, tab.size, index)
        self.generator.load(str(self.generator.reg - 1), tab.v_type)
        self.stack.append(Value("%" + str(self.generator.reg - 1), tab.v_type))

    def exitInttype(self, ctx: JFKProjektParser.InttypeContext):
        self.stack.append(Value(None, "i32"))

    def exitRealtype(self, ctx: JFKProjektParser.RealtypeContext):
        self.stack.append(Value(None, "double"))

    def exitID(self, ctx: JFKProjektParser.IDContext):
        ID = ctx.ID().getText()
        var = self.get_variable(ID)
        if var is None:
            raise RuntimeError("Invalid variable " + ID)
        self.generator.load(ID, var.v_type)
        self.stack.append(Value("%" + str(self.generator.reg - 1), var.v_type))

    def exitInt(self, ctx: JFKProjektParser.IntContext):
        self.stack.append(Value(ctx.INT().getText(), "i32"))

    def exitReal(self, ctx: JFKProjektParser.RealContext):
        self.stack.append(Value(ctx.REAL().getText(), "double"))

    def exitAdd(self, ctx: JFKProjektParser.AddContext):
        self.arithmetic_operation("add")

    def exitMinus(self, ctx: JFKProjektParser.MinusContext):
        self.arithmetic_operation("minus")

    def exitMultiply(self, ctx: JFKProjektParser.MultiplyContext):
        self.arithmetic_operation("multiply")

    def exitDivide(self, ctx: JFKProjektParser.DivideContext):
        self.arithmetic_operation("divide")

    def exitToint(self, ctx:JFKProjektParser.TointContext):
        v = self.stack.pop()
        if (v.v_type == "double"):
            self.generator.fptosi(v.value)
        self.stack.append(Value("%" + str(self.generator.reg - 1), "i32"))

    def exitToreal(self, ctx:JFKProjektParser.TorealContext):
        v = self.stack.pop()
        if(v.v_type == "i32"):
            self.generator.sitofp(v.value)
        self.stack.append(Value("%" + str(self.generator.reg - 1), "double"))

    def get_variable(self, var_name):
        for var in self.variables:
            if var.name == var_name:
                return var
        return None

    def get_tab(self, tab_name):
        for tab in self.tabs:
            if tab.name == tab_name:
                return tab
        return None

    def arithmetic_operation(self, operation):
        value_2 = self.stack.pop()
        value_1 = self.stack.pop()

        if value_1.v_type != value_2.v_type:
            raise RuntimeError("Different types of variables cannot be added.")

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
