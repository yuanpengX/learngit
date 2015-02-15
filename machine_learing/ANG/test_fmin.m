 %global x;
%global m;
%x = 
%function [grad,j]=cost_function(theta)
%global x;
%global m;
%j = sum((1./(1+exp(-x*theta))-y).^2)/(2*m);
%grad = x'*(1./(1+exp(-x*theta))-y);
%end
%options = optimset('Gradobj','on','MaxIter',1000);
%[opttheta,functionval,exit_val] = fminunc(@cost_function,inittheta,options);
x = [1 1;1 0;0 1;0 0];
x = [ones(length(x),1) x];
y = [1;0;0;0];
function g = sigmoid(z)
g = 1./(1+exp(-z));
end

function [grad j] = cost_fun(theta,X,y)
m = length(size(X,1));
j = 1/m.*sum(-y.*log(sigmoid(X*theta))-(1-y).*log(1-sigmoid(X*theta)));
grad = 1/m.*(X'*(X*theta-y));
end

options = optimset('Gradobj','on','MaxIter',400);
init_theta = ones(size(x,2),1)
[theta jval] = fminunc(@(t)(cost_fun(t,x,y)),init_theta,options)
