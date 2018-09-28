import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
     #test var declar
    def test_variable_declar(self):
        """test variable declar"""
        input="""var a  : integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_variable_declar_many(self):
        """test variable declar many"""
        input="""var a , b , c : integer ; e , f : real ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    def test_variable_declar_array(self):
        """test variable declar many"""
        input="""var d , b : array [    1 .. 5    ] of integer ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_variable_declar_error(self):
        """test variable declar many"""
        input="""d , b : array [    1 .. 5    ] of integer ;"""
        expect = "Error on line 1 col 0: d"
        self.assertTrue(TestParser.test(input,expect,204))
    
    #test function declar
    def test_function_declar(self):
        """test function declar """
        input="""function foo (a , b : integer ; c : real ) : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_function_declar_error_para(self):
        """test function declar para """
        input="""function foo (a , b : integer  ;) : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 32: )"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_function_empty_para(self):
        """test function declar """
        input="""function foo () : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_wrong_miss_close(self):
        """test function declar """
        input="""function foo ( : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 15: :"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_function_named_error(self):
        """test function declar """
        input="""function 1foo (): array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 9: 1"
        self.assertTrue(TestParser.test(input,expect,209))  
    def test_function_named(self):
        """test function named """
        input="""function _ADVCDfoo     (): array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))  
    def test_wrong_miss_colon(self):
        """test wrong miss colon """
        input="""function foo ()  array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 17: array"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_wrong_miss_body(self):
        """test wrong miss body """
        input="""function foo () : array [ 1 .. 2 ] of integer ;
            var x , y : real ;  """
           
        expect = "Error on line 2 col 32: <EOF>"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_wrong_miss_return(self):
        """ test wrong miss return """
        input="""function foo ();
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 15: ;"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_wrong_miss_semi(self):
        """test wrong miss semi """
        input="""function foo () : array [ 1 .. 2 ] of integer 
            var x , y : real ;
            begin
            
            end"""
        expect = "Error on line 2 col 12: var"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_wrong_miss_semi_var(self):
        """test wrong miss semi var """
        input="""function foo () : array [ 1 .. 2 ] of integer ;
            var x , y : real 
            begin
            
            end"""
        expect = "Error on line 3 col 12: begin"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_wrong_miss_close_body(self):
        """test wrong miss body end"""
        input="""function foo () : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin"""
        expect = "Error on line 3 col 17: <EOF>"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_case_insensitive_1(self):
        """test_case_insensitive_1"""
        input="""FuNctIon _ADVCDfoo     (): array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_wrong_type_return(self):
        """test_wrong_type_return"""
        input="""function _ADVCDfoo     (): array [ 1 .. 2 ] of array [ 1 .. 2 ] ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 47: array"
        self.assertTrue(TestParser.test(input,expect,218))
    #test procedure declar
    def test_procedure_declar(self):
        """test_procedure_declar"""
        input="""procedure abc ();
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    
    def test_case_insensitive(self):
        """test_case_insensitive"""
        input="""prOceDure _ADVCDfoo ();
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_wrong_redundancy_colon(self):
        """test_wrong_redundancy_colon"""
        input="""procedure abc (): array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 16: :"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_wrong_miss_semi_produre(self):
        """test_wrong_redundancy_colon"""
        input="""procedure abc ()
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 2 col 12: var"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_wrong_miss_body_produre(self):
        """test_wrong_miss_body_produre """
        input="""procedure foo ();
            var x , y : real ;  """
           
        expect = "Error on line 2 col 32: <EOF>"
        self.assertTrue(TestParser.test(input,expect,223))
    #test Assignment Statement
    def test_assignment_stmt_simple(self):
        """test_assignment_stmt"""
        input= """procedure abc ();
            var x , y : real ; 
            begin
                a:=12;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,224))
    def test_assignment_stmt_many(self):
        """test_assignment_stmt_many"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                a:=b:=c:=d:=12;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,225))
    def test_assign_stmt_with_expr(self):
        """test_assign_stmt_with_expr"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                a:=b:=c:=d:=(12+3);
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,226))
    def test_assign_stmt_with_funcall(self):
        """test_assign_stmt_with_expr"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                a:=b:=c:=d:=foo();
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,227))
    def test_assign_stmt_with_funcall_semi(self):
        """test_assign_stmt_with_expr"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                a:=b:=c:=d:=foo(2+3;);
            end"""
        expect='Error on line 4 col 35: ;'
        self.assertTrue(TestParser.test(input,expect,228))
    def test_assign_stmt_with_funcall_explist(self):
        """test_assign_stmt_with_funcall_explist"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                a:=b:=c:=d:=foo(2+3, 3*3, a AND b);
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,229))
    def test_assign_stmt_with_realtype(self):
        """test_assign_stmt_with_funcall_explist"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                some_real := 37573.5 * 37593 + 385.8 / 367.1;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,230))
        
    #test_if_state
    def test_ifstate(self):
        """test_ifstate"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                if color = red then
                   a:=3;
                else
                    b:=3;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,231))
    def test_ifstate_miss_else(self):
        """test_ifstate_miss_else"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                if color = red then
                    b:=3;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,232))
    def test_ifstate_miss_bodyif(self):
        """test_ifstate_miss_bodyif"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                if color = red then
            end"""
        expect='Error on line 5 col 12: end'
        self.assertTrue(TestParser.test(input,expect,233))
    def test_ifstate_miss_exp(self):
        """test_ifstate_miss_exp"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                if  then
                    b:=3;
            end"""
        expect='Error on line 4 col 20: then'
        self.assertTrue(TestParser.test(input,expect,234))
    def test_ifstate_wrong_exp(self):
        """test_ifstate_wrong_exp"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                if +hello then
                    b:=3;
            end"""
        expect='Error on line 4 col 19: +'
        self.assertTrue(TestParser.test(input,expect,235))
    def test_ifstate_wrong_exp_real(self):
        """test_ifstate_wrong_exp_real"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                if 3//4 then
                    b:=3;
            end"""
        expect='Error on line 5 col 20: b'
        self.assertTrue(TestParser.test(input,expect,236))
    def test_ifstate_have_semi(self):
        """test_ifstate_have_semi"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                if color = red then;
                    hk:=56;
            end"""
        expect='Error on line 4 col 35: ;'
        self.assertTrue(TestParser.test(input,expect,237))
    def test_ifstate_have_semi_else(self):
        """test_ifstate_have_semi_else"""
        input= """procedure abc ();
        var x , y : real ; 
            begin
                if color = red then
                   a:=3;
                else;
                    b:=3;
            end"""
        expect='Error on line 6 col 20: ;'
        self.assertTrue(TestParser.test(input,expect,238))
    #test_for_state 
    def test_for_state_to(self):
        """test_for_state_to"""
        input= """procedure ABC ();
        var x , y : real ; 
            begin
                for i:= 1 to 10 do g:=5;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,239))
    def test_for_state_downto(self):
        """test_for_state_downto"""
        input= """procedure ABC ();
        var x , y : real ; 
            begin
                for i:= 1 downto 10 do g:=5;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,240))
    def test_for_state_miss_colon(self):
        """test_for_state_miss_colon"""
        input= """procedure ABC ();
        var x , y : real ; 
            begin
                for i= 1 downto 10 do g:=5;
            end"""
        expect='Error on line 4 col 21: ='
        self.assertTrue(TestParser.test(input,expect,241))
    def test_for_state_wrong_downto(self):
        """test_for_state_wrong_downto"""
        input= """procedure ABC ();
        var x , y : real ; 
            begin
                for i:= 1 dwnto 10 do g:=5;
            end"""
        expect='Error on line 4 col 26: dwnto'
        self.assertTrue(TestParser.test(input,expect,242))
    def test_for_state_miss_assign(self):
        """test_for_state_miss_assign"""
        input= """procedure ABC ();
        var x , y : real ; 
            begin
                for dwnto 10 do g:=5;
            end"""
        expect='Error on line 4 col 26: 10'
        self.assertTrue(TestParser.test(input,expect,243))
    def test_for_state_miss_stmt(self):
        """test_for_state_miss_stmt"""
        input= """procedure ABC ();
        var x , y : real ; 
            begin
                for i:= 1 downto 10 do ;
            end"""
        expect='Error on line 4 col 39: ;'
        self.assertTrue(TestParser.test(input,expect,244))
    def test_for_state_many_stmt(self):
        """test_for_state_many_stmt"""
        input= """procedure ABC ();
        var x , y : real ; 
            begin
                for i:= 1 downto 10 do a := 3; d := 5;
                if color = red then
                   a:=3;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,245))
    def test_for_state_named(self):
        """test_for_state_named"""
        input= """procedure ABC ();
        var x , y : real ; 
            begin
                for 123:= 1 downto 10 do a := 3; d := 5;
            end"""
        expect='Error on line 4 col 20: 123'
        self.assertTrue(TestParser.test(input,expect,246))
    #test while state
    def test_while_state(self):
        """test_while_tate"""
        input= """procedure whilestate ();
        var x , y : real ; 
            begin
                while a = true do b := 5; d := 24; d := 25; ;
            end"""
        expect='Error on line 4 col 60: ;'
        self.assertTrue(TestParser.test(input,expect,247))
    def test_whilestate_many_stmt(self):
        """test_whilestate_many_stmt"""
        input= """procedure whilestate ();
        var x , y : real ; 
            begin
                while a = true do b := 5; d := 24; d := 25;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,248))
    def test_whilestate_wrong_expr(self):
        """test_whilestate_wrong_expr"""
        input= """procedure whilestate ();
        var x , y : real ; 
            begin
                while a := true do b := 5;;
            end"""
        expect='Error on line 4 col 24: :='
        self.assertTrue(TestParser.test(input,expect,249))
    def test_whilestate_miss_body(self):
        """test_whilestate_miss_body"""
        input= """procedure whilestate ();
        var x , y : real ; 
            begin
                while a = true do ;
            end"""
        expect='Error on line 4 col 34: ;'
        self.assertTrue(TestParser.test(input,expect,250))
    def test_whilestate_miss_expr(self):
        """test_whilestate_miss_expr"""
        input= """procedure whilestate ();
        var x , y : real ; 
            begin
                while  do  s := 234;;
            end"""
        expect='Error on line 4 col 23: do'
        self.assertTrue(TestParser.test(input,expect,251))
    def test_whilestate_miss_semi(self):
        """test_whilestate_miss_expr"""
        input= """procedure whilestate ();
        var x , y : real ; 
            begin
                while  a =4 do  s := 234;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,252))
    #test break state
    def test_break_state(self):
        """test_break_state"""
        input= """procedure break_state ();
        var x , y : real ; 
            begin
                while  a =4 do  break;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,253))
    def test_break_state_miss_semi(self):
        """test_break_state_miss_semi"""
        input= """procedure break_state ();
        var x , y : real ; 
            begin
                while  a =4 do  break;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,254))
    def test_break_state_with_for(self):
        """test_break_state_with_for"""
        input= """procedure break_state ();
        var x , y : real ; 
            begin
                for  a :=4 to 23 do  break;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,255))
    #test continue state
    def test_continue_state_withfor(self):
        """test_continue_state_withfor"""
        input= """procedure continue_state();
        var x , y : real ; 
            begin
                for  a :=4 to 23 do  continue;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,256))
    def test_continue_state_withwhile(self):
        """test_continue_state_withwhile"""
        input= """procedure continue_state();
        var x , y : real ; 
            begin
                while  a =4 do  continue;;
            end"""
        expect='Error on line 4 col 41: ;'
        self.assertTrue(TestParser.test(input,expect,257))
    def test_continue_state_miss_semi(self):
        """test_continue_state_miss_semi"""
        input= """procedure continue_state();
        var x , y : real ; 
            begin
                while  a =4 do  continue;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,258))
    def test_continue_state_wrong_stmt(self):
        """test_continue_state_wrong_stmt"""
        input= """procedure continue_state();
        var x , y : real ; 
            begin
                while  a =4 do  coninue+fg**3;;
            end"""
        expect='Error on line 4 col 39: +'
        self.assertTrue(TestParser.test(input,expect,259))
    #test return_state
    def test_return_state(self):
        """test_return_state"""
        input= """procedure return_state();
        var x , y : real ; 
            begin
                return a=4;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,260))
    def test_return_state_non_expr(self):
        """test_return_state_non_expr"""
        input= """procedure return_state();
        var x , y : real ; 
            begin
                return ;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,261))
    def test_return_state_miss_semi(self):
        """test_return_state_non_expr"""
        input= """procedure return_state();
        var x , y : real ; 
            begin
                return 
            end"""
        expect='Error on line 5 col 12: end'
        self.assertTrue(TestParser.test(input,expect,262))
    #test with_state
    def test_with_state(self):
        """test_with_state"""
        input= """procedure with_state();
        var x , y : real ; 
            begin
                with a , b : integer ; c : array [ 1 .. 2 ] of real ; do
                    d := 34; 
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,263))
    def test_with_state_non_var(self):
        """test_with_state_non_var"""
        input= """procedure with_state();
        var x , y : real ; 
            begin
                with  do
                    d = 34; 
            end"""
        expect='Error on line 4 col 22: do'
        self.assertTrue(TestParser.test(input,expect,264))
    def test_with_state_one_var(self):
        """test_with_state_one_var"""
        input= """procedure with_state();
        var x , y : real ; 
            begin
                with a , b : integer ;  do
                    a := 34; 
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,265))
    def test_with_state_wrong_declar(self):
        """test_with_state_wrong_declar"""
        input= """procedure with_state();
        var x , y : real ; 
            begin
                with a , b  integer ;  do
                    a = 34; 
            end"""
        expect='Error on line 4 col 28: integer'
        self.assertTrue(TestParser.test(input,expect,266))

    #test call_state
    def test_call_state_simple(self):
        """test_call_state_simple"""
        input= """procedure call_state();
        var x , y : real ; 
            begin
                foo () ;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,267))
    def test_call_state_many_para(self):
        """test_call_state_many_para"""
        input= """procedure call_state();
        var x , y : real ; 
            begin
                foo (23+45, hello) ;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,268))
    def test_call_state_complex(self):
        """test_call_state_complex"""
        input= """procedure call_state();
        var x , y : real ; 
            begin
                foo ( 3 , a+1, m( 2 ) ) ;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,269))
    def test_call_state_miss_LB(self):
        """test_call_state_miss_LB"""
        input= """procedure call_state();
        var x , y : real ; 
            begin
                foo ) ;
            end"""
        expect='Error on line 4 col 20: )'
        self.assertTrue(TestParser.test(input,expect,270))
    def test_call_state_miss_semi(self):
        """test_call_state_miss_semi"""
        input= """procedure call_state();
            var x , y : real ; 
            begin
                foo () 
            end"""
        expect='Error on line 5 col 12: end'
        self.assertTrue(TestParser.test(input,expect,271))
    #test compound_state 
    def test_compound_state(self):
        """test_compound_state"""
        input= """procedure compound_state();
           var x , y : real ; 
            begin
                
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,272))
    #test Built-in Functions
    def test_getInt(self):
        """test_getInt"""
        input= """procedure built_in();
            var x , y : real ; 
            begin
                getInt();
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,273))
    def test_getInt_wrong_para(self):
        """test_getInt"""
        input= """procedure built_in();
            var x , y : real ; 
            begin
                getInt(23.34);
            end"""
        expect='Error on line 4 col 23: 23.34'
        self.assertTrue(TestParser.test(input,expect,274))
    def test_putInt(self):
        """test_putInt"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                putInt();
            end"""
        expect='Error on line 4 col 23: )'
        self.assertTrue(TestParser.test(input,expect,275))
    def test_putInt_wrong_para(self):
        """test_putInt_wrong_para"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                putInt(23.34);
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,276))
    def test_putIntLn(self):
        """test_putIntLn"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                putIntLn();
            end"""
        expect='Error on line 4 col 25: )'
        self.assertTrue(TestParser.test(input,expect,277))
    def test_putIntLn_wrong_para(self):
        """test_putIntLn_wrong_para"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                putIntLn(sdgfdfgg);
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,278))
    def test_getFloat(self):
        """test_getFloat"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                getFloat();
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,279))
    def test_getFloat_wrong_para(self):
        """test_getFloat_wrong_para"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                getFloat(sdgfdfgg);
            end"""
        expect='Error on line 4 col 25: sdgfdfgg'
        self.assertTrue(TestParser.test(input,expect,280))
    def test_putFloat(self):
        """test_putFloat"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                putFloat(23.454);
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,281))
    def test_putFloat_wrong_para(self):
        """test_putFloat_wrong_para"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                putFloat();
            end"""
        expect='Error on line 4 col 25: )'
        self.assertTrue(TestParser.test(input,expect,282))
    def test_putFloatLn(self):
        """test_putFloatln"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                putFloatLn(23.454);
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,283))
    def test_putFloatln_wrong_para(self):
        """test_putFloatln_wrong_para"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                putFloatLn();
            end"""
        expect='Error on line 4 col 27: )'
        self.assertTrue(TestParser.test(input,expect,284))
    
    def test_putBool(self):
        """test_putBool"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                putBool(true);
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,285))
    def test_putBool_wrong_para(self):
        """test_putBool_wrong_para"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                putBool();
            end"""
        expect='Error on line 4 col 24: )'
        self.assertTrue(TestParser.test(input,expect,286))

    def test_putBoolLn(self):
        """test_putBoolln"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                putFloatLn(false);
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,287))
    def test_putBoolln_wrong_para(self):
        """test_putBoolLn_wrong_para"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                putBoolLn();
            end"""
        expect='Error on line 4 col 26: )'
        self.assertTrue(TestParser.test(input,expect,288))

    def test_putString(self):
        """test_putString"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                putString(abcdf);
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,289))

    def test_putStringLn(self):
        """test_putStringln"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                putStringLn(dffgfghg);
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,290))
   
    def test_putString_wrong_para(self):
        """test_putString_wrong_para"""
        input= """procedure built_in();
        var x , y : real ; 
            begin
                putString();
            end"""
        expect='Error on line 4 col 26: )'
        self.assertTrue(TestParser.test(input,expect,291))
    
    #Test Index Expression
    def test_index_expr_simple(self):
        """test_index_expr_simple"""
        input= """procedure index_expr();
         
            begin
              c := a[3];
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,292))
    def test_index_expr_compl(self):
        """test_index_expr_compl"""
        input= """procedure index_expr();
         
            begin
              c := a[b[2]] +3;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,293))
    def test_index_expr_miss_RSB(self):
        """test_index_expr_miss_RSB"""
        input= """procedure index_expr();
         
            begin
              c := a[b[2] +3;
            end"""
        expect='Error on line 4 col 28: ;'
        self.assertTrue(TestParser.test(input,expect,294))
    def test_index_expr_null_body(self):
        """test_index_expr_null_body"""
        input= """procedure index_expr();
         
            begin
              c := a[] +3;
            end"""
        expect='Error on line 4 col 21: ]'
        self.assertTrue(TestParser.test(input,expect,295))
    def test_index_expr_with_assign_simple(self):
        """test_index_expr_with_assign_simple"""
        input= """procedure index_expr();
            begin
             foo() := a[b[2]] +3;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,296))
    def test_index_expr_with_assign_compl(self):
        """test_index_expr_with_assign_compl"""
        input= """procedure index_expr();
            begin
             foo(2)[3+x] := a[b[2]] +3;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,297))
   
    def test_using_sub(self):
        """test_using_sub"""
        input= """procedure built_in();
        var x , y : real ; 
            d : array [ 1-1 .. 1+1 ] of integer ;
            begin
                x := 2;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,298))
    #test full program
    def test_full_program(self):
        """test full program"""
        input= """var i : integer ;
                    function f () : integer ;
                        begin
                            return 200;
                        end
                    procedure main () ;
                    var
                         main : integer ;
                    begin
                        main := f () ;
                        putIntLn ( main ) ;
                         with
                            i : integer ;
                            main : integer ;
                            f : integer ;
                        do begin
                            main := f := i := 100 ;
                            putIntLn ( i ) ;
                            putIntLn ( main ) ;
                            putIntLn ( f ) ;
                        end
                        putIntLn ( main ) ;
                    end
                    var g : real ;"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,299))

    