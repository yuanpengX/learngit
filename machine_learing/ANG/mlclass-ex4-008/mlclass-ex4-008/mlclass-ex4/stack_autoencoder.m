load ex4data1
m = size(X,1);
hidden_size = round(size(X,2)/2);
lambda = 1;
iter = 1000;
tic
W1 = autoencoder(X,hidden_size,lambda,iter);
toc
X = [ones(m,1) X];
h1 = sigmoid(X*W1');
hidden_size = round(size(h1,2)/2);
W2 = autoencoder(h1,hidden_size,lambda,iter);

h1 = [ones(m,1) h1];
h2 = sigmoid(h1*W2');
width = round(sqrt(size(h2,2)));
colormap gray
sel = randperm(size(h2,1));
sel = sel(1:100);
displayData(h2(sel,:));
pause
for i = 1:size(sel,1)
features = reshape(h2(sel(i),:),width,width);
imagesc(features,[-1 1]);
pause
end

save auto.mat
