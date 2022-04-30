class LLVMGenerator:
    
    reg = 1
    header_text = ""
    main_text = ""

    def print(self, value, var_type, id):
        if var_type == "i32":
            if not id:
                self.main_text += "%" + str(self.reg) + " = load i32, i32* " + value + "\n"
                self.reg += 1
            self.main_text += "%" + str(self.reg) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %" + str(self.reg - 1) + ")\n"
            self.reg += 1
        else:
            if not id:
                self.main_text += "%" + str(self.reg) + " = load double, double* " + value + "\n"
                self.reg += 1
            self.main_text += "%" + str(self.reg) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %" + str(self.reg - 1) + ")\n"
            self.reg += 1

    def scanf(self, var_id, var_type):
        pass

    def declare(self, var_id, var_type):
        self.main_text += f"%{var_id} = alloca {var_type}\n"

    def assign(self, var_id, value, var_type):
        self.main_text += f"store {var_type} {value}, {var_type}* %{var_id}\n"

    def load(self, var_id, var_type):
        self.main_text += f"%{self.reg} = load {var_type}, {var_type}* %{var_id}\n"
        self.reg += 1

    def add_i32(self, val1, val2):
        self.main_text += f"%{self.reg} = add i32 {val1}, {val2}\n"
        self.reg += 1

    def add_double(self, val1, val2):
        self.main_text += f"%{self.reg} = fadd double {val1}, {val2}\n"
        self.reg += 1

    def minus_i32(self, val1, val2):
        self.main_text += f"%{self.reg} = sub i32 {val1}, {val2}\n"
        self.reg += 1

    def minus_double(self, val1, val2):
        self.main_text += f"%{self.reg} = fsub double {val1}, {val2}\n"
        self.reg += 1

    def multiply_i32(self, val1, val2):
        self.main_text += f"%{self.reg} = mul i32 {val1}, {val2}\n"
        self.reg += 1

    def multiply_double(self, val1, val2):
        self.main_text += f"%{self.reg} = fmul double {val1}, {val2}\n"
        self.reg += 1

    def divide_i32(self, val1, val2):
        self.main_text += f"%{self.reg} = sdiv i32 {val1}, {val2}\n"
        self.reg += 1

    def divide_double(self, val1, val2):
        self.main_text += f"%{self.reg} = fdiv double {val1}, {val2}\n"
        self.reg += 1

    def generate(self):
        text = "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += "@strpi = constant [4 x i8] c\"%d\\0A\\00\"\n"
        text += "@strpd = constant [4 x i8] c\"%f\\0A\\00\"\n"
        text += "@strs = constant [3 x i8] c\"%d\\00\"\n"
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.main_text
        text += "ret i32 0 }\n"
        return text