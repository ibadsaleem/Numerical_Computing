from math import *;
from sympy import *

from Equation import Expression
import os
FIXEDDIGITS = 10;

def fact(num):
	if(num <= 1):
		return 1;
	return num * fact(num-1);



glob_table =[];
glob_object = {};

def getdigits(exp):
	num= 0;
	while(exp != 1.0):
		exp = exp *10;
		num=num+1;
	return num;
	
class CALCULUS:
	def __init__(self , eq , var):
		self.stringeq = eq;
		self.inputvar = var;
		pass;
		
	def equation(self,a):
		fn = Expression(self.stringeq,[self.inputvar]);
		return round(fn(a) , FIXEDDIGITS);	


def get_input():
	n = int(input("enter number of inputs"));
	res = [[],[]];
	for i in range(0,n):
		res[0].append(float(input("enter x" + str(i) + "  = ")));
		res[1].append(float(input("enter fx(" + str(i) + ")  = ")));
	return res;
	

	
	
	

class THREE_POINT_DIFFERENTIATION:
	def __init__(self):
		self.vars = ""
		self.point = 0.0;
		self.eq = ""
		pass;
	
	def seteq(self):
		if(self.vars == "" and self.eq == ""):
			self.vars = input("enter variables = ");
			self.eq= input("enter equation = ");
		else:
			x = input("Same equation?")
			if(x == "Y" or x == "y"):
				pass;
			else:
				self.vars = input("enter variables = ");
				self.eq= input("enter equation = ");	
	def midpoint(self ):
		self.seteq();
		c = CALCULUS(self.eq , self.vars);
		x0 = float(input("x0 = "));
		self.point = x0;
		h = float(input("h = "));
		return (c.equation(x0+h) - c.equation(x0-h)) / (2*h);	
	
	def endpoint(self ):
		self.seteq();
		c = CALCULUS(self.eq , self.vars);
		x0 = float(input("x0 = "));
		self.point = x0;
		h = float(input("h = "));
		return (	(-3*(c.equation(x0))) + ( 4 * c.equation(x0+h)) +  (-1 * c.equation(x0+(2*h)) )  )/(2*h) 
		
		pass;
		
class FIVE_POINT_DIFFERENTIATION:
	
	def __init__(self):
		self.vars = ""
		self.eq = ""
		self.point = 0.0;
		pass;
	def seteq(self):
		if(self.vars == "" and self.eq == ""):
			self.vars = input("enter variables = ");
			self.eq= input("enter equation = ");
		else:
			x = input("Use equation last used in this method ? ")
			if(x == "Y" or x == "y"):
				pass;
			else:
				self.vars = input("enter variables = ");
				self.eq= input("enter equation = ");	
		
	def midpoint(self):
		self.seteq();
		c = CALCULUS(self.eq , self.vars);
		x0 = float(input("x0 = "));
		self.point = x0;
		h = float(input("h = "));
		return (c.equation(x0-(2*h))  -(c.equation(x0-h)  * 8) +(c.equation(x0+h)  * 8) - c.equation(x0+(2*h))   )/ (12*h);
	def endpoint(self ):
		self.seteq();
		c = CALCULUS(self.eq , self.vars);
		x0 = float(input("x0 = "));
		self.point = x0;
		h = float(input("h = "));
		return ((-25*c.equation(x0)) + (48 * c.equation(x0+h)) + (-36 * c.equation(x0+(2*h))) + (16 * c.equation(x0 + (3*h))) + (-3 * c.equation(x0 + (4*h)))	)/(12 * h) ; 
		
			

class TRAPEZONIAL_INTEGRATION:
	def seteq(self):
		if(self.vars == "" and self.eq == ""):
			self.vars = input("enter variables = ");
			self.eq= input("enter equation = ");
			self.lb = 0.0
			self.hb = 0.0
		else:
			x = input("Use equation last used in this method ? ")
			if(x == "Y" or x == "y"):
				pass;
			else:
				self.vars = input("enter variables = ");
				self.eq= input("enter equation = ");	
		
	def __init__(self ):
		self.eq = ""
		self.vars = "";
		
	def solve(self):
		self.seteq();
		c = CALCULUS(self.eq , self.vars);
		lower = float(eval(input("enter lower limit a = ")));
		self.lb = lower;
		upper = float(eval(input("enter upper  limit b = ")))
		self.hb = upper; 
		n = float(input("enter value of n"))
		h = float((upper-lower)/n);
		sum = 0;
        
		sum =  sum + c.equation(lower);
		lower = lower+h
		while(round(lower , 5) != round(upper, 5)):
				
				
				sum = sum +(2* c.equation(lower));
				lower = lower + h;
		sum =  sum + c.equation(upper);
		
		return (sum*h)/2;
		
		
class SIMPSON_INTEGRATION:
	
	def seteq(self):
		if(self.vars == "" and self.eq == ""):
			self.vars = input("enter variables = ");
			self.eq= input("enter equation = ");
			self.lb = 0.0
			self.hb = 0.0
		else:
			x = input("Use equation last used in this method ? ")
			if(x == "Y" or x == "y"):
				pass;
			else:
				self.vars = input("enter variables = ");
				self.eq= input("enter equation = ");	
		
	def __init__(self ):
		self.eq = ""
		self.vars = "";
		
	def solveonethird(self):
		self.seteq();
		c = CALCULUS(self.eq , self.vars);
		lower = float(eval(input("enter lower limit a = ")));
		self.lb = lower;
		upper = float(eval(input("enter upper  limit b = ")))
		self.hb = upper; 
		n = float(input("enter value of n"))
		h = float((upper-lower)/n);
		sum = 0;
		sum =  sum + c.equation(lower);
		lower = lower+h
		mod = 0;
		while(round(lower , 5) != round(upper, 5)):
				if(mod % 2 == 0):
					sum = sum +(4* c.equation(lower));
				
					
				else:
					sum = sum +(2* c.equation(lower));
					
				lower = lower + h;
				mod = mod +1;
		
		sum =  sum + c.equation(upper);
		
		return (sum*h)/3;
	
	def solvethreeeighth(self):
		self.seteq();
		c = CALCULUS(self.eq , self.vars);
		lower = float(eval(input("enter lower limit a = ")));
		self.lb= lower;
		upper = float(eval(input("enter upper  limit b = ")))
		self.hb = upper; 
		n = float(input("enter value of n"))
		h = float((upper-lower)/n);
		sum = 0;
		sum =  sum + c.equation(lower);
		lower = lower+h
		mod = 0;
		while(round(lower , 5) != round(upper, 5)):
				if(mod % 3 == 0):
					print(2);
					sum = sum +(2* c.equation(lower));
				else:
					print(3);
					sum = sum +(3* c.equation(lower));
				lower = lower + h;
				mod = mod +1;
				
		
		sum =  sum + c.equation(upper);
		
		
		return (3/8)*(sum*h);	

		
test = SIMPSON_INTEGRATION()

class TrueValue:
    def __init__(self):
        pass;
    def calc(self , eq , var , h , l):
        eq=eq.replace("^" , "**");
        print("func = " + eq);
        x = symbols(var);
        expr = eval(eq).evalf();
        iexpr = integrate(expr,x);
        val1 = iexpr.subs([(x,h)]).evalf();
        val2 = iexpr.subs([(x,l)]).evalf();
        
        return (val1-val2);
        pass;
    def calc_diff(self, eq , var , at):
        eq=eq.replace("^" , "**");
        x = symbols(var);
        sp = var.split(" ");
        eq=eq.replace(sp[0] , "x");
        expr = eval(eq).evalf();
        iexpr = diff(expr,x);
        val1 = iexpr.subs([(x,at)]).evalf();
       
        
        return (val1);
    def calc_diff2(self, eq , var , at):
        eq=eq.replace("^" , "**");
        
        x,y= symbols(var);
        sp = var.split(" ");
        eq=eq.replace(sp[0] , "x");
        eq=eq.replace(sp[1] , "y");
			
        expr = eval(eq).evalf();
        #iexpr = eval(diff(expr ,x)expr,x,y);
        print(iexpr);
        val1 = iexpr.subs([(x,at) ] ).evalf();
       
        
        return (val1);
    
   
    
class FUNCHANDLER:
    def __init__(self):
        self.threepoints = THREE_POINT_DIFFERENTIATION();
        self.fivepoints = FIVE_POINT_DIFFERENTIATION();
        self.trapezonial = TRAPEZONIAL_INTEGRATION();
        self.simpson = SIMPSON_INTEGRATION();
        self.accurate = TrueValue();
        self.vars= "";
        self.eq = "";
        pass;

                
    def threepointmidpoint(self):
        sol = self.threepoints.midpoint();
        acc = self.accurate.calc_diff(self.threepoints.eq ,self.threepoints.vars , self.threepoints.point  );
        print("f`(x) = " + str(sol)  );
        print("true error" + str(round( abs(acc - sol) , 7)));
        
        pass;
    
    def threepointend(self):
        sol = self.threepoints.endpoint();
        acc = self.accurate.calc_diff(self.threepoints.eq ,self.threepoints.vars , self.threepoints.point  );
        print("f`(x) = " + str(sol)  );
        print("true error" + str(round( abs(acc - sol) , 7)));
        pass;
    def fivepointend(self):
        sol = self.fivepoints.endpoint();
        acc = self.accurate.calc_diff(self.fivepoints.eq ,self.fivepoints.vars , self.fivepoints.point  );
        print("f`(x) = " + str(sol)  );
        print("true error" + str(round( abs(acc - sol) , 7)));
        pass;
    def fivepointmidpoint(self):
        sol = self.fivepoints.midpoint();
        acc = self.accurate.calc_diff(self.fivepoints.eq ,self.fivepoints.vars , self.fivepoints.point  );
        print("f`(x) = " + str(sol)  );
        print("true error" + str(round( abs(acc - sol) , 7)));
        pass;
    def trapezonialintegration(self):
        sol = self.trapezonial.solve();
        print("intg(f(x)) = " + str(sol));
        print("lower = " + str(self.trapezonial.lb ) + "   upper = " + str(self.trapezonial.hb) );
        acc = self.accurate.calc(self.trapezonial.eq , self.trapezonial.vars ,self.trapezonial.hb , self.trapezonial.lb );
        print("acc = " + str(acc));
        print("true error = " + str(round( abs(acc - sol) , 7)) );
        pass;
    def simpsonintegration13rd(self):
        sol = self.simpson.solveonethird();
        print("intg(f(x)) = " + str(sol));
        print("lower = " + str( self.simpson.lb ) + "   upper = " + str( self.simpson.hb) );
        acc = self.accurate.calc( self.simpson.eq , self.simpson.vars , self.simpson.hb ,  self.simpson.lb );
        print("acc = " + str(acc));
        print("true error = " + str(round( abs(acc - sol) , 7)) );
        pass;
    def simpsonintegration38th(self):
        sol = self.simpson.solvethreeeighth();
        print("intg(f(x)) = " + str(sol));
        print("lower = " + str( self.simpson.lb ) + "   upper = " + str( self.simpson.hb) );
        acc = self.accurate.calc( self.simpson.eq , self.simpson.vars , self.simpson.hb ,  self.simpson.lb );
        print("acc = " + str(acc));
        print("true error = " + str(round( abs(acc - sol) , 7)) );
        pass;
   

def spaces(a):
	str1 = "";
	for i in range(0 , 20-len(str(a))):
		str1 = str1 + " ";
	str1 = str1 + str(a);
	return 	str1;



def format_output(a , b , c , fa , fb, fc , error):
	str1 = "";
	str1 = str1 + spaces(a);
	str1 = str1 + spaces(b);
	str1 = str1 + spaces(c);
	str1 = str1 + spaces(fa);
	str1 = str1 + spaces(fb);
	str1 = str1 + spaces(fc);
	str1 = str1 + spaces(error);
	print(str1);
	
	

def format_print(a , b , c , fa , fb, fc , error):
	
	str1 = "";
	str1 = str1 + spaces(a);
	str1 = str1 + spaces(b);
	str1 = str1 + spaces(c);
	str1 = str1 + spaces(fa);
	str1 = str1 + spaces(fb);
	str1 = str1 + spaces(fc);
	str1 = str1 + spaces(error);
	print(str1);
	
	
	 
			
	    

class NUMERICALCOMPUTING:
    
	def equation(self,a):
        
		fn = Expression(self.stringeq,[self.inputvar]);
		return fn(a);
		
	def derivative(self , a):
		return 0;			#derivative here
	
	def __init__(self , var , eq):
		self.inputvar = var
		self.stringeq = eq
		pass;
	
	
	def bisection(self,lowerval , upperval , t_level ):
		res = 0;
		nitr = 0;
		try:	
			a = lowerval;
			b = upperval;
			c = (a + b)/2;
			res = c;
			prev_value = 0;
			print(self.equation(c));
			new_value = round(self.equation(c ) , FIXEDDIGITS);
			if(self.equation(a) * self.equation(b)   > 0):
				raise ValueError;
			format_print("      a" ,"b", "c", "f(a)" , "f(b)", "f(c)" ,"abs.error" );
			print("");
			while(abs(new_value - prev_value) > t_level):
				a_value=round(self.equation(a) , getdigits(t_level));
				b_value = round(self.equation(b) , getdigits(t_level));
				
				format_print(a ,b, c, a_value , b_value , new_value ,abs(round(new_value - prev_value , FIXEDDIGITS)) );
				#print("a =  " + str(a) + " b = " + str(b) + " c = " + str(c) + "  f(a)="+ str(a_value) + "  f(b)=" + str(b_value)+ "	f (c) = " + str(new_value ) +"  error=" + str(abs(round(new_value - prev_value , FIXEDDIGITS))) );
				
				nitr=nitr+1;
				prev_value = new_value;
				if(new_value < 0 and self.equation(a) < 0):
					#substitute a
					a = round(c, getdigits(t_level)+1);
				elif(new_value < 0 and self.equation(b) < 0):
					#substitute b
					b= round(c , getdigits(t_level)+1);
				elif(new_value > 0 and self.equation(a) > 0):
					#substitute a
					a=round(c , getdigits(t_level)+1);
				elif(new_value > 0 and  self.equation(b) > 0):
					#substitute b
					b = round(c , getdigits(t_level)+1);
				res = c;		
				c = (a+b)/2;
				c = round(c , getdigits(t_level)+1);
				new_value = round(self.equation(c ) , getdigits(t_level)+1);
			print("number of iterations = " + str(nitr));
			print("\nSolution = " + str(res));
			#return list(res , nitr ,abs(new_value - prev_value));	
		except ValueError:
			
			print("f(" + str(lowerval) + ") = " + str(self.equation(lowerval)) +   "  f(" + str(upperval) + ") = " + str(self.equation(upperval)) );
			print("\n\tsolution donot exist in this range must meet condition f(a)*fb(b) < 0\n");
		else:
			print("\nSolution = " + str(res));	
			print("");
			
			
	
			
	def regular_falsi(self,lowerval , upperval , t_level):
		res = 0;
		nitr = 0;
		try:	
			a = lowerval;
			b = upperval;
			c = round((a*self.equation(b)-b*self.equation(a))/(self.equation(b)-self.equation(a)) , getdigits(t_level)+1);
			res = round(c,getdigits(t_level)+1);
			prev_value = 0;
			new_value = round(self.equation(c ) , getdigits(t_level)+1);
			if(self.equation(a) * self.equation(b)   > 0):
				raise ValueError;
			format_print("      a" ,"b", "c", "f(a)" , "f(b)", "f(c)" ,"abs.error" );
			print("");
			while(abs(new_value - prev_value) > t_level):
				a_value=round(self.equation(a) , getdigits(t_level));
				b_value = round(self.equation(b) , getdigits(t_level));
				format_print(a ,b, c, a_value , b_value , new_value ,abs(round(new_value - prev_value , FIXEDDIGITS)) );
				#print("a =  " + str(a) + " b = " + str(b) + " c = " + str(c) + "  f(a)="+ str(a_value) + "  f(b)=" + str(b_value)+ "	f (c) = " + str(new_value ) +"  error=" + str(abs(round(new_value - prev_value , FIXEDDIGITS))) );
				
				nitr=nitr+1;
				prev_value = new_value;
				if(new_value < 0 and self.equation(a) < 0):
					#substitute a
					a = round(c , getdigits(t_level)+1);
				elif(new_value < 0 and self.equation(b) < 0):
					#substitute b
					b= round(c , getdigits(t_level)+1);
				elif(new_value > 0 and self.equation(a) > 0):
					#substitute a
					a=round(c , getdigits(t_level)+1);
				elif(new_value > 0 and  self.equation(b) > 0):
					#substitute b
					b = round(c , getdigits(t_level)+1);
				res = c;		
				c = round((a*self.equation(b)-b*self.equation(a))/(self.equation(b)-self.equation(a)) , getdigits(t_level)+ 1);
				new_value = round(self.equation(c ) , getdigits(t_level)+1);
			print("number of iterations = " + str(nitr));
			print("\nSolution = " + str(res));
			return [res , nitr ,abs(new_value - prev_value)];
		except ValueError:
			print("f(" + str(lowerval) + ") = " + str(self.equation(lowerval)) +   "  f(" + str(upperval) + ") = " + str(self.equation(upperval)) );
			print("\n\tsolution donot exist in this range must meet condition f(a)*fb(b) < 0");
		else:
			print("Solution = " + str(res));	
			
		
		
	def secant_method(self,lowerval , upperval , t_level):
		res = 0;
		dig = getdigits(t_level)+1;
		nitr=0;
		try:	
			a = lowerval;
			b = upperval;
			c = round((a*self.equation(b)-b*self.equation(a))/(self.equation(b)-self.equation(a)) , dig);
			res = c;
			prev_value = 0;
			new_value = round(self.equation(c ) , dig);
			format_print("      a" ,"b", "c", "f(a)" , "f(b)", "f(c)" ,"abs.error" );
			print("");
			while(abs(new_value - prev_value) > t_level):
				a_value=round(self.equation(a) , getdigits(t_level));
				b_value = round(self.equation(b) , getdigits(t_level));
				#print("a =  " + str(a) + " b = " + str(b) + " c = " + str(c) + "  f(a)="+ str(a_value) + "  f(b)=" + str(b_value)+ "	f (c) = " + str(new_value ) +"  error=" + str(abs(round(new_value - prev_value , FIXEDDIGITS))) );
				format_print(a ,b, c, a_value , b_value , new_value ,abs(round(new_value - prev_value , FIXEDDIGITS)) );
				nitr=nitr+1;
				#print("a =  " + str(a) + " b = " + str(b) + " c = " + str(c) + "	f (c) = " + str(new_value)+"  error=" + str(abs(round(new_value - prev_value , FIXEDDIGITS))));
				prev_value = new_value;
				a = b;
				b = c;
				res = c;		
				c = round((a*self.equation(b)-b*self.equation(a))/(self.equation(b)-self.equation(a)) , dig);
				new_value = round(self.equation(c ) , dig);
			print("number of iterations = " + str(nitr));
			print("\nSolution = " + str(res));
			return [res , nitr , abs(new_value - prev_value)];
		except ValueError:
			print("solution donot exist in this range");
		else:
			print("Solution = " + str(res));	
					



class LAGRANGECOMPUTING:
	
	coof = [];
	def equation(self,a):
        
		fn = Expression(self.stringeq,[self.inputvar]);
		return fn(a);
	
	def getfromtable(self , a):
		return self.table[self.values[a]];
	
	def __init__(self,tablevalues , istable , eq , var):
		self.stringeq = eq;
		self.inputvar = var;
		self.values = [];
		self.table ={};
		if(istable):
			self.table = tablevalues;
			for x in tablevalues:
				self.values.append(x);
			print(self.values);
		else:
			self.values = tablevalues;
			for val in self.values:
				self.table[val] = self.equation(val);
		print(self.table);	
	def lagrange_approximate_at(self,val , degree , istable):
		try:
			if(degree >= len(self.table)):
				print("err 1");
				raise ValueError;
			res = 0;
			#set array here hamza
			if(val >  float(max(self.values)) or val < float(min(self.values))):
				raise ValueError;
			newarr = [];
			tpoint =0 ;
			for i in range(0 , len(self.values)):
				if(val >= float(self.values[tpoint]) and val <= float(self.values[tpoint+degree])):
					for j in range(i , len(self.values)):
						newarr.append(self.values[j]);
					break;
				
				else:
					tpoint=tpoint+1;	
			self.values = newarr;
			#print("new values = " + str(self.values));
			
			for i in range(0,degree+1):
				r = round(self.get_lagrange_coof(val , i , degree) , FIXEDDIGITS);
				if(istable):	
					res = res + (r*round(self.getfromtable(i), FIXEDDIGITS  ));
				else:
					res = res + (r*round(self.equation(self.values[i]) , FIXEDDIGITS));
					print(round(self.equation(self.values[i]) , FIXEDDIGITS));
				print("");	
			print("\nsolution = " + str(res));
			return res;
			#working below
			#for P1 = Lof0 + L1f1
			
			
			
		except ValueError:
			print("too many values given or not given or value out of bound");	
		pass;
	def get_lagrange_coof(self,val , i , degree):
		res=  1;
		for j in  range(0 , degree+1):
			if(i != j):
				print("x = " + str(val) + "  x0 = " + str(self.values[i]) + "   x1/x2 = " + str(self.values[j]));
				res= res * (val-self.values[j])/(self.values[i]-self.values[j]);
		return res;		
		


class DDT:
	def __init__(self , tabledata):
		self.table = tabledata;
		#print(len(self.table[0]));
		pass;
	def approximate_ddt(self,val ):
		i = 1;
		while(len(self.table[len(self.table)-1]) != 1):
			print("\n");         
			
			self.create_ddt_columns(i);
			i = i+1;
		res = 0;
		for line in self.table:
			print(line);
		
		for j in range(1,len(self.table)-1):
			pr = 1;
			#print(str(pr) + " * " + str(self.table[j][0]))
			pr = pr * self.table[j][0];
			
			for k in range(1 , j):
				#print(str(pr) + " * " +str(val)+ "  -  " + str(self.table[0][k-1]) + "\n" );
			
				pr = pr * (round(val - self.table[0][k-1] , FIXEDDIGITS));
			res = res + pr;
	
		res = round(res,FIXEDDIGITS)
		print(res);	
		return res;
		
	def create_ddt_columns(self , i):	#i is 1 ddt or 2ddt
		col = i;
		res = [];
		jmp = i;
		for j in range(1,len(self.table[col])):
			
			result = (self.table[col][j] - self.table[col][j-1])/(self.table[0][j+jmp-1] - self.table[0][j-1]);
			#print(str(self.table[col][j]) + "-" + str(self.table[col][j-1]) + "  /   "   + str(self.table[0][j+jmp-1]) + "  -  "  + str(self.table[0][j-1]) );
			res.append(round(result , FIXEDDIGITS));
		self.table.append(res);			


class SDTbackward:
	def __init__(self , tabledata):
		self.table = tabledata;
		#print(len(self.table[0]));
		pass;
	def approximate_sdt(self,val ):
		i = 1;
		while(len(self.table[len(self.table)-1]) != 1):
			print("\n");         
			
			self.create_sdt_columns(i);
			i = i+1;
		res = 0;
		for line in self.table:
			print(line);
		#calcualte s  = x-x[0] / x[1]-x[0];
		s = (val-self.table[0][len(self.table[0])-1])/(self.table[0][1]-self.table[0][0]);
		print("s = " + str(s));
		#caluculate with forward diff formulae
		for j in range(0 , len(self.table)-1):
			pr = 1;
			pr = pr * self.get_backward_divided_difference(j);
			for k in range(0,j):
				pr = pr *  (s+k);
			pr = pr / fact(j);	
			res = res + pr;
		print(round(res , FIXEDDIGITS));	
		return res;
	
	def get_backward_divided_difference(self,pointat):
		if(pointat >= len(self.table)):
			print("there is an error");
			return 1;
		return self.table[pointat+1][len(self.table[pointat+1]) -1];		
			
	def create_sdt_columns(self , i):	#i is 1 ddt or 2ddt
		col = i;
		res = [];
		jmp = i;
		for j in range(1,len(self.table[col])):
			
			result = (self.table[col][j] - self.table[col][j-1]);
			#print(str(self.table[col][j]) + "-" + str(self.table[col][j-1])   );
			res.append(round(result , FIXEDDIGITS));
		self.table.append(res);			
		
	

class SDTforward:
	def __init__(self , tabledata):
		self.table = tabledata;
		#print(len(self.table[0]));
		pass;
	def approximate_sdt(self,val ):
		i = 1;
		while(len(self.table[len(self.table)-1]) != 1):
			print("\n");         
			
			self.create_sdt_columns(i);
			i = i+1;
		res = 0;
		for line in self.table:
			print(line);
		#calcualte s  = x-x[0] / x[1]-x[0];
		s = (val-self.table[0][0])/(self.table[0][1]-self.table[0][0]);
		#caluculate with forward diff formulae
		for j in range(0 , len(self.table)-1):
			pr = 1;
			pr = pr * self.get_forward_divided_difference(j);
			for k in range(0,j):
				pr = pr *  (s-k);
			pr = pr / fact(j);	
			res = res + pr;
		print(round(res , FIXEDDIGITS));	
		return res;
	
	def get_forward_divided_difference(self,pointat):
		if(pointat >= len(self.table)):
			print("there is an error");
			return 1;
		return self.table[pointat+1][0];		
			
	def create_sdt_columns(self , i):	#i is 1 ddt or 2ddt
		col = i;
		res = [];
		jmp = i;
		for j in range(1,len(self.table[col])):
			
			result = (self.table[col][j] - self.table[col][j-1]);
			#print(str(self.table[col][j]) + "-" + str(self.table[col][j-1])   );
			res.append(round(result , FIXEDDIGITS));
		self.table.append(res);			
		

class TRUEERROR:
	def __init__():
		pass;
	
	def equation(eq , val):
		pass;	
	def find_abs_error(eq , your_result , value ):
		return abs(your_result - equation(eq , value));
	
		
#x = input("enter variables = ");
#string = input("enter equation");
string = "";

x = "";

menu={
"firstscreen" : ["Chapter 2 methods" , "Chapter 3 methods" , "Chapter 4 methods" , "chapter 5 methods" , "clear screen" , "exit" ],
"chap2 methods" : ["bisection" , "Regular Falsi" , "secant method" , "Collective analysis"],
"chap3 method" : ["lagrange interpolation" , "newton divided difference" , "newton forward difference formulae" , "newton backward difference formulae" ],
"chapter 4" : ["three point end point differentiation" , "three point mid point differentiation" , "five point endpoint differentiation" , "five point mid point differentiation", "trapezonial integration" , "simpson integration 1/3rd" ,"simpson integration 3/8th"],
"chapter 5" : ["euler ODE" , "midpoint ODE" , "modified euler ODE"]	
};
	
	
	
def title():
	print("NC PROGRAM");
def print_choice(i):
	j=1;
	p="";
	counter=1;
	str1 = ""
	for x in menu:
		if(j==i):
			str1= x
			for items in menu[x]:
				print(str(counter) + ". " + items );
				counter=counter+1;
		j=j+1;	
		
	choose = int(input(">>> "));
	if(choose >= 0 and choose <= len(menu[str1])):
		return choose;
	return -1;	
			
def firstscreen():
	pass;



class CALCULATOR1:
	def __init__(self):
		pass;
	def calc(self , eq , var , a , b):
		eq=eq.replace("^" , "**");
		s = var.split(" ");
		x,y = symbols(var);
		eq = eq.replace(s[0] , "x");
		eq = eq.replace(s[1] , "y");
		
		expr = eval(eq).evalf();
		val = expr.subs([(x,a) , (y,b)]).evalf();
		return val;
		
class ODE:
	
	def format_table(self , table , method):
		print("x" + "  				" +   method)
		
		for entry in self.table:
			gaps= ""
			for i in range(0, 30-len(str(entry[0]))):
					gaps = gaps + " ";
			print(str(entry[0]) + gaps + str(entry[1]));
		
	
	def __init__(self):
		self.eq = "";
		self.vars = "";
		self.table = [];
		self.h=0.0;
		self.at = 0.0;
		self.x0 = 0.0;
		self.y0 = 0.0;
		self.equation= CALCULATOR1();
		
		
		pass
	
	def setvals(self):
		self.table = [];
		if(self.eq ==""):
			
			self.vars = input("variables = ");
			self.eq = input("equation = ");
			self.h = float(eval(input("h = ")));
			self.at =	float(eval(input("value at = ")));
			self.x0 = float(eval(input("x0 = ")));
			self.y0 = float(eval(input("y0 = ")));
		else:
			x = input("do you want to use last equation : ");
			if(x == "no" or x == "NO" or x == "n" or x =="N" ):
				self.vars = input("variables = ");
				self.eq = input("equation = ");
				self.h = float(eval(input("h = ")));
				self.at =	float(eval(input("value at = ")));
				self.x0 = float(eval(input("x0 = ")));
				self.y0 = float(eval(input("y0 = ")));
			else:
				self.h = float(eval(input("h = ")));
				self.at =	float(eval(input("value at = ")));
				self.x0 = float(eval(input("x0 = ")));
				self.y0 = float(eval(input("y0 = ")));
				pass;	
	def midpoint(self):
		self.setvals();
		print("func = " + self.eq);
		i = 0;
		self.table = []
		while(round(self.x0 ,10) != round(self.at , 10)):
			arr= [];
			val = self.equation.calc(self.eq , self.vars , self.x0 +(self.h/2) , self.y0 + ((self.h*(self.equation.calc(self.eq , self.vars , self.x0 , self.y0)))/2 ) 		);
			self.y0 = self.y0 + (self.h * val);
			self.x0 = self.x0+self.h;
			arr.append(round(self.x0 , FIXEDDIGITS));
			arr.append(round(self.y0, FIXEDDIGITS) );
			self.table.append(arr);
			
			pass;
		
		self.format_table(self.table , "midpoint");	
		print("\nat   " + str(self.table[len(self.table)-1][0] )   + "   y` is   "  +str(self.table[len(self.table)-1][1] ))
		
				
	def euler(self):
		
		self.setvals();
		
		print("func = " + self.eq);
		i = 0;
		
		while(round(self.x0 ,10) != round(self.at , 10)):
			arr= [];
			val = self.equation.calc(self.eq , self.vars , self.x0 , self.y0);
			self.y0 = self.y0 + (self.h * val);
			self.x0 = self.x0+self.h;
			arr.append(round(self.x0 , FIXEDDIGITS ));
			arr.append(round(self.y0 , FIXEDDIGITS));
			self.table.append(arr);
			pass;
		
		self.format_table(self.table , "euler");	
		print("\nat   " + str(self.table[len(self.table)-1][0] )   + "   y` is   "  +str(self.table[len(self.table)-1][1] ))
		#truev = TrueValue();
		#err = self.table[len(self.table)-1][1] - truev.calc_diff2(self.eq , self.vars , self.table[len(self.table)-1][0])
		
		
		pass;
	
	def modifiedeuler(self):
		self.setvals();
		
		print("func = " + self.eq);
		i = 0;
		
		while(round(self.x0 ,10) != round(self.at , 10)):
			arr= [];
			val = self.equation.calc(self.eq , self.vars , self.x0 , self.y0);
			self.y0 = self.y0 + ( (self.h/2) *( val + self.equation.calc(self.eq , self.vars , self.x0 + self.h , self.y0+  (self.h*	val			) 	)  					)  );
			self.x0 = self.x0+self.h;
			arr.append(round(self.x0 , FIXEDDIGITS ));
			arr.append(round(self.y0 , FIXEDDIGITS));
			self.table.append(arr);
			
			pass;
		
		self.format_table(self.table , "modified euler");	
		
		print("\nat   " + str(self.table[len(self.table)-1][0] )   + "   y` is   "  +str(self.table[len(self.table)-1][1] ))
		
		
		pass;			

class CALLER:
	def __init__(self):
		
		self.var = "";
		self.eq = "";
		self.table = {};
		pass;
	
	def take_input(self):
		self.var = input("Enter the variable : ");
		
		self.eq = input("Enter equation with the proper syntax :  ");
		
		
	def call_bisection(self):

		self.take_input();
		
		call = NUMERICALCOMPUTING(self.var , self.eq);
		
		lower = float(eval(input("enter value of a=")));
		
		upper= float(eval(input("enter value of b=")));
		t_d = float(input("enter tolerance value [t] 10^-[t] = (enter only t after minus sign) = "));
		t_d = 1/pow(10,t_d);
		#print("tolerance = "  + str(t_d));
		call.bisection(lower, upper,t_d);
		
		
	def call_regular_falsi(self):
		self.take_input();
		print(self.eq);
		call = NUMERICALCOMPUTING(self.var , self.eq);
	
		lower = float(eval(input("enter value of a=")));
		upper= float(eval(input("enter value of b=")));
		t_d = float(input("enter tolerance value [t] 10^-[t] = (enter only t after minus sign) = "));
		t_d = 1/pow(10,t_d);
		#print("tolerance = "  + str(t_d));
		call.regular_falsi(lower, upper,t_d);
		
		pass;
	def call_secant(self):
		self.take_input();
		print(self.eq);
		call = NUMERICALCOMPUTING(self.var , self.eq);
	
		lower = float(eval(input("enter value of a=")));
		
		upper= float(eval(input("enter value of b=")));
		t_d = float(input("enter tolerance value [t] 10^-[t] = (enter only t after minus sign) = "));
		t_d = 1/pow(10,t_d);
		#print("tolerance = "  + str(t_d));
		res = call.secant_method(lower,upper,t_d);
		pass;
	def create_table(self):
		self.table = {};
		n = int(input("how many entries to input >>> "));
		for i in range(0,n):
			x = float(input("x" + str(i) + " = "));
			self.table[x] = float(input("f(" + str(i) + ") = "));
			print(x-1);
		
	def lagrange_inter(self):
		inp = int(input("1)from table    2) from equation\n"));
		if(inp==1 or inp==2):
			if(inp == 1):
				#table
				if(len(self.table ) == 0):
					
					self.create_table();
				else:
					ask = input("do you want to use older tabke ? (Y/N)");
					if(ask == "N"):
						self.create_table();
					
						
				lag = LAGRANGECOMPUTING(self.table,True,"","");
				unknown = float(input("value at  = "));
				for i in range(1,len(lag.table) -1):
					print("for degree "+ str(i) );
					lag.lagrange_approximate_at(unknown , i , True);
				pass;
			else:
				self.take_input();
				arr = [];
				n = int(input("emter number of digits = "));
				
				for i in range(0,n):
					x=float(input("x" +str(i) + "="));
					arr.append(x);
				lag = LAGRANGECOMPUTING(arr,False,self.eq,self.var);
				unknown = float(input("value at  = "));
				print(len(lag.table));
				for i in range(1,len(lag.table)-1):
					print("   					for degree "+ str(i) );
					try:
						lag.lagrange_approximate_at(unknown , i , False);
					except:
						pass;
					print("  \n\n")
				#equation
				pass;		
		pass;	
	def newton_ddt(self):
		xarr=[];
		fxarr=[];
		n = int(input("emter number of entries = "));
				
		for i in range(0,n):
			x=float(input("x" +str(i) + "="));
			fx=float(input("y" + str(i) + "="));
			xarr.append(x);
			fxarr.append(fx);
			
		ddt = DDT([xarr , fxarr]);
		unknown = float(input("value at  = "));
		ddt.approximate_ddt(unknown);
		
	def forward_sdt(self):
		xarr=[];
		fxarr=[];
		n = int(input("emter number of entries = "));
				
		for i in range(0,n):
			x=float(input("x" +str(i) + "="));
			fx=float(input("y" + str(i) + "="));
			xarr.append(x);
			fxarr.append(fx);
		sdtf = SDTforward([xarr , fxarr]);
		unknown = float(input("value at  = "));
		sdtf.approximate_sdt(unknown);
		pass;
	
	def analyze_all(self):
		print("collective eanaysis of the 3 methods .. enter right intervak");
		self.take_input();
		
		call = NUMERICALCOMPUTING(self.var , self.eq);
		
		lower = float(input("enter value of a="));
		upper= float(input("enter value of b="));
		t_d = float(input("enter tolerance value [t] 10^-[t] = (enter only t after minus sign) = "));
		t_d = 1/pow(10,t_d);
		#print("tolerance = "  + str(t_d));
		call.bisection(lower, upper,t_d);
		call.regular_falsi(lower , upper , t_d);
		call.secant_method(lower , upper, t_d);
		
		
		print("");
		pass;	
	def backward_sdt(self):
		xarr=[];
		fxarr=[];
		n = int(input("emter number of entries = "));
				
		for i in range(0,n):
			x=float(input("x" +str(i) + "="));
			fx=float(input("y" + str(i) + "="));
			xarr.append(x);
			fxarr.append(fx);
		sdtb = SDTbackward([xarr , fxarr]);
		unknown = float(input("value at  = "));
		sdtb.approximate_sdt(unknown);
		pass;
		pass;






caller = CALLER();
handler = FUNCHANDLER();
ode = ODE();
calling=[
	[caller.call_bisection , caller.call_regular_falsi , caller.call_secant , caller.analyze_all],
	[caller.lagrange_inter , caller.newton_ddt , caller.forward_sdt , caller.backward_sdt],
	[handler.threepointend , handler.threepointmidpoint , handler.fivepointend , handler.fivepointmidpoint , handler.trapezonialintegration , handler.simpsonintegration13rd , handler.simpsonintegration38th ],
	[ode.euler , ode.midpoint , ode.modifiedeuler]
	
]	

def banner():
	names= ["IBAD SALEEM" , "TANZEEL AHMED" , "ABDUL REHMAN" , "ALI HAMZA USMANI" ]
	print("\t\tNUMNERICAL COMPUTING IN PYTHON\n\n");
		
	for x in names:
		print("\t\t\t\t" + x);
	
	inp  = input("\n\n\n\t\t\tPRESS ANY KEY CONTINUE =   ");
	if(inp != "E"):
		return 1;
	else:
		return 0;
	


res = banner();

os.system("cls");

while(res):	
	level = 1;
	prom = print_choice(level);

	if(prom == 1):
		level = 2;
		prom = print_choice(level);
		if(prom >=1 and prom <= len(calling[0])):
			calling[0][prom-1]();
		else:
			print("invalid input");
	
	elif(prom == 2):
		level=3
		prom= print_choice(level);
		print("prom = "+str(prom));
		if(prom >=1 and prom <= len(calling[1])):
			calling[1][prom-1]();
		else:
			print("invalid input");
		pass;
	elif(prom == 3):
		level = 4;
		prom = print_choice(level);
		print("prom = "+str(prom));
		if(prom >=1 and prom <= len(calling[2])):
			calling[2][prom-1]();
		else:
			print("invalid input");
		pass
	elif(prom == 4):
		level = 5;
		prom = print_choice(level);
		print("prom = "+str(prom));
		if(prom >=1 and prom <= len(calling[3])):
			calling[3][prom-1]();
		else:
			print("invalid input");
		pass
	
	elif(prom == 5):
		os.system("cls");			
	elif(prom == 6):
		res = 0;
