import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    #ID 
    def test_identifier(self):
       """test identifiers"""
       self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
       self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
       self.assertTrue(TestLexer.test("aAsVN","aAsVN,<EOF>",103))
       self.assertTrue(TestLexer.test("_Abc1","_Abc1,<EOF>",104))
       self.assertTrue(TestLexer.test("_123 a_123 1_2adv","_123,a_123,1,_2adv,<EOF>",105))
       self.assertTrue(TestLexer.test("1abc","1,abc,<EOF>",106))
       
    
    #Comment
    def test_comment(self):
        """test comment"""
        self.assertTrue(TestLexer.test("""//Comment the single comment""","""<EOF>""", 107))
        self.assertTrue(TestLexer.test("(**) input","input,<EOF>", 108))
        self.assertTrue(TestLexer.test("{*dsffff*} input","input,<EOF>", 109))
        self.assertTrue(TestLexer.test("(*comment ne )*nest ne*) end *) abcxyz","""end,*,),abcxyz,<EOF>""", 110))
        self.assertTrue(TestLexer.test("""//sdgdfg (*hello*)
            comment the single line""", """comment,the,single,line,<EOF>""", 111))
        self.assertTrue(TestLexer.test("{*comment // comment line*} input","input,<EOF>", 112))
        self.assertTrue(TestLexer.test("""(*
                                    * Duc
                                    * Tran
                                    * 
                                    *
                                    *
                                    *
                                    *)  int main""","""int,main,<EOF>""", 113))
        self.assertTrue(TestLexer.test("{*comment // comment line*} input","input,<EOF>", 114))
    #Keywords
    def test_keyword(self):
        """test keywords"""
        self.assertTrue(TestLexer.test("""
        breaK Else return
            ""","""breaK,Else,return,<EOF>""",115))
        self.assertTrue(TestLexer.test("""break else return false abdf""","""break,else,return,false,abdf,<EOF>""", 116))
        self.assertTrue(TestLexer.test("""
        BreaK break return
            ""","""BreaK,break,return,<EOF>""",117))
        self.assertTrue(TestLexer.test("""
        continue for to downto CoNtinuE
            ""","""continue,for,to,downto,CoNtinuE,<EOF>""",118))
        
        
   # Test Operator
    def test_operator(self):
        """test operator"""
        self.assertTrue(TestLexer.test("""a=b+c*d/10""","""a,=,b,+,c,*,d,/,10,<EOF>""", 119))
        self.assertTrue(TestLexer.test("""not hey  or    mod""","""not,hey,or,mod,<EOF>""", 120))
        self.assertTrue(TestLexer.test(""": =""",""":,=,<EOF>""", 121))
        self.assertTrue(TestLexer.test(""">==""",""">=,=,<EOF>""", 122))
        self.assertTrue(TestLexer.test("""> ==""",""">,=,=,<EOF>""", 123))
        self.assertTrue(TestLexer.test("""=<>==""","""=,<>,=,=,<EOF>""", 124))
        self.assertTrue(TestLexer.test("""=<=<==""","""=,<=,<=,=,<EOF>""", 125))
        self.assertTrue(TestLexer.test("""x := -3;""","""x,:=,-,3,;,<EOF>""", 126))
        self.assertTrue(TestLexer.test(' ::= ',':,:=,<EOF>',127))
        self.assertTrue(TestLexer.test(" - 8000","-,8000,<EOF>",128))
        self.assertTrue(TestLexer.test(" --8000","-,-,8000,<EOF>",129))
        
    #Seperator
    def test_seperator(self):
        """test seperator"""
        self.assertTrue(TestLexer.test("""integer a[5];
    There are many, people ..""","""integer,a,[,5,],;,There,are,many,,,people,..,<EOF>""", 130))
        self.assertTrue(TestLexer.test("""var () main""","""var,(,),main,<EOF>""", 131))
        self.assertTrue(TestLexer.test(""";;[[..:=""",""";,;,[,[,..,:=,<EOF>""", 132))
        self.assertTrue(TestLexer.test("""{he } main d""","""main,d,<EOF>""", 133))
    # INTLIT
    def test_intlit(self):
        """test intlit"""
        self.assertTrue(TestLexer.test("a=1000", "a,=,1000,<EOF>", 134))
        self.assertTrue(TestLexer.test("-1000", "-,1000,<EOF>", 135))
        self.assertTrue(TestLexer.test("-++++++1000", "-,+,+,+,+,+,+,1000,<EOF>", 136))
    # FLOATLIT
    def test_floatlit(self):
       """test FLOATLIT"""
       self.assertTrue(TestLexer.test("1.2", "1.2,<EOF>", 137))
       self.assertTrue(TestLexer.test("1.", "1.,<EOF>", 138))
       self.assertTrue(TestLexer.test(".1", ".1,<EOF>", 139))
       self.assertTrue(TestLexer.test("1e2", "1e2,<EOF>", 140))
       self.assertTrue(TestLexer.test("1.2E-2", "1.2E-2,<EOF>", 141))
       self.assertTrue(TestLexer.test("9.0", "9.0,<EOF>", 142))
       self.assertTrue(TestLexer.test("12e8", "12e8,<EOF>", 143))
       self.assertTrue(TestLexer.test("0.33E-3", "0.33E-3,<EOF>", 144))
       self.assertTrue(TestLexer.test("128e-42", "128e-42,<EOF>", 145))
       self.assertTrue(TestLexer.test("e-12", "e,-,12,<EOF>", 146))
       self.assertTrue(TestLexer.test("143e", "143,e,<EOF>", 147))
       self.assertTrue(TestLexer.test("""1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42""", """1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,<EOF>""", 148))
       self.assertTrue(TestLexer.test("e-12", "e,-,12,<EOF>", 149)) 
       self.assertTrue(TestLexer.test("23e", "23,e,<EOF>", 150))
       self.assertTrue(TestLexer.test( "1.e2","""1.e2,<EOF>""",151))

       
    #boolean literal
    def test_booleanlit(self):
        self.assertTrue(TestLexer.test("true false hello", "true,false,hello,<EOF>", 152))
        self.assertTrue(TestLexer.test("True False hello", "True,False,hello,<EOF>", 153))
        self.assertTrue(TestLexer.test("TrueFalse hello", "TrueFalse,hello,<EOF>", 154))
        self.assertTrue(TestLexer.test(" hello = Fasle", "hello,=,Fasle,<EOF>", 155))
    
    def test_integer(self):
       """test integers"""
       self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",156))
       self.assertTrue(TestLexer.test("a = 1000;","a,=,1000,;,<EOF>",157))
       self.assertTrue(TestLexer.test(" -5000","-,5000,<EOF>",158))
       self.assertTrue(TestLexer.test(" - 8000","-,8000,<EOF>",159))
       self.assertTrue(TestLexer.test(" --8000","-,-,8000,<EOF>",160))

    def test_stringlit(self):
        """test stringlit"""
        self.assertTrue(TestLexer.test(' "hello" ','hello,<EOF>',161))
        
        self.assertTrue(TestLexer.test("""abc""","""abc,<EOF>""", 162))
        self.assertTrue(TestLexer.test('"hell okkk asd"',"hell okkk asd,<EOF>",163))
        self.assertTrue(TestLexer.test(' "hello i am duc" ','hello i am duc,<EOF>',164))
        self.assertTrue(TestLexer.test('sdfgf "hello i am duc" ','sdfgf,hello i am duc,<EOF>',165))
        self.assertTrue(TestLexer.test('sdfgf "hello i am duc" hello ','sdfgf,hello i am duc,hello,<EOF>',166))
        self.assertTrue(TestLexer.test('"0234fdfg i am duc" hello ','0234fdfg i am duc,hello,<EOF>',167))
       
    ### Test UNCLOSE_STRING
    def test_error_string(self):
        self.assertTrue(TestLexer.test(""" "assaf ""","Unclosed String: assaf ",168))
        self.assertTrue(TestLexer.test(""" "abc  x ""","""Unclosed String: abc  x """,169))
        self.assertTrue(TestLexer.test(""" sdfhdshj'abc""","""sdfhdshj,Error Token '""",170))
        self.assertTrue(TestLexer.test(" "".""","Error Token .",171))
        self.assertTrue(TestLexer.test(""" " a = true


                " ""","""Unclosed String:  a = true""",172))
        self.assertTrue(TestLexer.test(" \" abc","""Unclosed String:  abc""",173))
        self.assertTrue(TestLexer.test(""" " abcd \ " ""","""Illegal Escape In String:  abcd \ """,174))
        self.assertTrue(TestLexer.test( """ "thong \n" ""","""Unclosed String: thong """,175))
        self.assertTrue(TestLexer.test(""""abc""",'Unclosed String: abc',176))
        self.assertTrue(TestLexer.test( """ "abcd\txyz" ""","""abcd	xyz,<EOF>""",177))
        self.assertTrue(TestLexer.test("""" 123\t45" """,
        """ 123	45,<EOF>""",178))
        self.assertTrue(TestLexer.test( """ "abcd\bxyz" ""","""abcdxyz,<EOF>""",178))
    # test additional
    def test_additional(self):
        self.assertTrue(TestLexer.test( "32132. .32132 1.2857342594587432E-10","32132.,.32132,1.2857342594587432E-10,<EOF>",179))
        self.assertTrue(TestLexer.test( """ "abc
        efg" ""","""Unclosed String: abc""",180))
        #self.assertTrue(TestLexer.test( """ "abc\ a" ""","""Illegal Escape In String: abc\""",181))
        self.assertTrue(TestLexer.test( """ "abc\n\t\a" ""","""Unclosed String: abc""",182))
        self.assertTrue(TestLexer.test( """ (*
                    ***#$@$#@$#@$!\t\n\afd
                      *) ""","""<EOF>""",183))
        self.assertTrue(TestLexer.test( """ 4382487324032247834932 ""","""4382487324032247834932,<EOF>""",184))
        self.assertTrue(TestLexer.test( """int a = 0000""","""int,a,=,0000,<EOF>""",185))
        self.assertTrue(TestLexer.test( """32132. .32132 1.2857342594587432E-10""","""32132.,.32132,1.2857342594587432E-10,<EOF>""",186))
        self.assertTrue(TestLexer.test("""
                   	// start declaration part
                   	int a ,b, c ;
                   	float f [ 5 ] ;
                   	//end declaration part

                   	// start statement part
                   	a=b=2;
                   	if (a=b) f [0]=1.0;
                   	//end statement part
                   ""","""int,a,,,b,,,c,;,float,f,[,5,],;,a,=,b,=,2,;,if,(,a,=,b,),f,[,0,],=,1.0,;,<EOF>""",187))
        self.assertTrue(TestLexer.test( """boolean b; // a variable of type boolean
                   int i; // a variable of type int
                   float f; // a variable of type float
                   boolean ba[5]; // a variable of type array on boolean
                   int ia[3]; // a variable of type array on int
                   float fa[100]; // a variable of type array on float
                   int i=5; //no initialization => int i;
                   float f[]; //must have size => float f[5];
                   boolean boo[2]=true,false; //no initialization => boolean boo[2];""","""boolean,b,;,int,i,;,float,f,;,boolean,ba,[,5,],;,int,ia,[,3,],;,float,fa,[,100,],;,int,i,=,5,;,float,f,[,],;,boolean,boo,[,2,],=,true,,,false,;,<EOF>""",188))
        self.assertTrue(TestLexer.test("""  float foo() 
          return foo(2)[arr[]]="string with number 123 + 125235e-369;
        ""","""float,foo,(,),return,foo,(,2,),[,arr,[,],],=,Unclosed String: string with number 123 + 125235e-369;""",189))
        self.assertTrue(TestLexer.test( "{ ~ [","""Error Token {""",190))
        self.assertTrue(TestLexer.test( """booleans breaks continues elses fors floats ifs ints returns""","""booleans,breaks,continues,elses,fors,floats,ifs,ints,returns,<EOF>""",191))
        self.assertTrue(TestLexer.test( """143e3""","""143e3,<EOF>""",192))
        self.assertTrue(TestLexer.test( """a > b < c;""","""a,>,b,<,c,;,<EOF>""",193))
        self.assertTrue(TestLexer.test( """boolean a[]""","""boolean,a,[,],<EOF>""",194))
        self.assertTrue(TestLexer.test( """// Xin chao Viet Nam  \a \b \t \t \b\a  123 abc  xin chao""","""<EOF>""",195))
        self.assertTrue(TestLexer.test( """ 
                                // abcxyz 123abc
                                PPL is very difficult" are you ready?
                                Val a=b;
                                ""","""PPL,is,very,difficult,Unclosed String:  are you ready?""",196))
        self.assertTrue(TestLexer.test(""" 
                ____
                _a1a1a1
                a_1_a_b_4
                A_a_1
                1_A
                ""","""____,_a1a1a1,a_1_a_b_4,A_a_1,1,_A,<EOF>""",197))
        self.assertTrue(TestLexer.test( """4^5^5^5""","""4,Error Token ^""",198))
        self.assertTrue(TestLexer.test( """ "123\f45" ""","""12345,<EOF>""",199))