% Define the data for the x-axis
epsilon = [0.1, 0.2, 0.4, 0.8, 1.2, 1.5];
y_offset = 0.06;
y_offset1 = 0.03;
MSE_TCA = [0, 0, 0, 0, 0, 0];
MSE_TNA = [0.00006160, 0.00002058, 0.00000532, 0.00000010, 0, 0];
MSE_UCA = [0.00509962, 0.00092690, 0.00022104, 0.00004804, 0.00001593, 0.00001030];
MSE_UNA = [0.00317908, 0.00076557, 0.00021817, 0.00004491, 0.00002103, 0.00001235];
MSE_UCD = [0.00190095, 0.00040901, 0.00007474, 0.00001680, 0.00000669, 0.00000333];
MSE_UND = [0.00198519, 0.00041792, 0.00008660, 0.00002108, 0.00000671, 0.00000398];
MSE_BCA = [0.00920384, 0.00180633, 0.00051140, 0.00015182, 0.00006312, 0.00004749];
MSE_BNA = [0.01185255, 0.002134111, 0.00070734, 0.00017222, 0.00008331, 0.00006014];
MSE_TCD = [0, 0, 0, 0, 0, 0];
MSE_TND = [0.00020376, 0.00005936, 0.00001629, 0.00000242, 0.00000096, 0.00000065];
MSE_BCD = [0.00190614, 0.00034632, 0.00011432, 0.00002384, 0.00001251, 0.00000860];
MSE_BND = [0.00143139, 0.00035910, 0.00009255, 0.00001931, 0.00001053, 0.00000732];

% Create a new figure window
figure;

% First subplot - (a) Adult Dataset
subplot(2, 2, 1); 
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1)+0.07, pos(2) + y_offset, 0.236220472440945,0.332753710261639]);  % Modify only the y-axis position
h1 = plot(epsilon, MSE_BCA, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'BiSample'); % Circle markers
hold on;
h2 = plot(epsilon, MSE_TCA, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'TSP'); % Square markers
h3 = plot(epsilon, MSE_UCA, '-*', 'Color',[0.6039, 0.6039, 0.6039], 'DisplayName', 'UP', 'LineWidth', 2, 'MarkerSize', 12); % Star markers
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
xticklabels({'0', '', '', '', '', '0.5', '', '', '', '', '1', '', '', '', '', '1.5'}); % Set corresponding labels
text(0.75, -0.0031, '(a) Adult Dataset on MCAR', 'HorizontalAlignment', 'center', 'FontWeight', 'bold', 'FontSize', 16, 'FontName', 'Times New Roman');

% Second subplot - (b) Diabetes Dataset
subplot(2, 2, 2);
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1), pos(2) + y_offset, 0.236220472440945, 0.332753710261639]);  % Modify only the y-axis position
h1 = plot(epsilon, MSE_BNA, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'BiSample'); % Circle markers
hold on;
h2 = plot(epsilon, MSE_TNA, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'TSP'); % Square markers
h3 = plot(epsilon, MSE_UNA, '-*', 'Color',[0.6039, 0.6039, 0.6039], 'DisplayName', 'UP', 'LineWidth', 2, 'MarkerSize', 12); % Star markers

set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget $\epsilon$', 'Interpreter', 'latex');
ylabel('Mean Square Error');
set(gca, 'FontSize', 16);
grid on;
box on;
legend show;
legend('Location', 'NorthEast', 'FontSize', 14);
set(h1, 'LineWidth', 2, 'MarkerSize', 12);
set(h2, 'LineWidth', 2, 'MarkerSize', 12);

% Set x-axis ticks and labels
xticks(0:0.1:1.5);
xticklabels({'0', '', '', '', '', '0.5', '', '', '', '', '1', '', '', '', '', '1.5'});
yticks(0:0.002:0.014);
ylim([0 0.014]); 
text(0.75,-0.0045, '(b) Adult Dataset on MNAR', 'HorizontalAlignment', 'center', 'FontWeight', 'bold', 'FontSize', 16, 'FontName', 'Times New Roman');

% Third subplot - (c) Diabetes Dataset
subplot(2, 2,3);
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1)+0.07, pos(2) + y_offset1, 0.236220472440945, 0.332753710261639]);  % Modify only the y-axis position
h1 = plot(epsilon, MSE_BCD, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'BiSample');
hold on;
h2 = plot(epsilon, MSE_TCD, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'TSP');
h3 = plot(epsilon, MSE_UCD, '-*', 'Color',[0.6039, 0.6039, 0.6039], 'DisplayName', 'UP', 'LineWidth', 2, 'MarkerSize', 12);

set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget $\epsilon$', 'Interpreter', 'latex');
ylabel('Mean Square Error');
set(gca, 'FontSize', 16);
grid on;
box on;
legend show;
legend('Location', 'NorthEast', 'FontSize', 14);
set(h1, 'LineWidth', 2, 'MarkerSize', 12);
set(h2, 'LineWidth', 2, 'MarkerSize', 12);
text(0.75, -0.00064, '(c) Diabetes Dataset on MCAR', 'HorizontalAlignment', 'center', 'FontSize', 16, 'FontWeight', 'bold', 'FontName', 'Times New Roman');

% Fourth subplot - (d) Diabetes Dataset
subplot(2, 2, 4); 
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1), pos(2) + y_offset1, 0.236220472440945, 0.332753710261639]);  % Modify only the y-axis position

h1 = plot(epsilon, MSE_BND, '-o', 'Color', [0.6235, 0, 0], 'DisplayName', 'BiSample');
hold on;
h2 = plot(epsilon, MSE_TND, '-s', 'Color', [0.0, 0.227, 0.459], 'DisplayName', 'TSP');
h3 = plot(epsilon, MSE_UND, '-*', 'Color',[0.6039, 0.6039, 0.6039], 'DisplayName', 'UP', 'LineWidth', 2, 'MarkerSize', 12);

set(gcf, 'unit', 'centimeters', 'position', [1, 1, 7, 5.25]);
set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget $\epsilon$', 'Interpreter', 'latex');
ylabel('Mean Square Error');
set(gca, 'FontSize', 16);
grid on;
box on;
legend show;
legend('Location', 'NorthEast', 'FontSize', 14);
set(h1, 'LineWidth', 2, 'MarkerSize', 12);
set(h2, 'LineWidth', 2, 'MarkerSize', 12);

% Set x-axis ticks and labels
xticks(0:0.1:1.5);
xticklabels({'0', '', '', '', '', '0.5', '', '', '', '', '1', '', '', '', '', '1.5'});
ylim([0 0.0022]); 
text(0.75, -0.0007, '(d) Diabetes Dataset on MNAR', 'HorizontalAlignment', 'center', 'FontSize', 16, 'FontWeight', 'bold', 'FontName', 'Times New Roman');
