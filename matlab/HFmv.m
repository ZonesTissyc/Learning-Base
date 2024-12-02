% 定义空间网格
[x, y, z] = meshgrid(linspace(-5, 5, 100), linspace(-5, 5, 100), linspace(-5, 5, 100));

% 定义H和F原子的坐标
H = [0, 0, 0];
F = [1.7, 0, 0]; % 大约1.7埃的键长

% 定义简单的原子轨道函数 (s轨道和p轨道)
orbital_H = @(x, y, z, center) exp(-sqrt((x-center(1)).^2 + (y-center(2)).^2 + (z-center(3)).^2));
orbital_F = @(x, y, z, center) (x-center(1)) .* exp(-sqrt((x-center(1)).^2 + (y-center(2)).^2 + (z-center(3)).^2));

% 计算电子密度分布，考虑最大重叠态
rho = orbital_H(x, y, z, H) .* orbital_F(x, y, z, F);

% 创建动画
figure;
isosurface(x, y, z, abs(rho), 0.01); % 绘制等值面
axis equal;
colormap jet;
xlabel('X');
ylabel('Y');
zlabel('Z');
title('HF 分子最大重叠程度电子云图');

% 设置动画参数
frames = 20; % 动画帧数
m = moviein(frames); % 创建一个movie矩阵
for i = 1:frames
    view(-37.5 + 24*(i-1), 30); % 改变视点
    m(:, i) = getframe; % 将当前图形保存到movie矩阵
end

% 播放动画
movie(m, 2); % 播放动画2次
