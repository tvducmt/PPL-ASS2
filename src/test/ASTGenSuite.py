import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """var x, y: string;"""
        expect = str(Program([VarDecl(Id("x"),StringType)]))
        self.assertTrue(TestAST.test(input,expect,306))

    # def test_simple_function(self):
    #     """More complex program"""
    #     input = """function foo ( x: string):INTEGER; 
    #         var k, f : string;
    #     begin
            
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,301))
    
    # def test_simple_function(self):
    #     """More complex program"""
    #     input = """function foo ():INTEGER; 
    #         var k, f : string;
    #     begin
            
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,302))
    
    # def test_simple_function(self):
    #     """More complex program"""
    #     input = """function foo ( x: string):INTEGER; 
    #     begin
            
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,303))
    
    # def test_simple_function(self):
    #     """More complex program"""
    #     input = """function foo ():INTEGER; 
    #     begin
            
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,304))
    
    # def test_simple_function(self):
    #     """More complex program"""
    #     input = """function foo ( x: string):INTEGER; 
    #         var k, f : string;
    #     begin
    #         a := 4;
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,305))
    
    

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
   