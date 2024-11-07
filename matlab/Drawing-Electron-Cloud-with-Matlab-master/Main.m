p =-pi/2:pi/60:pi/2; t=0:2*pi/100:2*pi; [P,T]=meshgrid(p, t); theta=pi/2-P; phi=T;
R=Yfxz2(theta,phi); %�ı�˾������������
R1=abs(R); [n, m]=size(R); C=ones(n, m);
i=find(R<0); %Ѱ�� R<0 ��ָ��
C(i)=0;
[X,Y,Z] =sph2cart (T,P,R1); surf(X,Y,Z,C);
xlabel('x'); ylabel('y'); zlabel('z'); axis equal; rotate3d on;%��������϶�ͼ�ο�����ת

%%%Ҳ���Խ����һ���Ϊ��������Ƴɶ�����
%m=moviein(20); %����һ�� 20 �д����
% for i=1:20
% view(-37.5+24*(i-1), 30); %�ı��ӵ�
% m(:,i) =getframe; %��ͼ�α��浽 m ����
% end
% movie(m,2); ���Ż��� 2 ��?



%%% Ҳ����������䱣��Ϊ M �ļ�����ƽ�漫����ͼ��
% t=0:pi/50:2*pi; phi=0; theta=t; 
% r=(Ysp_1(theta, phi)); polar (t, abs(r), '-r');
% i=find(r>0); r(i)=nan; hold on; polar(t, abs(r),'-b');