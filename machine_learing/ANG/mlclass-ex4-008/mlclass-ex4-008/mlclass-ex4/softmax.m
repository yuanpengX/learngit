load auto
load ex4data1

%get features
m = 3000;
lambda = 1;
X_train = X(1:m,:);
a1 = [ones(m,1) X_train];
z2 = a1*W1';
a2 = [ones(m,1) sigmoid(z2)];
z3 = a2*W2';
a3 = sigmoid(z3);
%train softmax 
%use oneVsall method
y_train = y(1:m);
num = 10;
a3 = [ones(m,1) a3];
init_theta = zeros(size(a3,2),1);
theta_vec = [];
options = optimset('GradObj','on','MaxIter',200);
for i = 1:num
theta_vec(:,i) = fmincg(@(a)logisticFun(a3,y_train==i,a,lambda),init_theta,options);
end

