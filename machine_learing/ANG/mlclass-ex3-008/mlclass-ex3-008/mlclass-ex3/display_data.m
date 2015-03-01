load ex3data1
sel = randperm(size(X,1));
sel = sel(1:1000);
function disp(X,y)
colormap gray
load ex3weights
for i = 1:size(X,1)
x = X(i,:);
width = round(sqrt(size(X,2)));
width2 = round(sqrt(size(Theta1,1)));
disp = reshape(x,width,width);
subplot(1,2,1);
title('image');
imagesc(disp,[-1,1]);
a1 = [1 x];
z2 = a1*Theta1';
a2 = sigmoid(z2);
xlabel(sprintf('true is %d',mod(y(i),10)));
subplot(1,2,2);
disp = reshape(a2,width2,width2);
imagesc(disp,[-1 1]);
a2 = [1 a2];
h = a2*Theta2';
[tmp y_p] = max(h);
xlabel(sprintf('predict is %d',mod(y_p,10)));
pause(0.5);
end;
end
disp(X(sel,:),y(sel));
