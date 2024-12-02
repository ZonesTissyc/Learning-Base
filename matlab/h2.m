% 定义空间网格
[x, y, z] = meshgrid(linspace(-5, 5, 100), linspace(-5, 5, 100), linspace(-5, 5, 100));

% 定义两个氢原子的坐标
H1 = [0, 0, -0.7];
H2 = [0, 0, 0.7];

% 定义简单的原子轨道函数
orbital = @(x, y, z, center) exp(-((x-center(1)).^2 + (y-center(2)).^2 + (z-center(3)).^2));

% 计算电子密度分布，考虑排斥态（反对称态）
rho = orbital(x, y, z, H1) - orbital(x, y, z, H2); % 反对称

% 绘制等值面图
figure;
isosurface(x, y, z, abs(rho), 0.05); % 取绝对值并设置等值面
axis equal;
colormap jet;
title('H_2 分子排斥态电子云图');
xlabel('X');
ylabel('Y');
zlabel('Z');
