class LLVMGenerator:
    
    reg = 1
    if_reg = 1
    if_stack = []
    loop_reg = 1
    loop_stack = []
    header_text = ""
    text = ""
    main_text = ""
    function_text = ""
    main_reg = 1

    def print(self, value, var_type, id):
        if id:
            value = '%' + str(self.reg - 1)

        if var_type == "i32":
            self.text += "%" + str(self.reg) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 " + value + ")\n"
            self.reg += 1
        elif var_type == "double":
            self.text += "%" + str(self.reg) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double " + value + ")\n"
            self.reg += 1
        elif var_type == "string":
            self.text += "%" + str(self.reg) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i8* " + value + ")\n"
            self.reg += 1
        else:
            self.text += "%" + str(self.reg) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.char, i32 0, i32 0), i32 " + value + ")\n"
            self.reg += 1

    def scanf(self, var_id, var_type):
        if var_type == "i32":
            self.text += "%" + str(self.reg) + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* %" + var_id + ")\n"
        else:
            self.text += "%" + str(self.reg) + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strs, i32 0, i32 0), double* %" + var_id + ")\n"

        self.reg += 1

    def declare(self, var_id, var_type):
        self.text += f"%{var_id} = alloca {var_type}\n"

    def array_ptr(self, tab_id, tab_type, tab_size, tab_index):
        self.text += f"%{self.reg} = getelementptr inbounds [{tab_size} x {tab_type}], [{tab_size} x {tab_type}]* %{tab_id}, i64 0, i64 {tab_index}\n"
        self.reg += 1

    def assign(self, var_id, value, var_type):
        self.text += f"store {var_type} {value}, {var_type}* %{var_id}\n"

    def load(self, var_id, var_type):
        self.text += f"%{self.reg} = load {var_type}, {var_type}* %{var_id}\n"
        self.reg += 1

    def sext(self, var_id, var_type):
        self.text += f"%{self.reg} = sext {var_type} %{var_id} to i32\n"
        self.reg += 1

    def add_i32(self, val1, val2):
        self.text += f"%{self.reg} = add i32 {val1}, {val2}\n"
        self.reg += 1

    def add_double(self, val1, val2):
        self.text += f"%{self.reg} = fadd double {val1}, {val2}\n"
        self.reg += 1

    def minus_i32(self, val1, val2):
        self.text += f"%{self.reg} = sub i32 {val1}, {val2}\n"
        self.reg += 1

    def minus_double(self, val1, val2):
        self.text += f"%{self.reg} = fsub double {val1}, {val2}\n"
        self.reg += 1

    def multiply_i32(self, val1, val2):
        self.text += f"%{self.reg} = mul i32 {val1}, {val2}\n"
        self.reg += 1

    def multiply_double(self, val1, val2):
        self.text += f"%{self.reg} = fmul double {val1}, {val2}\n"
        self.reg += 1

    def divide_i32(self, val1, val2):
        self.text += f"%{self.reg} = sdiv i32 {val1}, {val2}\n"
        self.reg += 1

    def divide_double(self, val1, val2):
        self.text += f"%{self.reg} = fdiv double {val1}, {val2}\n"
        self.reg += 1

    def sitofp(self, id):
        self.text += f"%{self.reg} = sitofp i32 {id} to double\n"
        self.reg += 1

    def fptosi(self, id):
        self.text += f"%{self.reg} = fptosi double {id} to i32\n"
        self.reg += 1

    def enter_if(self):
        self.text += f"br i1 %{self.reg - 1}, label %if{self.if_reg}, label %if{self.if_reg+1}\n\n"
        self.text += f"if{self.if_reg}:\n"
        self.if_stack.append(self.if_reg + 1)
        self.if_reg += 2

    def exit_if(self):
        if_reg = self.if_stack.pop()
        self.text += f"br label %if{if_reg}\n\n"
        self.text += f"if{if_reg}:\n"

    def loop_declr(self):
        self.text += f"br label %loop{self.loop_reg}\n\n"
        self.text += f"loop{self.loop_reg}:\n"
        self.loop_stack.append(self.loop_reg)
        self.loop_reg += 1

    def enter_loop(self):
        self.text += f"br i1 %{self.reg - 1}, label %if{self.if_reg}, label %if{self.if_reg + 1}\n\n"
        self.text += f"if{self.if_reg}:\n"
        self.if_stack.append(self.if_reg + 1)
        self.if_reg += 2

    def exit_loop(self):
        if_reg = self.if_stack.pop()
        loop_reg = self.loop_stack.pop()
        self.text += f"br label %loop{loop_reg}\n\n"
        self.text += f"if{if_reg}:\n"

    def enter_function(self, name,):
        self.main_text += self.text
        self.main_reg = self.reg
        self.text = f"define i32 @{name}() nounwind {{\n"
        self.reg = 1

    def exit_function(self):
        self.text += f"ret i32 %{self.reg - 1}\n"
        self.text += "}\n\n"
        self.function_text += self.text
        self.text = "\n"
        self.reg = self.main_reg

    def call(self, name):
        self.text += f"%{self.reg} = call i32 @{name}()\n"
        self.reg += 1

    def sgt(self, val1, val2):
        self.text += f"%{self.reg} = icmp sgt i32 {val1}, {val2}\n"
        self.reg += 1

    def sge(self, val1, val2):
        self.text += f"%{self.reg} = icmp sge i32 {val1}, {val2}\n"
        self.reg += 1

    def generate(self):
        text = "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += "@strpi = constant [4 x i8] c\"%d\\0A\\00\"\n"
        text += "@strpd = constant [4 x i8] c\"%f\\0A\\00\"\n"
        text += "@strs = constant [3 x i8] c\"%d\\00\"\n"
        text += "@.str = constant [3 x i8] c\"%s\\00\"\n"
        text += "@.char = constant [3 x i8] c\"%c\\00\"\n"
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.main_text
        text += self.text
        text += "ret i32 0 }\n"
        text += self.function_text
        return text
