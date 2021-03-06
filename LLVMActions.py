from LLVMGenerator import LLVMGenerator

from JFKProjektListener import JFKProjektListener
from JFKProjektParser import JFKProjektParser


class Variable:
    name = ''
    v_type = 'double'
    v_range = 0
    v_global = False

    def __init__(self, name, v_type, v_range, v_global = False):
        self.name = name
        self.v_type = v_type
        self.v_range = v_range
        self.v_global = v_global

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
    global_variables = []
    stack = []  # Value
    tabs = []  # Tab
    actual_range = 0
    functions = []
    main_variables = None

    def exitProg(self, ctx: JFKProjektParser.ProgContext):
        print(self.generator.generate())
        pass

    def exitPrint(self, ctx: JFKProjektParser.PrintContext):
        var_name = ctx.value().getText()
        found_var = self.get_tab(var_name)
        if found_var is not None:
            if found_var.v_type == 'i8':
                self.generator.print(var_name, "string", id=True)
            else:
                raise RuntimeError("Unknown variable " + var_name)
        else:
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
        if v.v_type != 'i32' and v.v_type != 'double':
            if v.v_type == 'i8':
                tab = self.get_tab(ID)
                if tab is None:
                    raise RuntimeError("Unknown array " + ID)
                if len(self.stack)+1 > int(tab.size)-1:
                    raise RuntimeError("Too long string " + ID)

                self.generator.array_ptr(ID, v.v_type, tab.size, str(len(self.stack)))
                self.generator.assign(self.generator.reg - 1, v.value, v.v_type)

                while len(self.stack) != 0 and self.stack[len(self.stack)-1].v_type == 'i8':
                    v = self.stack.pop()
                    self.generator.array_ptr(ID, v.v_type, tab.size, str(len(self.stack)))
                    self.generator.assign(self.generator.reg - 1, v.value, v.v_type)
            else:
                raise RuntimeError("Incorrect value")
        else:
            if self.get_variable(ID) is None:
                self.variables.append(Variable(ID, v.v_type, self.actual_range))
                self.generator.declare(ID, v.v_type)

            self.generator.assign(ID, v.value, v.v_type)

    def exitGlobalassign(self, ctx:JFKProjektParser.GlobalassignContext):
        ID = ctx.ID().getText()
        v = self.stack.pop()
        if v.v_type != 'i32' and v.v_type != 'double':
            raise RuntimeError("Incorrect value")
        else:
            if self.get_variable(ID) is None:
                self.variables.append(Variable(ID, v.v_type, 0, True))
                self.global_variables.append(Variable(ID, v.v_type, 0, True))
                self.generator.declare(ID, v.v_type, True, v.value)
            else:
                raise RuntimeError("Incorrect variable name")

    def exitRead(self, ctx: JFKProjektParser.ReadContext):
        ID = ctx.ID().getText()

        if self.get_variable(ID) is None:
            self.variables.append(Variable(ID, "double", self.actual_range))
            self.generator.declare(ID, "double")

        self.generator.scanf(ctx.ID().getText(), self.get_variable(ID).v_type)

    def exitTab(self, ctx: JFKProjektParser.TabContext):
        ID = ctx.ID().getText()
        size = ctx.INT().getText()
        type = self.stack.pop()
        self.tabs.append(Tab(ID, type.v_type, str(int(size)+1)))
        self.generator.declare(ID, "[" + str(int(size)+1) + " x " + type.v_type + "]")

    def exitTabassign(self, ctx: JFKProjektParser.TabassignContext):
        ID = ctx.ID().getText()
        tab = self.get_tab(ID)
        if tab is None:
            raise RuntimeError("Tab " + ID + " does not exists")
        index = ctx.INT().getText()
        if int(index) < 0 or int(index) >= int(tab.size) - 1:
            raise RuntimeError("Invalid index " + index + " in " + ID)

        self.generator.array_ptr(ID, tab.v_type, tab.size, index)

        value = self.stack.pop()
        if value.v_type != tab.v_type:
            raise RuntimeError("Incorrect value")

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
        if tab.v_type == "i8":
            self.generator.sext(str(self.generator.reg - 1), tab.v_type)
        self.stack.append(Value("%" + str(self.generator.reg - 1), tab.v_type))

    def exitInttype(self, ctx: JFKProjektParser.InttypeContext):
        self.stack.append(Value(None, "i32"))

    def exitRealtype(self, ctx: JFKProjektParser.RealtypeContext):
        self.stack.append(Value(None, "double"))

    def exitChartype(self, ctx:JFKProjektParser.ChartypeContext):
        self.stack.append(Value(None, "i8"))

    def exitID(self, ctx: JFKProjektParser.IDContext):
        ID = ctx.ID().getText()
        var = self.get_variable(ID)
        if var is None:
            var = self.get_tab(ID)
            if var is None:
                raise RuntimeError("Invalid variable " + ID)
            self.generator.array_ptr(ID, var.v_type, var.size, 0)
        else:
            self.generator.load(ID, var.v_type, var.v_global)
            self.stack.append(Value("%" + str(self.generator.reg - 1), var.v_type))

    def exitInt(self, ctx: JFKProjektParser.IntContext):
        self.stack.append(Value(ctx.INT().getText(), "i32"))

    def exitReal(self, ctx: JFKProjektParser.RealContext):
        self.stack.append(Value(ctx.REAL().getText(), "double"))

    def exitChar(self, ctx: JFKProjektParser.CharContext):
        self.stack.append(Value(ord(ctx.CHAR().getText()[1]), "i8"))

    def exitString(self, ctx: JFKProjektParser.StringContext):
        for i in range(len(ctx.STRING().getText())-2):
            self.stack.append(Value(ord(ctx.STRING().getText()[i+1]), "i8"))

    def exitAdd(self, ctx: JFKProjektParser.AddContext):
        self.arithmetic_operation("add")

    def exitMinus(self, ctx: JFKProjektParser.MinusContext):
        self.arithmetic_operation("minus")

    def exitMultiply(self, ctx: JFKProjektParser.MultiplyContext):
        self.arithmetic_operation("multiply")

    def exitDivide(self, ctx: JFKProjektParser.DivideContext):
        self.arithmetic_operation("divide")

    def exitToint(self, ctx: JFKProjektParser.TointContext):
        v = self.stack.pop()
        if (v.v_type == "double"):
            self.generator.fptosi(v.value)
        self.stack.append(Value("%" + str(self.generator.reg - 1), "i32"))

    def exitToreal(self, ctx: JFKProjektParser.TorealContext):
        v = self.stack.pop()
        if(v.v_type == "i32"):
            self.generator.sitofp(v.value)
        self.stack.append(Value("%" + str(self.generator.reg - 1), "double"))

    def enterBlockif(self, ctx:JFKProjektParser.BlockifContext):
        self.generator.enter_if()
        self.actual_range += 1

    def exitBlockif(self, ctx:JFKProjektParser.BlockifContext):
        self.generator.exit_if()
        self.actual_range -= 1
        self.delete_variables()

    def enterWhile_declr(self, ctx:JFKProjektParser.While_declrContext):
        self.generator.loop_declr()

    def enterBlockwhile(self, ctx:JFKProjektParser.BlockwhileContext):
        self.generator.enter_loop()
        self.actual_range += 1

    def exitBlockwhile(self, ctx:JFKProjektParser.BlockwhileContext):
        self.generator.exit_loop()
        self.actual_range -= 1
        self.delete_variables()

    def enterFunction_declaration(self, ctx:JFKProjektParser.Function_declarationContext):
        self.main_variables = self.variables
        self.variables = self.global_variables
        ID = ctx.ID().getText()
        for f in self.functions:
            if f == ID:
                raise RuntimeError("Incorrect function name")
        self.functions.append(ID)

        self.generator.enter_function(ID)

    def exitFunction_declaration(self, ctx:JFKProjektParser.Function_declarationContext):
        self.generator.exit_function()
        self.variables = self.main_variables

    def exitFcall(self, ctx:JFKProjektParser.FcallContext):
        ID = ctx.ID().getText()
        ok = False
        for f in self.functions:
            if f == ID:
                self.generator.call(ID)
                ok = True
                self.stack.append(Value("%"+str(self.generator.reg-1), 'i32'))
        if not ok:
            raise RuntimeError("Incorrect function name")

    def exitGreater(self, ctx:JFKProjektParser.GreaterContext):
        value_2 = self.stack.pop()
        value_1 = self.stack.pop()

        self.generator.sgt(value_1.value, value_2.value)

    def exitLess(self, ctx:JFKProjektParser.LessContext):
        value_2 = self.stack.pop()
        value_1 = self.stack.pop()

        self.generator.sgt(value_2.value, value_1.value)

    def exitGreater_equal(self, ctx: JFKProjektParser.Greater_equalContext):
        value_2 = self.stack.pop()
        value_1 = self.stack.pop()

        self.generator.sge(value_1.value, value_2.value)

    def exitLess_equal(self, ctx:JFKProjektParser.Less_equalContext):
        value_2 = self.stack.pop()
        value_1 = self.stack.pop()

        self.generator.sge(value_2.value, value_1.value)

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

    def delete_variables(self):
        for var in self.variables:
            if var.v_range > self.actual_range:
                self.variables.remove(var)
