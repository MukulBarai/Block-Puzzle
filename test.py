
class Block:
	width = 10
	height = 10

block = Block()

def change(block):
	nBlock = block
	nBlock.width = 20
	nBlock.height = 20

print(block.width)
change(block)
print(block.width)