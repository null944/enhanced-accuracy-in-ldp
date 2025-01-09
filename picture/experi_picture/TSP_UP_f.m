% Define the x-axis data
epsilon = [0.1, 0.2, 0.4, 0.8, 1.2, 1.5];
y_offset = 0.04;
y_offset1 = 0.02;

MSE_TCA = [0.00138403, 0.00022833, 0.00006006, 0.00001666, 0.00000774, 0.00000400];
MSE_TNA = [0.00154140, 0.00041851, 0.00009148, 0.00001502, 0.00000738, 0.00000392];
MSE_UCA = [0.00427158, 0.00110616, 0.00025303, 0.00004888, 0.00001694, 0.00001170];
MSE_UNA = [0.00480576, 0.00106923, 0.00021789, 0.00004727, 0.00002067, 0.00001256];
MSE_TCD = [0.00089704, 0.00020235, 0.00004599, 0.00000833, 0.00000385, 0.00000191];
MSE_TND = [0.00158784, 0.00038858, 0.00007799, 0.00001335, 0.00000479, 0.00000223];
MSE_UCD = [0.00172467, 0.00044907, 0.00009700, 0.00001732, 0.00000679, 0.00000354];
MSE_UND = [0.00187432, 0.00046170, 0.00009826, 0.00001795, 0.00000624, 0.00000344];

% Create a new figure window
figure;

% First subplot - (a) Adult Dataset
subplot(2, 2, 1);
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1)+0.07, pos(2) + y_offset, 0.236220472440945,0.332753710261639]);  % Modify only the y-axis position
h1 = plot(epsilon, MSE_UCA, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'UP'); % Use circle markers and connect line segments
hold on;
h2 = plot(epsilon, MSE_TCA, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'TSP'); % Use square markers and connect line segments
set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget $\epsilon$', 'Interpreter', 'latex'); % LaTeX formatted x-axis label
ylabel('Mean Square Error');
set(gca, 'FontSize', 16);
grid on;
box on;
legend show; % Show legend
legend('Location', 'NorthEast', 'FontSize', 14);
% Set x-axis ticks and labels
xticks(0:0.1:1.5); % Set tick positions
xticklabels({'0', '', '', '','', '0.5', '', '', '','', '1', '', '', '','', '1.5'}); % Set corresponding labels
set(h1, 'LineWidth', 2, 'MarkerSize', 12); % Adjust line width and marker size
set(h2, 'LineWidth', 2, 'MarkerSize', 12);
text(0.75, -0.0015, '(a) Adult Dataset on MCAR', 'HorizontalAlignment', 'center','FontWeight', 'bold', 'FontSize', 16, 'FontName', 'Times New Roman');

% Second subplot - (b) Diabetes Dataset
subplot(2, 2, 2); % Create the second subplot in a 1x2 grid
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1), pos(2) + y_offset, 0.236220472440945,0.332753710261639]);  % Modify only the y-axis position
h1 = plot(epsilon, MSE_UNA, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'UP'); % Use circle markers and connect line segments
hold on;
h2 = plot(epsilon, MSE_TNA, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'TSP'); % Use square markers and connect line segments

set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget $\epsilon$', 'Interpreter', 'latex'); % LaTeX formatted x-axis label
ylabel('Mean Square Error');
set(gca, 'FontSize', 16);
grid on;
box on;
legend show; % Show legend
legend('Location', 'NorthEast', 'FontSize', 14);
set(h1, 'LineWidth', 2, 'MarkerSize', 12); % Adjust line width and marker size
set(h2, 'LineWidth', 2, 'MarkerSize', 12);

% Set x-axis ticks and labels
xticks(0:0.1:1.5); % Set tick positions
xticklabels({'0', '', '', '','', '0.5', '', '', '','', '1', '', '', '','', '1.5'}); % Set corresponding labels
text(0.75,-0.0015, '(b) Adult Dataset on MNAR', 'HorizontalAlignment', 'center', 'FontWeight', 'bold','FontSize', 16, 'FontName', 'Times New Roman');

subplot(2, 2, 3); 
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1)+0.07, pos(2) + y_offset1,0.236220472440945,0.332753710261639]);  % Modify only the y-axis position
h1 = plot(epsilon, MSE_UCD, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'UP'); % Use circle markers and connect line segments
hold on;
h2 = plot(epsilon, MSE_TCD, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'TSP'); % Use square markers and connect line segments
set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget $\epsilon$', 'Interpreter', 'latex'); % LaTeX formatted x-axis label
ylabel('Mean Square Error');
set(gca, 'FontSize', 16);
grid on;
box on;
legend show; % Show legend
legend('Location', 'NorthEast', 'FontSize', 14);

% Set x-axis ticks and labels
xticks(0:0.1:1.5); % Set tick positions
xticklabels({'0', '', '', '','', '0.5', '', '', '','', '1', '', '', '','', '1.5'}); % Set corresponding labels
set(h1, 'LineWidth', 2, 'MarkerSize', 12); % Adjust line width and marker size
set(h2, 'LineWidth', 2, 'MarkerSize', 12);
text(0.75, -0.00058, '(c) Diabetes Dataset on MCAR', 'HorizontalAlignment', 'center', 'FontSize',16,'FontWeight', 'bold', 'FontName', 'Times New Roman');

subplot(2, 2, 4); 
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1), pos(2) + y_offset1, 0.236220472440945,0.332753710261639]);  % Modify only the y-axis position

h1 = plot(epsilon, MSE_UND, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'UP'); % Use circle markers and connect line segments
hold on;
h2 = plot(epsilon, MSE_TND, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'TSP'); % Use square markers and connect line segments
set(gcf,'unit','centimeters','position',[1,1 ,7 ,5.25]);
set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget $\epsilon$', 'Interpreter', 'latex'); % LaTeX formatted x-axis label
ylabel('Mean Square Error');
set(gca, 'FontSize', 16);
grid on;
box on;
legend show; % Show legend
legend('Location', 'NorthEast', 'FontSize', 14);
set(h1, 'LineWidth', 2, 'MarkerSize', 12); % Adjust line width and marker size
set(h2, 'LineWidth', 2, 'MarkerSize', 12);

% Set x-axis ticks and labels
xticks(0:0.1:1.5); % Set tick positions
xticklabels({'0', '', '', '','', '0.5', '', '', '','', '1', '', '', '','', '1.5'}); % Set corresponding labels
ylim([0 0.002]); % Ensure the upper limit of the y-axis is at least 0.002
text(0.75, -0.00058, '(d) Diabetes Dataset on MNAR', 'HorizontalAlignment', 'center', 'FontSize', 16,'FontWeight', 'bold', 'FontName', 'Times New Roman');
