
def Train_Accucary(model,X,Y,splitter):
	mean=0
	count =0
	for test_index,ignore in splitter:
		X_train=[]
		Y_train=[]
		for i in test_index:
			X_train.append(X[i])
			Y_train.append(Y[i])
		mean=mean+model.fit(X_train,Y_train).score(X_train,Y_train)
		count = count+1
	return mean/count