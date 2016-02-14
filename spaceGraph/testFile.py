import spaceGraph as sg

sg = cSpace('spaceGraph')

sg.addChildren([cSpace('A'), cSpace('B'), cSpace('C'), cSpace('D')])
sg.addChildren([cSpace('E'), cSpace('F')])
sg.c['A'].addChildren([cSpace('A1'),cSpace('A2'),cSpace('A3')])
sg.c['A'].connectChildren('A1','A3')
sg.c['A'].c['A2'].addChildren([cSpace('A21'),cSpace('A22'),cSpace('A23')])
sg.c['B'].addChildren([cSpace('B1'),cSpace('B2'),cSpace('B3')])
sg.c['B'].c['B2'].addChildren([cSpace('B21'),cSpace('B22'),cSpace('B23')])

sg.connectChildren('A', 'B')
sg.connectChildren('B', 'C')
sg.connectChildren('B', 'D')
sg.connectChildren('C', 'D')
sg.connectChildren('E', 'F')
sg.connectChildren('F', 'C')

A = sg.c['A']
path = A.findAllPathsTo('F')
#print(path)
short = A.findShortestPathTo('F')
#print(short)
A22 = sg.c['A'].c['A2'].c['A23']
print(A22.relationTo(sg.c['B'].c['B2'].c['B22']))
