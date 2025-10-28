% 定义横坐标的数据
epsilon = [0.1, 0.2, 0.4, 0.8, 1.2, 1.5];

y_offset=0.3
MSE_RR1 = [0.002408871955303 ,
0.000417809469373 ,
0.000138893409607 ,
0.000029557175769 ,
0.000013122442896 ,
0.000008772035755 ,
]; 
MSE_RR2 = [0.0004636 ,
0.0000973 ,% Define x-axis data
epsilon = [0.1, 0.2, 0.4, 0.8, 1.2, 1.5];

y_offset=0.3
MSE_RR1 = [0.002408871955303 ,
0.000417809469373 ,
0.000138893409607 ,
0.000029557175769 ,
0.000013122442896 ,
0.000008772035755 ,
]; 
MSE_RR2 = [0.0004636 ,
0.0000973 ,
0.0000240 ,
0.0000053 ,
0.0000028 ,
0.0000012 ,
]; 
MSE_ARR1 = [0.000115768332440 ,
0.000026690977204 ,
0.000009064892197 ,
0.000001136340696 ,
0 ,
0 ,
]; 
MSE_ARR2 = [0.0000428 ,
0.0000129 ,
0.0000026 ,
0.0000008 ,
0.0000002 ,
0.0000001 ,
]; 

% Create a new figure window
figure;

% First subplot - (a) Adult Dataset
subplot(1, 2, 1); % Create first subplot in 1x2 grid
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1)+0.07, pos(2) + y_offset, 0.236220472440945,0.332753710261639]);  % Only modify y-axis position

h1 = plot(epsilon, MSE_RR1, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'RR'); % Use circle markers with connecting lines
hold on;
h2 = plot(epsilon, MSE_ARR1, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'ARR'); % Use square markers with connecting lines
set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget $\epsilon$', 'Interpreter', 'latex'); % LaTeX formatted x-axis label
ylabel('Mean Square Error');
set(gca, 'FontSize', 16);
grid on;
box on;
legend show; % Display legend
legend('Location', 'NorthEast', 'FontSize', 14);
% Set x-axis ticks and labels
xticks(0:0.1:1.5); % Set tick positions
xticklabels({'0', '', '', '','', '0.5', '', '', '','', '1', '', '', '','', '1.5'}); % Set corresponding labels
set(h1, 'LineWidth', 2, 'MarkerSize', 12); % Adjust line width and marker size
set(h2, 'LineWidth', 2, 'MarkerSize', 12);
text(0.75, -0.00083, '(a) Adult Dataset', 'HorizontalAlignment', 'center', 'FontWeight', 'bold','FontSize', 18, 'FontName', 'Times New Roman');
% Second subplot - (b) Diabetes Dataset
subplot(1, 2, 2); % Create second subplot in 1x2 grid
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1), pos(2)+y_offset , 0.236220472440945,0.332753710261639]);  % Only modify y-axis position

h1 = plot(epsilon, MSE_RR2, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'RR'); % Use circle markers with connecting lines
hold on;
h2 = plot(epsilon, MSE_ARR2, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'ARR'); % Use square markers with connecting lines
set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget $\epsilon$', 'Interpreter', 'latex'); % LaTeX formatted x-axis label
ylabel('Mean Square Error');
set(gca, 'FontSize', 16);
grid on;
box on;
legend show; % Display legend
legend('Location', 'NorthEast', 'FontSize', 14);
set(h1, 'LineWidth', 2, 'MarkerSize', 12); % Adjust line width and marker size
set(h2, 'LineWidth', 2, 'MarkerSize', 12);
% Set x-axis ticks and labels
xticks(0:0.1:1.5); % Set tick positions
xticklabels({'0', '', '', '','', '0.5', '', '', '','', '1', '', '', '','', '1.5'}); % Set corresponding labels
text(0.75, -0.000165, '(b) Diabetes Dataset', 'HorizontalAlignment', 'center', 'FontWeight', 'bold','FontSize', 18, 'FontName', 'Times New Roman');
0.0000240 ,
0.0000053 ,
0.0000028 ,
0.0000012 ,
]; 
MSE_ARR1 = [0.000115768332440 ,
0.000026690977204 ,
0.000009064892197 ,
0.000001136340696 ,
0 ,
0 ,
]; 
MSE_ARR2 = [0.0000428 ,
0.0000129 ,
0.0000026 ,
0.0000008 ,
0.0000002 ,
0.0000001 ,
]; 

% 创建一个新的图形窗口
figure;

% 第一个子图 - (a) Adult Dataset
subplot(1, 2, 1); % 创建1x2网格的第一个子图
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1)+0.07, pos(2) + y_offset, 0.236220472440945,0.332753710261639]);  % 只修改y轴位置

h1 = plot(epsilon, MSE_RR1, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'RR'); % 使用圆圈标记点，并连接线段
hold on;
h2 = plot(epsilon, MSE_ARR1, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'ARR'); % 使用正方形标记点，并连接线段
set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget $\epsilon$', 'Interpreter', 'latex'); % LaTeX格式的横坐标标签
ylabel('Mean Square Error');
set(gca, 'FontSize', 16);
grid on;
box on;
legend show; % 显示图例
legend('Location', 'NorthEast', 'FontSize', 14);
% 设置x轴刻度和标签
xticks(0:0.1:1.5); % 设置刻度位置
xticklabels({'0', '', '', '','', '0.5', '', '', '','', '1', '', '', '','', '1.5'}); % 设置对应的标签
set(h1, 'LineWidth', 2, 'MarkerSize', 12); % 调整线条宽度和标记大小
set(h2, 'LineWidth', 2, 'MarkerSize', 12);
%set(gca, 'XTickLabel', get(gca, 'XTickLabel'), 'FontSize', 14); % 设置x轴刻度标签字体大小
%set(gca, 'YTickLabel', get(gca, 'YTickLabel'), 'FontSize', 14); % 设置y轴刻度标签字体大小
%title('(a) Adult Dataset', 'FontName', 'Times New Roman', 'FontSize', 18,'position',[0.750001272771295,-0.00075,1.4e-14]);
text(0.75, -0.00083, '(a) Adult Dataset', 'HorizontalAlignment', 'center', 'FontWeight', 'bold','FontSize', 18, 'FontName', 'Times New Roman');
% 第二个子图 - (b) Diabetes Dataset
subplot(1, 2, 2); % 创建1x2网格的第二个子图
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1), pos(2)+y_offset , 0.236220472440945,0.332753710261639]);  % 只修改y轴位置

h1 = plot(epsilon, MSE_RR2, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'RR'); % 使用圆圈标记点，并连接线段
hold on;
h2 = plot(epsilon, MSE_ARR2, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'ARR'); % 使用正方形标记点，并连接线段
set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget $\epsilon$', 'Interpreter', 'latex'); % LaTeX格式的横坐标标签
ylabel('Mean Square Error');
set(gca, 'FontSize', 16);
grid on;
box on;
legend show; % 显示图例
legend('Location', 'NorthEast', 'FontSize', 14);
set(h1, 'LineWidth', 2, 'MarkerSize', 12); % 调整线条宽度和标记大小
set(h2, 'LineWidth', 2, 'MarkerSize', 12);
% 设置x轴刻度和标签
xticks(0:0.1:1.5); % 设置刻度位置
xticklabels({'0', '', '', '','', '0.5', '', '', '','', '1', '', '', '','', '1.5'}); % 设置对应的标签
%yticks(0:0.0005:0.002);
%ylim([0 0.002]); % 确保y轴的上限至少为0.002
%yticklabels({'0', '0.0005', '0.001', '0.0015', '0.002', }) % 设置y轴刻度标签
text(0.75, -0.000165, '(b) Diabetes Dataset', 'HorizontalAlignment', 'center', 'FontWeight', 'bold','FontSize', 18, 'FontName', 'Times New Roman');
%title('(b) Diabetes Dataset', 'FontName', 'Times New Roman', 'FontSize', 18,'position',[0.746502570538426,-0.000155,0]);