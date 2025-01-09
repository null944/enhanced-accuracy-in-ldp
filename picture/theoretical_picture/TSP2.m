% Create a new figure window
figure;
% Plot the first graph
subplot(1, 2, 1);
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1) + 0.09, pos(2) + 0.28, 0.236220472440945, 0.332753710261639]);  % Modify only the y-axis position

% Parameter definitions
epsilon = 1;
delta = 0.1;
d = 4;
n = 1000; % Assume total sample size is 1000
n0 = n * delta;
ni = n * (1 - delta) / d;
% Define the range of p_2 values
p2_values = linspace(exp(epsilon) / (1 + exp(epsilon)), 1, 100);

% One-stage perturbation scheme calculation
p = exp(epsilon) / (exp(epsilon) + d);
q = 1 / (exp(epsilon) + d);
var_one_stage = q * (1 - q) / (n * (p - q)^2) + (1 - p - q) / ((d + 1) * n * (p - q));
var_one_nr = q * (1 - q) / (n * (p - q)^2) + (n0 * (1 - p - q)) / (n * n * (p - q));

% Initialize storage for the mean variance of the two-stage scheme
var_two_stage = zeros(size(p2_values));
var_two_nr = zeros(size(p2_values));

for i = 1:length(p2_values)
    p2 = p2_values(i);
    q2 = (1 - p2) / d;
    p1 = (exp(epsilon) * (p2 + d * q2 - 2 * q2) - q2 * (d - 1)) / ((d - 1 + exp(epsilon)) * (p2 - q2));
    q1 = (1 - p1) / (d - 1);
    % Calculate the missing value variance
    var_n0 = ((n * q2 * (1 - q2)) / ((p2 - q2)^2) + (n0 * (1 - p2 - q2)) / (p2 - q2)) / (n^2);
    % Calculate p^* and q^*
    p_star = p1 * p2 + (1 - p1) * q2;
    q_star = q1 * p2 + (1 - q1) * q2;
    
    % Calculate variance var(n_i / n)
    var_ni = ((ni * p_star * (1 - p_star) + n0 * q2 * (1 - q2) + (n - n0 - ni) * q_star * (1 - q_star)) / ((p_star - q_star)^2)) / (n^2);
    % Summarize the mean variance of the two-stage scheme
    var_two_stage(i) = (var_n0 + d * var_ni) / (d + 1);
    var_two_nr(i) = var_n0;
end

% Set axis limits
xlim([0.7, 1]);
%ylim([0, 0.0025]);

% Define marker shapes
marker_shapes = {'o', 's', '*', 'x'};

% Plot curves
plot(p2_values, var_one_stage * ones(size(p2_values)), 'LineWidth', 2, 'Color', [0.6235, 0, 0], 'Marker', marker_shapes{1}, 'MarkerSize', 12, 'MarkerIndices', 1:20:numel(p2_values));
hold on;
plot(p2_values, var_two_stage, 'LineWidth', 2, 'Color', [0.0, 0.227, 0.459], 'Marker', marker_shapes{2}, 'MarkerSize', 12, 'MarkerIndices', 1:20:numel(p2_values));
plot(p2_values, var_one_nr * ones(size(p2_values)), 'LineWidth', 2, 'Color', [0.9490, 0.6000, 0.2549], 'Marker', marker_shapes{3}, 'MarkerSize', 12, 'MarkerIndices', 1:20:numel(p2_values));
plot(p2_values, var_two_nr, 'LineWidth', 2, 'Color', [0.4314, 0.6706, 0.8314], 'Marker', marker_shapes{4}, 'MarkerSize', 12, 'MarkerIndices', 1:20:numel(p2_values));

% Plot vertical dashed line
alpha = exp(epsilon) / (1 + exp(epsilon));
x_line = alpha * ones(size(ylim));
line_color = [0.9290, 0.6940, 0.1250]; % Yellow
line(x_line, [0, var_one_stage], 'LineStyle', '--', 'Color', line_color, 'LineWidth', 1);

% Set axis labels and title
set(gca, 'FontName', 'Times New Roman');
xlabel('Missing Status Perturbation Probability p_2');
ylabel('Mean Squared Error');
set(gca, 'FontSize', 16);
legend('UP-f', 'TSP-f', 'UP-nr', 'TSP-nr', 'FontName', 'Times New Roman', 'FontSize', 14);

% Label the formula at the x-axis scale
formula_x = exp(epsilon) / (1 + exp(epsilon));
text(formula_x, -0.00026, '$$\frac{e^\epsilon}{1 + e^\epsilon}$$', 'Interpreter', 'latex', 'FontName', 'Times New Roman', 'Color', line_color, 'HorizontalAlignment', 'center', 'FontSize', 12);

% Set axis limits
xlim([0.7, 1]);
ylim([0, 0.0025]);

% Add grid lines
grid on;
box on;
title('(a) p_2', 'HorizontalAlignment', 'center', 'FontWeight', 'bold', 'FontSize', 18, 'FontName', 'Times New Roman', 'position', [0.85, -0.00105, 0]);
% Show the figure
hold off;

% Plot the second graph
subplot(1, 2, 2);
pos = get(gca, 'Position');
set(gca, 'Position', [pos(1), pos(2) + 0.28, 0.236220472440945, 0.332753710261639]);  % Modify only the y-axis position
epsilon = 1;

d = 4;
delta_range = linspace(0, 0.2, 100000);
n = 1000;

% One-stage perturbation scheme
p = exp(epsilon) / (exp(epsilon) + d);
q = 1 / (exp(epsilon) + d);
var_one_stage = zeros(size(delta_range));
for i = 1:length(delta_range)
    var = q * (1 - q) / (n * (p - q)^2) + (1 - p - q) / ((d + 1) * n * (p - q));
    var_one_stage(i) = var;
end
var_one_nr = zeros(size(delta_range));
var_two_nr = zeros(size(delta_range));
% Define marker shapes
marker_shapes = {'^', 'o', 's'};

% Two-stage perturbation scheme
p2 = 0.85;
q2 = (1 - p2) / d;
p1 = (exp(epsilon) * (p2 + d * q2 - 2 * q2) - q2 * (d - 1)) / ((d - 1 + exp(epsilon)) * (p2 - q2));
q1 = (1 - p1) / (d - 1);

for i = 1:length(delta_range)
    delta = delta_range(i);
    n0 = n * delta;
    ni = (n - n0) / d;
    var_n0_one = q * (1 - q) / (n * (p - q)^2) + (n0 * (1 - p - q)) / (n * n * (p - q));
    var_one_nr(i) = var_n0_one;
    var_n0 = ((n * q2 * (1 - q2)) / ((p2 - q2)^2) + (n0 * (1 - p2 - q2)) / (p2 - q2)) / (n^2);
    % Calculate p^* and q^*
    p_star = p1 * p2 + (1 - p1) * q2;
    q_star = q1 * p2 + (1 - q1) * q2;
    
    % Calculate variance var(n_i / n)
    var_ni = ((ni * p_star * (1 - p_star) + n0 * q2 * (1 - q2) + (n - n0 - ni) * q_star * (1 - q_star)) / ((p_star - q_star)^2)) / (n^2);
    var = (var_n0 + var_ni * d) / (d + 1);
    var_two_stage(i) = var;
    var_two_nr(i) = var_n0;
end
% Define marker shapes
marker_shapes = {'o', 's', '*', 'x'};
% One-stage perturbation scheme plot
plot(delta_range, var_one_stage, 'Marker', marker_shapes{1}, 'Color', [0.6235, 0, 0], 'MarkerSize', 12, 'MarkerIndices', 1:20000:numel(delta_range), 'LineWidth', 2);
hold on;
% Two-stage perturbation scheme plot
plot(delta_range, var_two_stage, 'Marker', marker_shapes{2}, 'Color', [0.0, 0.227, 0.459], 'MarkerSize', 12, 'MarkerIndices', 1:20000:numel(delta_range), 'LineWidth', 2);
plot(delta_range, var_one_nr, 'Marker', marker_shapes{3}, 'Color', [0.9490, 0.6000, 0.2549], 'MarkerSize', 12, 'MarkerIndices', 1:20000:numel(delta_range), 'LineWidth', 2);
plot(delta_range, var_two_nr, 'Marker', marker_shapes{4}, 'Color', [0.4314, 0.6706, 0.8314], 'MarkerSize', 12, 'MarkerIndices', 1:20000:numel(delta_range), 'LineWidth', 2);
set(gca, 'FontName', 'Times New Roman');
xlabel('Missing Rate \delta');
ylabel('Mean Squared Error');
set(gca, 'FontSize', 16);
legend('UP-f', 'TSP-f', 'UP-nr', 'TSP-nr', 'FontName', 'Times New Roman', 'FontSize', 14);

% Set axis limits
xlim([0, 0.2]);
ylim([0, max([var_one_stage, var_two_stage]) * 1.1]);

% Add grid lines
grid on;
title('(b) \delta', 'HorizontalAlignment', 'center', 'FontWeight', 'bold', 'FontSize', 18, 'FontName', 'Times New Roman', 'position', [0.1, -0.00095, 0]);
% Show the figure
hold off;
