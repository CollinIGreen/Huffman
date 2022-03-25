class Huff():
  def __init__(self):
    self.value = None
    self.bVal = None
    self.oNode = None
    self.zNode = None
    self.Code = None
  def MakeT(self, alphaL):
    list = []
    for i in alphaL:
      new = Huff()
      new.value = i
      list.append(new)
    alphaL = list
    while len(alphaL) != 1:
      node1 = alphaL.pop(0)
      node2 = alphaL.pop(0)
      rNode = Huff()
      rNode.value = node1.value+node2.value
      if node1.value < node2.value:
        rNode.zNode, rNode.zNode.bVal = node1, "0"
        rNode.oNode, rNode.oNode.bVal = node2, "1"
      else:
        rNode.zNode, rNode.zNode.bVal = node2, "0"
        rNode.oNode, rNode.oNode.bVal = node1, "1"
      alphaL.append(rNode)
      for i in range(len(alphaL)):
        for x in range(i, len(alphaL)):
          if alphaL[i].value > alphaL[x].value:
            alphaL[i], alphaL[x] = alphaL[x], alphaL[i]
    self.value = alphaL[0].value
    self.oNode = alphaL[0].oNode
    self.zNode = alphaL[0].zNode
  def binCode(self):
    if self.oNode == None and self.zNode == None:
      return [self.value, self.bVal]
    value = self.oNode.binCode()
    value2 = self.zNode.binCode()
    if self.bVal != None:
      if len(value[1]) != 1:
        if self.bVal != None:
          for i in range(len(value)):
            value[i][1] = value[i][1] + self.bVal
      else:
        if self.bVal != None:
          value[1] = value[1]+self.bVal
        value = [value]
      if len(value2[1]) != 1:
        if self.bVal != None:
          for i in range(len(value2)):
            value2[i][1] = value2[i][1] + self.bVal
      else:
        if self.bVal != None:
          value2[1] = value2[1] + self.bVal
        value2 = [value2]
    for i in value:
      value2.append(i)
    value2.sort()
    self.Code = value2
    return value2
hello = Huff()
hello.MakeT([0.02,0.03,0.04,0.06,0.07,0.08,0.09,0.11,0.20,0.30])
print(hello.binCode())
