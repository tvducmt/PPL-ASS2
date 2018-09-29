import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    ############### test var declar
    def test_var_simple(self):
        """test var simple: int main() {} """
        input = """var x, y: string;"""
        expect = str(Program([VarDecl(Id('x'),StringType()),VarDecl(Id('y'),StringType())]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_var_complex(self):
        """test var complex"""
        input = """var x, y: string;
                        a, b: integer;"""
        expect = str(Program([VarDecl(Id('x'),StringType()),VarDecl(Id('y'),StringType()), VarDecl(Id(str('a')),IntType()),VarDecl(Id(str('b')),IntType())]))
        self.assertTrue(TestAST.test(input,expect,302))
    
    def test_var_arr_simple(self):
        """test_var_arr_simple"""
        input = """var x: array [2 .. 4] of integer;"""
        expect = str(Program([VarDecl(Id('x'),ArrayType(IntLiteral(2),IntLiteral(4),IntType()))]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_var_arr_complex(self):
        """test var complex"""
        input = """var x, y: array [2 .. 4] of integer;"""
        expect = str(Program([VarDecl(Id('x'),ArrayType(IntLiteral(2),IntLiteral(4),IntType())),VarDecl(Id('y'),ArrayType(IntLiteral(2),IntLiteral(4),IntType()))]))
        self.assertTrue(TestAST.test(input,expect,304))




    ############# end test var declare 

    #------------------------ test Funcdeclar -----------------
        # name, param, local, body, returnType=VoidType()
    # def test_simple_function(self):
    #     """More simple program"""
    #     input = """function foo ():INTEGER; 
    #     begin
            
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,305))
    
    # def test_function_with_para(self):
    #     """test_function_with_para"""
    #     input = """function foo (x, y: string):INTEGER; 
    #     begin
            
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id('x'),StringType()),VarDecl(Id('y'),StringType())],[],[], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,306))
    
    # def test_function_many_para(self):
    #     """test_function_many_para"""
    #     input = """function foo ( x: string; a: string):INTEGER; 
    #     begin
            
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id('x'),StringType()),VarDecl(Id('a'),StringType())],[],[], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,307))

    # def test_function_with_local(self):
    #     """test_function_many_para"""
    #     input = """function foo ():INTEGER; 
    #     var x:string;
    #     begin
            
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[VarDecl(Id('x'),StringType())],[], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,308))

    # def test_function_with_many_local(self):
    #     """test_function_with_many_local"""
    #     input = """function foo ():INTEGER; 
    #     var x:string;
    #         a, b: boolean;
    #     begin
            
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[VarDecl(Id('x'),StringType()), VarDecl(Id('a'),BoolType()), VarDecl(Id('b'),BoolType())],[], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,309))
    
    # def test_simple_AssignState(self):
    #     """test_simple_AssignState"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         y := 5;
    #     end"""
    #     expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('y'),IntLiteral(5))], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,310))
    # def test_complex_AssignState(self):
    #     """test_complex_AssignState"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         x := y := 5;
    #     end"""
    #     expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('x'),IntLiteral(5)), Assign(Id('y'),IntLiteral(5))], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,311))
    # def test_complex_AssignState_exp(self):
    #     """test_complex_AssignState_exp"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         x := (5+3);
    #     end"""
    #     expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('x'),BinaryOp('+',IntLiteral(5),IntLiteral(3)))], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,312))

    # def test_complex_many_assignState_exp(self):
    #     """test_complex_many_assignState_exp"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         x := y := (5+3);
    #     end"""
    #     expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('x'),BinaryOp('+',IntLiteral(5),IntLiteral(3))), Assign(Id('y'),BinaryOp('+',IntLiteral(5),IntLiteral(3)))], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,313))
    
    # def test_assignState_ArrayCell(self):
    #     """test_assignState_ArrayCell"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         c := b[10] := 4;
    #     end"""
    #     expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('c'),IntLiteral(4)), Assign(ArrayCell(Id('b'),IntLiteral(10)), IntLiteral(4))], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,314))
    
    # def test_assignState_exp_complex(self):
    #     """test_assignState_exp_complex"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #          y := (a[10]+3);
    #     end"""
    #     expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('y'),BinaryOp('+',ArrayCell(Id('a'),IntLiteral(10)),IntLiteral(3)))], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,315))
   
    # ifState : IF expr THEN stmt (ELSE stmt)?;
    # def test_ifState_miss_else(self):
    #     """test_ifState_miss_else"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         if (x=3) then x := 5;
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp('=',Id('x'),IntLiteral(3)),[Assign(Id('x'),IntLiteral(5))],[])], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,316))
    
    # def test_ifState_with_else(self):
    #     """test_ifState_with_else"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         if (x=3) then x := 5; else y := 4;
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp('=',Id('x'),IntLiteral(3)),[Assign(Id('x'),IntLiteral(5))],[Assign(Id('y'),IntLiteral(4))])], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,317))
    
    # def test_ifState_loop(self):
    #     """test_ifState_with_else"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         if a > 3 then
	# 			if a < 7 then 
	# 				b := b + 2;
	# 			else 
	# 				b := "huhuhu";
    #     end"""
    #     expect = str(Program([FuncDecl(Id('foo'),[],[],[If(BinaryOp('>',Id('a'),IntLiteral(3)),[If(BinaryOp('<',Id('a'),IntLiteral(7)),[Assign(Id('b'),BinaryOp('+',Id('b'),IntLiteral(2)))],[Assign(Id('b'),StringLiteral('huhuhu'))])],[])], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,318))
    

    # forState : FOR ID ASSIGN expr (TO|DOWNTO) expr DO stmt;
    # def test_forState(self):
    #     """test_forState"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         for i:= 1 to 10 do g:=5;
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id('i'),IntLiteral(1),IntLiteral(10),BooleanLiteral(False),[Assign(Id('g'),IntLiteral(5))])], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,319))
    
    # def test_forState_downto(self):
    #     """test_forState_downto"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         for i:= 1 downto 10 do g:=5;
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id('i'),IntLiteral(1),IntLiteral(10),BooleanLiteral(True),[Assign(Id('g'),IntLiteral(5))])], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,320))
    
    # def test_forState_expr(self):
    #     """test_ifState_with_else"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         for i:= 1 downto 10 do g:=5+g;
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id('i'),IntLiteral(1),IntLiteral(10),BooleanLiteral(True),[Assign(Id('g'),BinaryOp('+',IntLiteral(5),Id('g')))])], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,321))
    

    # whileState : WHILE expr DO stmt;
    # def test_whileState_expr(self):
    #     """test_whileState_expr"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         while x<3 do x := 5;
    #     end"""
    #     expect = str(Program([FuncDecl(Id('foo'),[],[],[While(BinaryOp('<',Id('x'),IntLiteral(3)),[Assign(Id('x'),IntLiteral(5))])], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,322))

    # def test_whileState_exprs(self):
    #     """test_whileState_exprs"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         while x<3 do x := y := 5;
    #     end"""
    #     expect = str(Program([FuncDecl(Id('foo'),[],[],[While(BinaryOp('<',Id('x'),IntLiteral(3)),[Assign(Id('x'),IntLiteral(5)), Assign(Id('y'),IntLiteral(5))])], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,323))
    # def test_whileState_loop(self):
    #     """test_whileState_loop"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         while x<3 do while x<3 do x := 5;
    #     end"""
    #     expect = str(Program([FuncDecl(Id('foo'),[],[],[While(BinaryOp('<',Id('x'),IntLiteral(3)),[While(BinaryOp('<',Id('x'),IntLiteral(3)),[Assign(Id('x'),IntLiteral(5))])])], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,324))
    # def test_ifstmt_inside_whileState(self):
    #     """test_ifstmt_inside_whileState"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         while x<3 do if (x=3) then x := 5; else y := 4; ;
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[While(BinaryOp('<',Id('x'),IntLiteral(3)),[If(BinaryOp('=',Id('x'),IntLiteral(3)),[Assign(Id('x'),IntLiteral(5))],[Assign(Id('y'),IntLiteral(4))])])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,325))

    # def test_forstmt_inside_whileState(self):
    #     """test_forstmt_inside_whileState"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         while x<3 do if (x=3) then for i:= 1 downto 10 do g:=5+g; 
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[While(BinaryOp('<',Id('x'),IntLiteral(3)),[If(BinaryOp('=',Id('x'),IntLiteral(3)),[For(Id('i'), IntLiteral(1),IntLiteral(10),BooleanLiteral(True),[Assign(Id('g'),BinaryOp('+',IntLiteral(5),Id('g')))])],[])])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,326))

     # Break;
    # def test_breakStmt(self):
    #     """test_breakStmt"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         break;
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[Break()],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,327))
    # def test_breakStmt_inside_while(self):
    #     """test_breakStmt_inside_while"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         while x<3 do Break;
    #     end"""
    #     expect = str(Program([FuncDecl(Id('foo'),[],[],[While(BinaryOp('<',Id('x'),IntLiteral(3)),[Break()])], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,328))
    
    # def test_breakStmt_inside_for(self):
    #     """test_breakStmt_inside_for"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         for i:= 1 downto 10 do break;
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id('i'), IntLiteral(1),IntLiteral(10),BooleanLiteral(True),[Break()])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,329))

    # # continueState : CONTINUE SEMI;
    # def test_continueState(self):
    #     """test_continueState"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         CONTINUE;
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[Continue()],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,330))
    # def test_continueState_inside_while(self):
    #     """test_continueState_inside_while"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         while x<3 do CONTINUE;
    #     end"""
    #     expect = str(Program([FuncDecl(Id('foo'),[],[],[While(BinaryOp('<',Id('x'),IntLiteral(3)),[Continue()])], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,331))
    
    # def test_continueState_inside_for(self):
    #     """test_continueState_inside_for"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         for i:= 1 downto 10 do CONTINUE;
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id('i'), IntLiteral(1),IntLiteral(10),BooleanLiteral(True),[Continue()])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,332))
    
    # returnState : RETURN expr? SEMI;
    # def test_returnState(self):
    #     """test_returnState"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         RETURN;
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[Return()],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,333))
    # def test_returnState_inside_while(self):
    #     """test_returnState_inside_while"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         while x<3 do RETURN;
    #     end"""
    #     expect = str(Program([FuncDecl(Id('foo'),[],[],[While(BinaryOp('<',Id('x'),IntLiteral(3)),[Return()])], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,334))
    
    # def test_returnState_inside_for(self):
    #     """test_returnState_inside_for"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         for i:= 1 downto 10 do RETURN;
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id('i'), IntLiteral(1),IntLiteral(10),BooleanLiteral(True),[Return()])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,335))
    # def test_returnState_expr(self):
    #     """test_returnState"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         RETURN x+3;
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[Return(BinaryOp('+',Id('x'),IntLiteral(3)))],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,336))
    # def test_returnState_expr_inside_while(self):
    #     """test_returnState_inside_while"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         while x<3 do RETURN x+3;
    #     end"""
    #     expect = str(Program([FuncDecl(Id('foo'),[],[],[While(BinaryOp('<',Id('x'),IntLiteral(3)),[Return(BinaryOp('+',Id('x'),IntLiteral(3)))])], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,337))
    
    # def test_returnState_expr_inside_for(self):
    #     """test_returnState_inside_for"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         for i:= 1 downto 10 do RETURN 5;
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id('i'), IntLiteral(1),IntLiteral(10),BooleanLiteral(True),[Return(IntLiteral(5))])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,338))

    #  withState : WITH  variable+ DO stmt;
    def test_withState(self):
        """test_withState"""
        input = """function foo ():INTEGER; 
        begin
            with a : string; do d := 4;
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[With([VarDecl(Id('a'),StringType())],[Assign(Id('d'),IntLiteral(4))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,339))
    def test_withState_var(self):
        """test_withState_var"""
        input = """function foo ():INTEGER; 
        begin
            with a, b, x : string; do d := 4;
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[With([VarDecl(Id('a'),StringType()),VarDecl(Id('b'),StringType()),VarDecl(Id('x'),StringType())],[Assign(Id('d'),IntLiteral(4))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,400))
    def test_withState_vars(self):
        """test_withState_vars"""
        input = """function foo ():INTEGER; 
        begin
            with a, b : string; x : integer; do d := 4;
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[With([VarDecl(Id('a'),StringType()),VarDecl(Id('b'),StringType()),VarDecl(Id('x'),IntType())],[Assign(Id('d'),IntLiteral(4))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,401))


    #------------------------ End test Funcdeclar -----------------




   