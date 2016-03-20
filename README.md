# Programming_project_20-02-2016
Programming project at Scilife - SVM protein predictor

24/02/2016 - finished python program to extract features from my data and turn into svm light file. I used many lists and for loops and in retrospect I think it would be better to use numpy arrays to ensure I keep track of all the sequences correctly. However, my outputs seems correct with manual inspection so I won't change it for now but that would be a future improvement. 

25/02/2016 - Made a python program to split my dataset (from original sequence file). I have 42 sequences and their corresponding topologies so have seven sequences and topologies in each dataset. I then made input files for svm_light using my feature extraction program and made 5 different combinations of training sets (set 1-4 to test with 5, set 1235 to test on 4 etc). I couldn't seem to find a way to input multiple files for training in svm_light so this was my way of solving that problem. 

26/02/2016 - Installed svm_light on my workstation and did a few different rounds of training and classifying and it all seemed to work relatively well. I got around 80% accuracy with the models I trained. I decided to try to start tackling the psi-blast part of the project and if that fails I can come back and optimise these models by trying different parameters etc. 

29/02/2016 - Ran psiblast for each protein sequence and generated PSSM files for each. Working on making a program to reformat PSSMs and write to a file with target values for SVM_light input 

01/03/2016 - Created python program to extract the data from the PSSM files and turn them into a data frame which I can then apply the sigmoidal function to and write to a file in the format for svm. Also, I am rerunning psiblast as I had originally used blast+ on the non-redundant database and it produced incorrect matrix files and did make any files for some sequences. At least the output file is the same so my program will work for the new matrices whenever they finish running. 

02/03/2016 - Flying to Canada to visit family and friends. Wrote project report outline and started writing report. Going to use latex because including figures and formulas is easier and looks pretty. 

03/03/2016 - Finished rerunning PSIBLAST and successfully made matrix files for all sequences. Used my program to create input files for svm-light from PSSMs. 

04/03/2016 - Split my svm dataset into 6 parts with five for training and testing and the 6th for the final test. Running SVM_light with linear kernel seems to be fine but producing only negative predictions. Might be a problem that my dataset is too small. 

07/03/2016 - SVM with polynomial kernel and RBF kernel finally produces some positive results but still not that many. Sigmoidal kernel produces terrible accuracy on 2 test sets so I won't continue testing with that one as it also takes a long time. RBF seems to be the best but is only around 80% accurate and just slightly better than polynomial. 

08/03/2016 - Figured out how to create a ROC curve from my svm output. Plotting all RBF test set results on one plot and all polynomial test set results on another to determine best kernel. 

09/03/2016 - Made python scripts for getting confusion matrix and MCCs 

13/03/2016-18/03/2016 - Doing some further optimizing and writing report 
