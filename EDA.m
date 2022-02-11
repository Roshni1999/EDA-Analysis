M1 = readmatrix('Roshni/data_roshni.xlsx');
M2 = readmatrix('Shabina/data_shabina.xlsx');

Time11 = M1(:,4);
Time1 = zeros(length(Time11), 1);
for i = 1:length(Time1)
    Time1(i) = Time11(i) - Time11(1);
end
EDA1 = M1(:,6);
ind1 = find(Time1<120);

Time22 = M2(:,4);
Time2 = zeros(length(Time22), 1);
for i = 1:length(Time2)
    Time2(i) = Time22(i) - Time22(1);
end
EDA2 = M2(:,5);
ind2 = find(Time2<120);

t1 = Time1(ind1);
t2 = Time2(ind2);
ADC1 = EDA1(ind1);
ADC2 = EDA2(ind2);

V1 = (ADC1./512)*2.5;
S1 = ((5./(0.5 -(0.2.*V1)))-5); 
SC1 = 200-S1;
V2 = (ADC2./512)*2.5;
S2 = ((5./(0.5 -(0.2.*V2)))-5); 
SC2 = 200-S2;

figure(1); hold on
plot(Time1(ind1), SC1 , 'b','LineWidth', 1)
plot(Time2(ind2), SC2 , 'r','LineWidth', 1)
xlabel('Time (seconds)'); ylabel('Skin Conductance (uS)');
title('Raw EDA signal'); legend('Subject1', 'Subject2')


%%