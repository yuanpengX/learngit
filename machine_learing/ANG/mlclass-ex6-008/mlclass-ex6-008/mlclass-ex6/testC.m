load('ex6data3.mat');
C = [0.01 0.03 0.1 0.3 1 3 10 30];
sigma = C;
mine = 1000000;
for i = 1:8
	for j = 1: 8
		model = svmTrain(X,y,C(i),@(x1,x2)gaussianKernel(x1,x2,sigma(j)));
		errors = mean(double(svmPredict(model,Xval)~=yval));
		if (errors < mine) & errors~=0
			tmp_i = i
			tmp_j = j
			mine = errors
		end	
	end
end
C(tmp_i)
sigma(tmp_j)


