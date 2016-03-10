import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
import sys

script_name = sys.argv[0]

# Input files/output files
input_file1 = sys.argv[1]
input_file2 = sys.argv[2]
output_file = sys.argv[3]

# create array from predictions file and test file target values
predictions = np.loadtxt(input_file1)
real_values = np.loadtxt(input_file2, usecols=(0,))

# calculate roc curve and auc
fpr, tpr, thresholds = metrics.roc_curve(real_values, predictions, pos_label=1)
roc_auc = metrics.auc(fpr, tpr)

# plot the roc curve and save to file
plt.figure()
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.savefig(output_file)





