import sys

def main():
	filename = sys.argv[1][:sys.argv[1].find(".asm")] + ".hack"
	outptr = open(filename, "w")

	with open(sys.argv[1], "r") as inptr:
		file = inptr.read()
	file = file.split("\n")

	newfile = []
	for line in file:
		# remove whitespace and comments
		line = ''.join(line.split())

		if(line.find("//") != -1):
			line = line[: line.find("//")]

		if(len(line) > 0):
			newfile.append(line)
	file = newfile

		# construct predefined
	symbol_tabel = {"R0" : "0", "R1" : "1", "R2" : "2", "R3" : "3", "R4" : "4", "R5" : "5", "R6" : "6", "R7" : "7", "R8" : "8", "R9" : "9", "R10" : "10", "R11" : "11", "R12" : "12", "R13" : "13", "R14" : "14", "R15" : "15", "SCREEN" : "16384", "KBD" : "24576", "SP" : "0", "LCL" : "1", "ARG" : "2", "THIS" : "3", "THAT" : "4"}

	# add all pseduo commands
	count = 0
	newfile = []
	for line in file:
		if(line[0] == "(" and line[len(line)-1] == ")"):
			symbol_tabel[line[1:len(line)-1]] = str(count)
		else:
			newfile.append(line)
			count = count + 1
	file = newfile


	# replace all pseudo while replacing variables
	newfile = []
	for line in file:
		if(line[0] == "@" and line[1:] in symbol_tabel):
			line = "@" + symbol_tabel[line[1:]]
		newfile.append(line)
	file = newfile

	filename = sys.argv[1][:sys.argv[1].find(".asm")] + ".hack"
	outptr = open(filename, "w")
	for line in file:
		# if A command
		if(line[0] == '@'):
			outptr.write(str(bin(int(line[1:]))[2:]).zfill(16) + "\n")

		# if C command
		else:
			dest, comp, jmp = "", "", ""
			# if JMP exists
			if(line.find(";") != -1):
				jmp = line[line.find(";") + 1:]
				line = line[:line.find(";")]

			# if dest exists
			if(line.find("=") != -1):
				dest = line[:line.find("=")]
				comp = line[line.find("=") + 1:]

			else:
				comp = line

			outptr.write(parse(dest, comp, jmp) + "\n")


def parse(dest, comp, jmp):
	all_dest = {"": "000", "M": "001", "D" : "010", "MD" : "011", "A" : "100", "AM" : "101", "AD" : "110", "AMD" : "111"}
	all_comp = {"0": "0101010", "1": "0111111", "-1": "0111010", "D" : "0001100", "A" : "0110000", "!D": "0001101", "!A": "0110001", "-D" : "0001111", "-A":"0110011", "D+1": "0011111", "A+1": "0110111", "D-1" : "0001110", "A-1":"0110010", "D+A":"0000010", "D-A":"0010011", "A-D":"0000111", "D&A":"0000000", "D|A":"0010101", "M" : "1110000", "!M" : "1110001", "-M" : "1110011", "M+1" : "1110111", "M-1" : "1110010", "D+M":"1000010", "D-M":"1010011", "M-D":"1000111", "D&M":"1000000", "D|M":"1010101"}
	all_jmp = {"": "000", "JGT" : "001", "JEQ": "010", "JGE":"011", "JLT":"100", "JNE":"101", "JLE":"110", "JMP":"111"}

	return "111" + all_comp[comp] + all_dest[dest] + all_jmp[jmp]

def sim():
				#print(dest + "      " + comp + "       " + jmp)


	print("\n\n\nDEBUG\n\n\n")
	print(symbol_tabel)
	for line in file:
		print(line)
	print(len(file))

if __name__ == "__main__":
	main()