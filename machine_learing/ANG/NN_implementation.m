%load data here
load mnistAll
train_images = mnist.train_images;
train_labels = mnist.train_labels;
m = 30000;
MN = 28*28;
train_images = train_images(:,:,1:m);
train_labels = train_lables(1:m);
train_images = double(reshape(train_images,MN,m));
Train_images = [ones(1,m);train_images];
Train_labels = zeros(10,m);
for i = 1:m
Train_labels(train_labels(i)+1,i) = 1;
end

%set net as MN*MN+1*MN+1*MN+1*10
L = 5;
s(1) = MN;
s(2) = MN+1;
s(3) = MN+1;
s(4) = MN+1;
s(5) = 10;

function [J,grad] = cost_fun(thetaVec,X,y,lambda,s,L)
m = size(X,2);
NUM = 1;
for i = 1:L-1
theta{i} = reshape(thetaVec(N:N+s(l)*s(l)-1),s(l),s(l+1));
N = N+s(l)+s(l+1);
end

%forward propagation
a{1} = X;
for i = 2:L
a{i} = sigmoid(theta{i-1}*a{i-1});
end

%back propagation
delta{L} = a{L}-y;
for i = 2:L-1
delta{i} = theta{i-1}*delta{i+1}.*a{i}.*(1-a{i});
end

%compute partial of J
grad = [];
for 1:L-1
D{i} = 1/m*delta{i+1}*a{i}'+lambda/m.*theta{i}; 
grad = [grad;(D{i})(:)];
end

end

X = Train_images(:,i);
y = Train(:,i);
options = optimst('GradObj','on','MaxIter',400);
[theta,jval] = fminunc(@(t)cos_fun(t,X,y,lambda,s,L),InitTheta,options);
