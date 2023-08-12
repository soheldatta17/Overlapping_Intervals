class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
		a=[]
		Intervals=list(sorted(Intervals))
		a.append(Intervals[0][0])
		a.append(Intervals[0][1])
		ma=Intervals[0][1]
		for i in range(1,len(Intervals)):
		    if ma<Intervals[i][1] and ma>=Intervals[i][0]:
		        a.remove(ma)
		        a.append(Intervals[i][1])
		        ma=Intervals[i][1]
		    if ma<Intervals[i][0]:
		        a.append(Intervals[i][0])
		        a.append(Intervals[i][1])
		        ma=Intervals[i][1]
		#a=list(a)
		Intervals=[[a[i],a[i+1]]for i in range(0,len(a),2)]
		return Intervals