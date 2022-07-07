path_to_read = '/home/risc/Awais/practice/label_correct/007476.txt'
path_to_write = '/home/risc/Awais/practice/label_correct/changed_labels'
with open(path_to_read) as f:
	for line in f:
		line = line.strip()
		line = line.split(' ')
		#print(line)
		line[0] = "MotorBike"
		line.insert(1, line.pop(-1))
		#print(line[0])
		#print(line)
		line = " ".join(line)
		print(line)

		path =path_to_read.split('/')[-1].split('.')[-2]
		print(path)
		with open("/home/risc/Awais/practice/label_correct/changed_labels/00%i.txt" %int(path), "a") as out:
			out.write(line)
			out.write('\n')
