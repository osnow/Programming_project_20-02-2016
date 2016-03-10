import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


script_name = sys.argv[0]

# Input files/output files
input_file1 = sys.argv[1]
input_file2 = sys.argv[2]
output_file = sys.argv[3]

# create array from predictions file and test file target values
predictions = np.loadtxt(input_file1)
real_values = np.loadtxt(input_file2, usecols=(0,))
pred_bin = []
for i in predictions:
    if i > 0:
        pred_bin.append(+1)
    else:
        pred_bin.append(-1)

mat = confusion_matrix(real_values, pred_bin)
print mat
plt.figure()
plt.imshow(mat, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix test set 1 Poly')
plt.colorbar()
labels = ["Pos", "Neg"]
ticks = np.arange(len(labels))
plt.xticks(ticks, labels, rotation=45)
plt.yticks(ticks, labels)
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.savefig(output_file, bbox_inches="tight")