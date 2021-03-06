"""
@author: jair
"""
import numpy as np
from scipy.integrate import simps, trapz

class ROC_AUC_1:
	#Implementing the ROC AUC Comput from:
	#Fawcett, 2005, An Introduction to ROC Analysis
	def __init__(self,datlist):
		self.data = datlist
		# first arg: prevision second arg: 1/0 for (true/false)
		self.data.sort( key=lambda tup: tup[0], reverse=True)
		self.Ndata = len(self.data)
		self.N = 0
		self.P = 0
		self.tp = 0.0
		self.fp = 0.0
		self.tp_ = 0.0
		self.fp_ = 0.0
		self.fprev = -1000
		#self.area = 0.0
		self.curve = []

    	def trapz_area(self):
         '''
         compute efficient trapezoid area
         '''
         yield np.trapz([tmp[1] for tmp in self.curve], x=[tmp[0] for tmp in self.curve])

	def auc(self):
		for tmp in self.data:
			if tmp[0] <> self.fprev:
				#self.area += area(self.fp,self.fp_,self.tp,self.tp_)
				self.curve.append([self.fp/self.N,self.tp/self.P])
				self.fprev = tmp[0]
				self.tp_ = self.tp
				self.fp_ = self.fp
			if tmp[1] == 1:
				self.tp += 1
			else:
				self.fp += 1
		self.curve.append([self.fp/self.N,self.tp/self.P])

	def counting(self):
		for tmp in self.data:
			if tmp[1] == 1:
				self.P += 1
			else:
				self.N += 1
				
'''
print "area fawcett", a_roc.area
print "area trapezoid:", np.trapz([tmp[1] for tmp in a_roc.curve], x=[tmp[0] for tmp in a_roc.curve ])
print "area Simpson:", scipy.integrate.simps(np.array([tmp[1] for tmp in a_roc.curve]), np.array([tmp[0] for tmp in a_roc.curve]))
'''
