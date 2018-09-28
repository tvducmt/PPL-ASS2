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
    def test_forState(self):
        """test_forState"""
        input = """function foo ():INTEGER; 
        begin
            for i:= 1 to 10 do g:=5;
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id('i'),IntLiteral(1),IntLiteral(10),BooleanLiteral(False),[Assign(Id('g'),IntLiteral(5))])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,319))
    
    def test_forState_downto(self):
        """test_forState_downto"""
        input = """function foo ():INTEGER; 
        begin
            for i:= 1 downto 10 do g:=5;
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id('i'),IntLiteral(1),IntLiteral(10),BooleanLiteral(True),[Assign(Id('g'),IntLiteral(5))])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,320))
    
    # def test_forState_expr(self):
    #     """test_ifState_with_else"""
    #     input = """function foo ():INTEGER; 
    #     begin
    #         for i:= 1 downto 10 do g:=5;
    #     end"""
    #     expect = str(Program([FuncDecl(Id('foo'),[],[],[If(BinaryOp('>',Id('a'),IntLiteral(3)),[If(BinaryOp('<',Id('a'),IntLiteral(7)),[Assign(Id('b'),BinaryOp('+',Id('b'),IntLiteral(2)))],[Assign(Id('b'),StringLiteral('huhuhu'))])],[])], IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,318))

    #------------------------ End test Funcdeclar -----------------




    # def test_call_without_parameter(self):
    #     """More complex program"""
    #     input = """procedure main (); begin
    #         getIntLn();
    #     end
    #     function foo ():INTEGER; begin
    #         putIntLn(4);
    #     end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),[],[],[CallStmt(Id("getIntLn"),[])]),
    #             FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,302))
   