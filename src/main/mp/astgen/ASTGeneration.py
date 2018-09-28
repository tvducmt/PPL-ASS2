from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    ##  program  : declare+ EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(list(map(lambda x: self.visit(x), ctx.declare())))
    
    #  declare : varDeclare | funcdeclare | procdecl;
    def visitDeclare(self, ctx: MPParser.DeclareContext):
        if ctx.varDeclare() is not None:
            return self.visit(ctx.varDeclare())
        elif ctx.funcdeclare() is not None:
            return self.visit(ctx.funcdeclare())
        else :
            return self.visit(ctx.procdecl())
            
    #   varDeclare : VAR variable+ ; 
    def visitVarDeclare(self, ctx: MPParser.VarDeclareContext):
        arr = []
        for item in ctx.variable():
            arr.append(self.visit(item))
        return str(arr)[2:-2]
        #return list(map(lambda x: self.visit(x), ctx.variable()))
   
    #   variable : idlist COLON vartype SEMI;
    def visitVariable(self, ctx:MPParser.VariableContext):
        #varble= self.visit(ctx.idlist())
        varType = self.visit(ctx.vartype())
        return list(map(lambda x: VarDecl(x, varType).__str__(), ctx.ID()))
       
    
    #   idlist : ID (COMMA ID)*;
    # def visitIdlist(self, ctx:MPParser.IdlistContext):
    #     return list(map(lambda x: Id(x.getText()), ctx.ID()))
        
    #   vartype : primtype | compoundtype ;
    def visitVartype(self, ctx: MPParser.VartypeContext):
        if ctx.primtype() is not None :
            return self.visit(ctx.primtype())
        else:
            return self.visit(ctx.compoundtype())
    #   primtype: INTTYPE | STRINGTYPE | BOOLEANTYPE | REALTYPE ;
    def visitPrimtype(self, ctx: MPParser.PrimtypeContext):
        if ctx.INTTYPE() is not None :
            return IntType()
        elif ctx.STRINGTYPE() is not None:
            return StringType()
        elif ctx.BOOLEANTYPE() is not None:
            return BoolType()
        else :
            return FloatType()

    ######################## funcdeclare

    #FUNCTION ID LB parameterlist RB COLON vartype SEMI varDeclare? compoundstate;
    def visitFuncdeclare(self, ctx:MPParser.FuncdeclareContext):
        para = self.visit(ctx.paramlist())
        varType= self.visit(ctx.vartype())
        cpstate = self.visit(ctx.cpstate())
        if ctx.varDeclare() is not None:
            return FuncDecl(Id(ctx.ID().getText()), para,  self.visit(ctx.varDeclare()), cpstate, varType)
        return FuncDecl(Id(ctx.ID().getText()), para, [], cpstate, varType)

    #  paramlist :  param (SEMI param)* | ;
    def visitParamlist(self, ctx: MPParser.ParamlistContext):
        return list(map(lambda x: self.visit(x), ctx.param()))
      

    # param : idlist COLON vartype;
    def visitParam(self, ctx: MPParser.ParamContext):
        varble= self.visit(ctx.idlist())
        varType = self.visit(ctx.vartype())
        return list(map(lambda x: VarDecl(x, varType).__str__(), varble))
    
    #   cpstate : BEGIN (stmt)* END;
    def visitCpstate(self, ctx: MPParser.CpstateContext):
        return [self.visit(ctx.stmt())] if ctx.stmt() else []

    def visitStmt(self, ctx:MPParser.StmtContext):
        if ctx.assignState() is not None:
            print("into here")
            self.visit(ctx.assignState())
        elif ctx.ifState() is not None:
            self.visit(ctx.ifState())
        elif ctx.forState() is not None:
            self.visit(ctx.forState())
        elif ctx.whileState() is not None:
            self.visit(ctx.whileState())
        elif ctx.breakState() is not None:
            self.visit(ctx.breakState())
        elif ctx.continueState() is not None:
            self.visit(ctx.continueState())
        elif ctx.returnState() is not None:
            self.visit(ctx.returnState())
        elif ctx.callState() is not None:
            self.visit(ctx.callState())
        elif ctx.cpstate() is not None:
            self.visit(ctx.cpstate())
        elif ctx.withState() is not None:
            self.visit(ctx.withState())
        else:
            self.visit(ctx.defaultFunction())
        
    def visitAssignState(self, ctx: MPParser.AssignStateContext):
        lhs =list(map(lambda x: self.visit(x), ctx.oneAssign))
        #lhs = visit(ctx.ID()) if ctx.ID() else 
        exp = self.visit(ctx.expr())
        return list(map(lambda x: Assign(x, exp), lhs)) 
     
    def visitOneAssign(self, ctx:MPParser.OneAssignContext):
        return self.visit(ctx.ID()) if ctx.ID() else self.visit(ctx.expr5())

    # ---------------------------Expression----------------------------------------------
    def visitExpr(self, ctx:MPParser.ExprContext):
        if ctx.getChildCount() == 1 :
            self.visit(ctx.expr1())
        else:
            return BinaryOp(self.visit(ctx.AND))











    # def visitFuncdeclare(self,ctx: MPParser.FuncdeclareContext):
    #     return FuncDecl(ctx.ID(), [],)


    # def visitFunction_declare(self,ctx:MPParser.Function_declareContext):
    #     local,cpstmt = self.visit(ctx.body()) 
    #     return FuncDecl(Id(ctx.ID().getText()),
    #                     [],
    #                     local,
    #                     cpstmt,
    #                     self.visit(ctx.mtype()))

    # def visitProcdecl(self,ctx:MPParser.ProcdeclContext):
    #     local,cpstmt = self.visit(ctx.body()) 
    #     return FuncDecl(Id(ctx.ID().getText()),
    #                     [],
    #                     local,
    #                     cpstmt)

    # def visitBody(self,ctx:MPParser.BodyContext):
    #     return [],[self.visit(ctx.stmt())] if ctx.stmt() else []
  
    # def visitStmt(self,ctx:MPParser.StmtContext):
    #     return self.visit(ctx.funcall())

    # def visitFuncall(self,ctx:MPParser.FuncallContext):
    #     return CallStmt(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    # def visitExp(self,ctx:MPParser.ExpContext):
    #     return IntLiteral(int(ctx.INTLIT().getText()))

    # def visitMtype(self,ctx:MPParser.MtypeContext):
    #     return IntType()
        

