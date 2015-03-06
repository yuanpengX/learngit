load ex4data1

m = size(X,1);
n = size(X,2);
sigma = zeros(n,n);
for k = 1:n
	for i = 1:m
		sigma += X(i,:)'*X(i,:);
	end
sigma/=m;
[u s v] = svd(sigma);
X_approx = X*u(:,1:k)*u(:,1:k)';
x_error(k) = sum(sum(X_approx-X).^2)/sum(sum(X.^2));
end
k = [1:n];
plot(k,x_error)
