% 定义空间网格
[x, y, z] = meshgrid(linspace(-3, 3, 100), linspace(-3, 3, 100), linspace(-3, 3, 100));

% 定义C和H原子的坐标
C = [0, 0, 0];
H1 = [1, 1, 1] * 1.09; % 大约1.09Å的C-H键长
H2 = [-1, -1, 1] * 1.09;
H3 = [1, -1, -1] * 1.09;
H4 = [-1, 1, -1] * 1.09;

% 定义sp³杂化轨道函数
sp3_orbital = @(x, y, z, center, dir) exp(-sqrt((x-center(1)).^2 + (y-center(2)).^2 + (z-center(3)).^2)) .* (dir(1)*x + dir(2)*y + dir(3)*z);

% 计算sp³杂化轨道的电子密度分布
rho_sp3_H1 = sp3_orbital(x, y, z, C, H1);
rho_sp3_H2 = sp3_orbital(x, y, z, C, H2);
rho_sp3_H3 = sp3_orbital(x, y, z, C, H3);
rho_sp3_H4 = sp3_orbital(x, y, z, C, H4);

% 总电子密度
rho_total = abs(rho_sp3_H1) + abs(rho_sp3_H2) + abs(rho_sp3_H3) + abs(rho_sp3_H4);

% 绘制等值面图
figure;
isosurface(x, y, z, rho_total, 0.1); % 设置等值面
axis equal;
colormap jet;
title('CH_4 分子杂化轨道图');
xlabel('X');
ylabel('Y');
zlabel('Z');
