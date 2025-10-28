% Define the data for the x-axis
epsilon = [0.1, 0.2, 0.4, 0.8, 1.2, 1.5];
y_offset = 0.3;

% Assume these are the MSE values for GRR and AGRR
MSE_GRR1 = [0.1965842, 0.0447661, 0.0090986, 0.0015148, 0.0004247, 0.0001923]; 
MSE_GRR2 = [0.031760556705193, 0.007218287648707, 0.001515723892598, 0.000234730960747, 0.000067819512593, 0.000031017595751]; 
MSE_AGRR1 = [0, 0, 0, 0, 0, 0]; 
MSE_AGRR2 = [0.000015189061620, 0.000002480891711, 0.000000269088775, 0.000000000411993, 0.000000000160937, 0.000000000073248]; 

% Create a new figure window
figure;

% First subplot - (a) Adult Dataset
subplot(1, 2, 1); % Create first subplot in 1x2 grid
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1)+0.07, pos(2) + y_offset, 0.236220472440945, 0.332753710261639]);  % Adjust y-axis position

h1 = plot(epsilon, MSE_GRR1, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'GRR'); % Use circle markers with connecting lines
hold on;
h2 = plot(epsilon, MSE_AGRR1, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'AGRR'); % Use square markers with connecting lines
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
xticklabels({'0', '', '', '', '', '0.5', '', '', '', '', '1', '', '', '', '', '1.5'}); % Set corresponding labels
set(h1, 'LineWidth', 2, 'MarkerSize', 12); % Adjust line width and marker size
set(h2, 'LineWidth', 2, 'MarkerSize', 12);
% Title for subplot (a)
text(0.75, -0.048, '(a) Adult Dataset', 'HorizontalAlignment', 'center', 'FontSize', 18, 'FontWeight', 'bold', 'FontName', 'Times New Roman');

% Second subplot - (b) Diabetes Dataset
subplot(1, 2, 2); % Create second subplot in 1x2 grid
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1), pos(2)+y_offset, 0.236220472440945, 0.332753710261639]);  % Adjust y-axis position
h1 = plot(epsilon, MSE_GRR2, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'GRR'); % Use circle markers with connecting lines
hold on;
h2 = plot(epsilon, MSE_AGRR2, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'AGRR'); % Use square markers with connecting lines
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
xticklabels({'0', '', '', '', '', '0.5', '', '', '', '', '1', '', '', '', '', '1.5'}); % Set corresponding labels
% Set y-axis ticks and labels
yticklabels({'0', '0.01', '0.02', '0.03', '0.035'}) % Set y-axis tick labels
ylim([0, 0.035])
% Title for subplot (b)
text(0.75, -0.0085, '(b) Diabetes Dataset', 'HorizontalAlignment', 'center', 'FontWeight', 'bold', 'FontSize', 18, 'FontName', 'Times New Roman');