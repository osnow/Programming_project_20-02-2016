# Programming_project_20-02-2016
Programming project at Scilife - SVM protein predictor

24/02/2016 - finished python program to extract features from my data and turn into svm light file. I used many lists and for loops and in retrospect I think it would be better to use numpy arrays to ensure I keep track of all the sequences correctly. However, my outputs seems correct with manual inspection so I won't change it for now but that would be a future improvement. 

25/02/2016 - Made a python program to split my dataset (from original sequence file). I have 42 sequences and their corresponding topologies so have seven sequences and topologies in each dataset. I then made input files for svm_light using my feature extraction program and made 5 different combinations of training sets (set 1-4 to test with 5, set 1235 to test on 4 etc). I couldn't seem to find a way to input multiple files for training in svm_light so this was my way of solving that problem. 

26/02/2016 - Installed svm_light on my workstation and did a few different rounds of training and classifying and it all seemed to work relatively well. I got around 80% accuracy with the models I trained. I decided to try to start tackling the psi-blast part of the project and if that fails I can come back and optimise these models by trying different parameters etc. 

29/02/2016 - Ran psiblast for each protein sequence and generated PSSM files for each. Working on making a program to reformat PSSMs and write to a file with target values for SVM_light input 
