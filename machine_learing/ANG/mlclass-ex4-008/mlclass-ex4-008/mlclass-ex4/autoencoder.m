function [W] = autoencoder(X,hidden_size,lambda,iter)

input_size = size(X,2);
epsilon = 0.12;
%actually we need only one W for W(2) = W(1)' 
Theta1 = rand(hidden_size,input_size+1)*2*epsilon-epsilon;
Theta2 = rand(input_size,hidden_size+1)*2*epsilon-epsilon;
theta_vec = [Theta1(:);Theta2(:)];
options = optimset('GradObj','on','MaxIter',iter);

cosFunction = @(a)encodeCostFun(a,X,hidden_size,lambda);

Theta = fmincg(cosFunction,theta_vec,options);
W = reshape(Theta(1:hidden_size*(input_size+1)),hidden_size,input_size+1);

end
