function [J grad] = logisticFun(X,y,theta,lambda)
m = size(X,1);

J = sum((X*theta-y).^2)/(2*m)+lambda/(2*m)*sum(theta(2:end).^2);

grad = X'*(X*theta-y);
tmp = theta;
tmp(1) = 0;
grad+=lambda/m.*tmp;

end
