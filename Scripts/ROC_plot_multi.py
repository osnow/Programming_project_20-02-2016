import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
import sys

script_name = sys.argv[0]

# Input files/output files
input_file1 = sys.argv[1:6]
input_file2 = sys.argv[6:11]
output_file = sys.argv[11]

plt.figure()
count = 1
# loop through prediction and true files and calculate roc curve and auc for each pair and plot them
for i, n in zip(input_file1, input_file2):
    predictions = np.loadtxt(i)
    real_values = np.loadtxt(n, usecols=(0,))
    fpr, tpr, thresholds = metrics.roc_curve(real_values, predictions, pos_label=1)
    roc_auc = metrics.auc(fpr, tpr)
    plt.plot(fpr, tpr, label='ROC curve test set %d (area = %0.2f)' % (count, roc_auc))
    count += 1

# Make figure with labels and legend and y=x line and save it to output file
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic Polynomial Kernel')
plt.legend(loc="lower right")
plt.savefig(output_file)
