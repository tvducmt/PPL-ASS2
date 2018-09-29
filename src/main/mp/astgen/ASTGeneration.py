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
            arr = ''
            for i in self.visit(ctx.varDeclare()):
                arr= arr+ ","+ (str(i))
            return arr[1:]
            #return self.visit(ctx.varDeclare())
        elif ctx.funcdeclare() is not None:
            return self.visit(ctx.funcdeclare())
        else :
            return self.visit(ctx.procdecl())
            
    #   varDeclare : VAR variable+ ; 
    def visitVarDeclare(self, ctx: MPParser.VarDeclareContext):
        arr = []
        for item in ctx.variable():
            for one in self.visit(item):
                arr.append(one)
        return arr 
    
    #   variable : idlist COLON vartype SEMI;
    def visitVariable(self, ctx:MPParser.VariableContext):
        varType = self.visit(ctx.vartype())
        return list(map(lambda x: VarDecl(Id(x.getText()), varType), ctx.ID()))
       

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
    def visitCompoundtype(self, ctx: MPParser.CompoundtypeContext):
        return ArrayType(IntLiteral(ctx.getChild(2)), IntLiteral(ctx.getChild(4)), self.visit(ctx.primtype()))



    ######################## funcdeclare

    #FUNCTION ID LB parameterlist RB COLON vartype SEMI varDeclare? compoundstate;
    def visitFuncdeclare(self, ctx:MPParser.FuncdeclareContext):
        para = self.visit(ctx.paramlist())
        varType= self.visit(ctx.vartype())
        cpstate = self.visit(ctx.cpstate())
        #if cpstate != []:
         #   print("cpstate")
            #print(cpstate)
        if ctx.varDeclare() is not None:
            return FuncDecl(Id(ctx.ID().getText()), para,  self.visit(ctx.varDeclare()), cpstate, varType)
        return FuncDecl(Id(ctx.ID().getText()), para, [], cpstate, varType)

    #  paramlist :  param (SEMI param)* | ;
    def visitParamlist(self, ctx: MPParser.ParamlistContext):
        arr = []
        for item in ctx.param():
            for one in self.visit(item):
                arr.append(one)
        return arr     
        #return list(map(lambda x: self.visit(x), ctx.param()))
      

    # param : idlist COLON vartype;
    def visitParam(self, ctx: MPParser.ParamContext):
        varType = self.visit(ctx.vartype())
        return list(map(lambda x: VarDecl(Id(x.getText()), varType), ctx.ID()))
       
    #   cpstate : BEGIN (stmt)* END;
    def visitCpstate(self, ctx: MPParser.CpstateContext):
        return list(map(lambda x: self.visit(x),ctx.stmt()))

    def visitStmt(self, ctx:MPParser.StmtContext):
        if ctx.assignState() is not None:
            return self.visit(ctx.assignState())
        elif ctx.ifState() is not None:
            return self.visit(ctx.ifState())
        elif ctx.forState() is not None:
            return self.visit(ctx.forState())
        elif ctx.whileState() is not None:
            return self.visit(ctx.whileState())
        elif ctx.breakState() is not None:
            return self.visit(ctx.breakState())
        elif ctx.continueState() is not None:
            return self.visit(ctx.continueState())
        elif ctx.returnState() is not None:
            return self.visit(ctx.returnState())
        elif ctx.callState() is not None:
            return self.visit(ctx.callState())
        elif ctx.cpstate() is not None:
            return self.visit(ctx.cpstate())
        elif ctx.withState() is not None:
            return self.visit(ctx.withState())
        else:
            print("into here defaultFunction")
            return self.visit(ctx.defaultFunction())


    #-------------Stmt ---------------------------------------------

    # assignState : oneAssign (oneAssign)* expr SEMI;
    # oneAssign   : (ID|expr5) ASSIGN;
    def visitAssignState(self, ctx: MPParser.AssignStateContext):
        arr = ''
        print(self.visit(ctx.expr()))
        for i in ctx.oneAssign() :
            assign =  Assign((self.visit(i)), self.visit(ctx.expr()))
            arr = arr + ',' + str(assign)         
        return arr[1:]
       
     # oneAssign   : (ID|expr5) ASSIGN;
    def visitOneAssign(self, ctx:MPParser.OneAssignContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else :
            return self.visit(ctx.expr5())
    # ifState : IF expr THEN stmt (ELSE stmt)?;
    def visitIfState(self, ctx:MPParser.IfStateContext):
         #expr:Expr
         #thenStmt:list(Stmt)
         #elseStmt:list(Stmt)
         expr = self.visit(ctx.expr())
         thenStmt = [self.visit(ctx.stmt(0))]
        
         if ctx.stmt(1) :
            elseStmt =[self.visit(ctx.stmt(1))]
            return If(expr, thenStmt,elseStmt )
         return If(expr, thenStmt, [])

    #  forState : FOR ID ASSIGN expr (TO|DOWNTO) expr DO stmt;
    def visitForState(self, ctx:MPParser.ForStateContext):
         #id:Id
        #expr1,expr2:Expr
        #loop:list(Stmt)
        #up:Boolean #True => increase; False => decrease
         loop = [self.visit(ctx.stmt())]
         print(loop)
         checkDown = True
         if ctx.TO():
             checkDown = False
         up = BooleanLiteral(checkDown)
         print(up)
         return For(Id(ctx.ID().getText()), self.visit(ctx.expr(0)),self.visit(ctx.expr(1)), up, loop)
    
    # whileState : WHILE expr DO stmt;
    def visitWhileState(self, ctx: MPParser.WhileStateContext):
        #sl:list(Stmt)
        #exp: Expr
         sl = [self.visit(ctx.stmt())]
         exp = self.visit(ctx.expr())
         return While(exp, sl)
    
    # breakState : BREAK SEMI;
    def visitBreakState(self, ctx:MPParser.BreakStateContext):
         return Break()
    # continueState : CONTINUE SEMI;
    def visitContinueState(self, ctx:MPParser.ContinueStateContext):
         return Continue()
    # returnState : RETURN expr? SEMI;
    def visitReturnState(self, ctx:MPParser.ReturnStateContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return(None)
    # withState : WITH  variable+ DO stmt;
    def visitWithState(self, ctx:MPParser.WithStateContext):
        #decl:list(VarDecl)
        #stmt:list(Stmt)
        decl = []
        for item in ctx.variable():
            for one in self.visit(item):
                decl.append(str(one))
        stmt= [self.visit(ctx.stmt())]
       
        return With(decl, stmt)


    # ---------------------------Expression----------------------------------------------
        #expr: expr ANDTHEN expr1
        #| expr ORELSE expr1
        #| expr1;
    def visitExpr(self, ctx:MPParser.ExprContext):
        if ctx.getChildCount() == 1 :
            #print("00")
            return self.visit(ctx.expr1())
        else:
            if ctx.ANDTHEN() :
                #print("01")
                return BinaryOp(ctx.ANDTHEN().getText(), self.visit(ctx.expr()), self.visit(ctx.expr1()))
            else :
                #print("02")
                return BinaryOp(ctx.ORELSE().getText(), self.visit(ctx.expr()), self.visit(ctx.expr1()))

    #expr1: expr2 (EQUAL|NOTEQUAL| LESSTHAN|LESOREQUAL|GREATERTHAN |GREOREQUAL) expr2 | expr2;
    def visitExpr1(self, ctx:MPParser.Expr1Context):
        
        if ctx.getChildCount() == 1 :
            #print("10")
            return self.visit(ctx.expr2(0))
        else:
            #print("11")
            op = ctx.getChild(1).getText()
            
            #print(str(op))
            left = self.visit(ctx.expr2(0))
            right = self.visit(ctx.expr2(1))
            return BinaryOp(op, left, right)
    
    #expr2: expr2 (ADDITION |SUBORNE | OR) expr3 | expr3;
    def visitExpr2(self, ctx:MPParser.Expr2Context):
       
        if ctx.getChildCount() == 1 :
            #print("20")
            return self.visit(ctx.expr3())
        else:
            #print("21")
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            #print(left)
            #print(right)
            #print(BinaryOp(op, left, right))
            return BinaryOp(op, left, right)

    #expr3: expr3 (DIVISION |  MULTIPLICATION | MOD | AND | INTDIV) expr4 | expr4;
    def visitExpr3(self, ctx:MPParser.Expr3Context):
        
        if ctx.getChildCount() == 1 :
            #print("30")
            return self.visit(ctx.expr4())
        else:
            #print("31")
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            return BinaryOp(op, left, right)
    
    # expr4:  (NOT| SUBORNE) expr4| expr5;
    def visitExpr4(self, ctx:MPParser.Expr4Context):
        
        if ctx.getChildCount() == 1 :
            #print("40")
            return self.visit(ctx.expr5())
        else:
            #print("41")
            op = ctx.getChild(0).getText()
            return UnaryOp(op, self.visit(ctx.expr4()))

    # expr5: expr6 LSB expr RSB| expr6;
    def visitExpr5(self, ctx:MPParser.Expr5Context):
        
        if ctx.getChildCount() == 1 :
            #print("50")
            return self.visit(ctx.expr6())
        else:
            #print("51")
            arr = self.visit(ctx.expr6())
            print(arr)
            expr = self.visit(ctx.expr())
            print(expr)
            return ArrayCell(arr, expr)
    
    # expr6: LB expr RB
    # | INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT | ID | funcall;

    def visitExpr6(self, ctx:MPParser.Expr6Context):
        
        if ctx.getChildCount() == 3 :
            #print("60")
            return self.visit(ctx.expr())
        else:
            #print("61")
            if ctx.INTLIT():
                return IntLiteral(ctx.INTLIT())
            elif ctx.BOOLEANLIT():
                return BooleanLiteral(ctx.BOOLEANLIT())
            elif ctx.FLOATLIT():
                return FloatLiteral(ctx.FLOATLIT())
            elif ctx.STRINGLIT():
                return StringLiteral(ctx.STRINGLIT().getText())
            elif ctx.ID():
                return Id(ctx.ID().getText())
            elif ctx.funcall():
                self.visit(ctx.funcall())
                 

    def visitFuncall(self, ctx: MPParser.FuncallContext):
        exprList = self.visit(ctx.exprList())
        return CallExpr(Id(ctx.ID().getText()), exprList)

    def visitExprList(self, ctx:MPParser.ExprListContext):
        arr=[]
        if self.visit(ctx.expr()) != [] :
            for one in ctx.expr():
                arr.append(one)
        return arr







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
        

