import spaceGraph as SG

sg = SG.cSpace('spaceGraph')

sg.addChildren([SG.cSpace('A'), SG.cSpace('B'), SG.cSpace('C'), SG.cSpace('D')])
sg.addChildren([SG.cSpace('E'), SG.cSpace('F')])
sg.c['A'].addChildren([SG.cSpace('A1'),SG.cSpace('A2'),SG.cSpace('A3')])
sg.c['A'].connectChildren('A1','A3')
sg.c['A'].c['A2'].addChildren([SG.cSpace('A21'),SG.cSpace('A22'),SG.cSpace('A23')])
sg.c['B'].addChildren([SG.cSpace('B1'),SG.cSpace('B2'),SG.cSpace('B3')])
sg.c['B'].c['B2'].addChildren([SG.cSpace('B21'),SG.cSpace('B22'),SG.cSpace('B23')])

sg.connectChildren('A', 'B')
sg.connectChildren('B', 'C')
sg.connectChildren('B', 'D')
sg.connectChildren('C', 'D')
sg.connectChildren('E', 'F')
sg.connectChildren('F', 'C')

A = sg.c['A']
path = A.findAllPathsTo(sg.c['F'])
#print(path)
short = A.findShortestPathTo(sg.c['F'])
#print(short)
A22 = sg.c['A'].c['A2'].c['A23']
SG.printRelation(A22.relationTo(sg.c['B'].c['B2'].c['B22']))
