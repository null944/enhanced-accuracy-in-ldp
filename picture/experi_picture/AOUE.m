% Define the x-axis data
epsilon = [0.1, 0.2, 0.4, 0.8, 1.2, 1.5];
y_offset = 0.3;

MSE_OUE1 = [0.0089925,
0.0021976,
0.00054767,
0.00013279,
0.00005476,
0.00003219];
MSE_OUE2 = [0.001598439511139,
0.000408928622791,
0.000097411634451,
0.000023479406114,
0.000009637516118,
0.000005805523194];
MSE_AOUE1 = [0.00023524,
0.00005691,
0.00001192,
0.00000042,
0.00000023,
0.00000022];
MSE_AOUE2 = [0.000027539505492,
0.000006577790584,
0.000001111256849,
0.000000047031844,
0.000000043573145,
0.000000044635181];

% Create a new figure window
figure;

% First subplot - (a) Adult Dataset
subplot(1, 2, 1); % Create the first subplot in a 1x2 grid
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1)+0.07, pos(2) + y_offset, 0.236220472440945,0.332753710261639]);  % Only modify the y-axis position

h1 = plot(epsilon, MSE_OUE1, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'OUE'); % Use circle markers and connect them with lines
hold on;
h2 = plot(epsilon, MSE_AOUE1, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'AOUE'); % Use square markers and connect them with lines
set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget $\epsilon$', 'Interpreter', 'latex'); % X-axis label in LaTeX format
ylabel('Mean Square Error');
set(gca, 'FontSize', 16);
grid on;
box on;
legend show; % Display the legend
legend('Location', 'NorthEast', 'FontSize', 14);
% Set x-axis ticks and labels
xticks(0:0.1:1.5); % Set tick positions
xticklabels({'0', '', '', '','', '0.5', '', '', '','', '1', '', '', '','', '1.5'}); % Set corresponding labels
set(h1, 'LineWidth', 2, 'MarkerSize', 12); % Adjust line width and marker size
set(h2, 'LineWidth', 2, 'MarkerSize', 12);
%text for the subplot title
text(0.75, -0.0034, '(a) Adult Dataset', 'HorizontalAlignment', 'center','FontWeight', 'bold', 'FontSize', 18, 'FontName', 'Times New Roman');

% Second subplot - (b) Diabetes Dataset
subplot(1, 2, 2); % Create the second subplot in a 1x2 grid
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1), pos(2)+y_offset , 0.236220472440945,0.332753710261639]);  % Only modify the y-axis position

h1 = plot(epsilon, MSE_OUE2, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'OUE'); % Use circle markers and connect them with lines
hold on;
h2 = plot(epsilon, MSE_AOUE2, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'AOUE'); % Use square markers and connect them with lines
set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget $\epsilon$', 'Interpreter', 'latex'); % X-axis label in LaTeX format
ylabel('Mean Square Error');
set(gca, 'FontSize', 16);
grid on;
box on;
legend show; % Display the legend
legend('Location', 'NorthEast', 'FontSize', 14);
set(h1, 'LineWidth', 2, 'MarkerSize', 12); % Adjust line width and marker size
set(h2, 'LineWidth', 2, 'MarkerSize', 12);
% Set x-axis ticks and labels
xticks(0:0.1:1.5); % Set tick positions
xticklabels({'0', '', '', '','', '0.5', '', '', '','', '1', '', '', '','', '1.5'}); % Set corresponding labels
yticks(0:0.0005:0.002);
ylim([0 0.002]); % Ensure the upper limit of the y-axis is at least 0.002
%text for the subplot title
text(0.75, -0.00067, '(b) Diabetes Dataset', 'HorizontalAlignment', 'center','FontWeight', 'bold', 'FontSize', 18, 'FontName', 'Times New Roman');
