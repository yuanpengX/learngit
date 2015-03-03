function [J grad] = encodeCostFun(theta_vec,X,hidden_size,lambda)

input_size = size(X,2);
Theta1 = reshape(theta_vec(1:hidden_size*(input_size+1)),hidden_size,input_size+1);
Theta2 = reshape(theta_vec(hidden_size*(input_size+1)+1:end),input_size,hidden_size+1);

%forward prog
m =  size(X,1);
a1 = [ones(m,1) X];
z2 = a1*Theta1';
a2 = [ones(m,1) sigmoid(z2)];
a3 = a2*Theta2';

J = sum(sum((X-a3).^2))./(2*m) + lambda/(2*m)*(sum(sum(Theta1(2:end).^2))+sum(sum(Theta2(2:end).^2)));

%back prog
z2 = [ones(m,1) z2];
grad1 = zeros(hidden_size,input_size+1);
grad2 = zeros(input_size,hidden_size+1);
for t = 1:m
delta_L = (a3(t,:)-X(t,:))';
delta_h = Theta2'*delta_L.*sigmoidGradient(z2(t,:)');
grad1+=delta_h(2:end)*a1(t,:);
grad2+= delta_L*a2(t,:);
end 

grad2/=m;
grad1/=m;
tmp1 = Theta1;
tmp2 = Theta2;
tmp1(:,1) = 0;
tmp2(:,1) = 0;
grad1 +=lambda/m.*tmp1;
grad2 += lambda/m.*tmp2;
grad = [grad1(:);grad2(:)];

end
