% Define the x-axis data
epsilon = [0.1, 0.2, 0.4, 0.8, 1.2, 1.5];
y_offset = 0.06;
y_offset2 = 0.03;

MSE_TCA = [0.01267198,
0.00209057,
0.00054993,
0.00015251,
0.00007089,
0.00003658];
MSE_TNA = [0.01380145,
0.00370556,
0.00080564,
0.00013644,
0.00006754,
0.00003588];

MSE_BCA = [0.02027753,
0.00367325,
0.00104235,
0.00028151,
0.00009512,
0.00008039];
MSE_BNA = [0.01885880,
0.00348992,
0.00078888,
0.00017268,
0.00012389,
0.00007604];

MSE_TCD = [0.00649544,
0.00158119,
0.00033066,
0.00005968,
0.00002484,
0.00001261];
MSE_TND = [0.01143104,
0.00280498,
0.00046486,
0.00007956,
0.00003028,
0.00001538];

MSE_BCD = [0.00292183,
0.00092573,
0.00019049,
0.00004761,
0.00002016,
0.00001880];
MSE_BND = [0.00345267,
0.00076654,
0.00020907,
0.00004659,
0.00002241,
0.00001271];

% Create a new figure window
figure;

% First subplot - (a) Adult Dataset on MCAR
subplot(2, 2, 1);
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1)+0.07, pos(2) + y_offset, 0.236220472440945,0.332753710261639]);  % Only modify the y-axis position

h1 = plot(epsilon, MSE_BCA, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'BiSample'); % Use circle markers and connect them with lines
hold on;
h2 = plot(epsilon, MSE_TCA, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'TSP'); % Use square markers and connect them with lines
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
text(0.75, -0.0079, '(a) Adult Dataset on MCAR', 'HorizontalAlignment', 'center','FontWeight', 'bold', 'FontSize', 16, 'FontName', 'Times New Roman');

% Second subplot - (b) Adult Dataset on MNAR
subplot(2, 2, 2);
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1), pos(2) + y_offset, 0.236220472440945,0.332753710261639]);  % Only modify the y-axis position

h1 = plot(epsilon, MSE_BNA, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'BiSample'); % Use circle markers and connect them with lines
hold on;
h2 = plot(epsilon, MSE_TNA, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'TSP'); % Use square markers and connect them with lines
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
text(0.75,-0.0063, '(b) Adult Dataset on MNAR', 'HorizontalAlignment', 'center', 'FontWeight', 'bold','FontSize', 16, 'FontName', 'Times New Roman');

% Third subplot - (c) Diabetes Dataset on MCAR
subplot(2, 2, 3);
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1)+0.07, pos(2) + y_offset2, 0.236220472440945,0.332753710261639]);  % Only modify the y-axis position

h1 = plot(epsilon, MSE_BCD, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'BiSample'); % Use circle markers and connect them with lines
hold on;
h2 = plot(epsilon, MSE_TCD, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'TSP'); % Use square markers and connect them with lines
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
text(0.75, -0.0025, '(c) Diabetes Dataset on MCAR', 'HorizontalAlignment', 'center', 'FontSize',16,'FontWeight', 'bold', 'FontName', 'Times New Roman');

% Fourth subplot - (d) Diabetes Dataset on MNAR
subplot(2, 2, 4);
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1), pos(2) + y_offset2, 0.236220472440945,0.332753710261639]);  % Only modify the y-axis position

h1 = plot(epsilon, MSE_BND, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'BiSample'); % Use circle markers and connect them with lines
hold on;
h2 = plot(epsilon, MSE_TND, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'TSP'); % Use square markers and connect them with lines
set(gcf,'unit','centimeters','position',[1,1 ,7 ,5.25]);
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
ylim([0 0.012]); % Ensure the upper limit of the y-axis is at least 0.012
text(0.75, -0.0038, '(d) Diabetes Dataset on MNAR', 'HorizontalAlignment', 'center', 'FontSize', 16,'FontWeight', 'bold', 'FontName', 'Times New Roman');
