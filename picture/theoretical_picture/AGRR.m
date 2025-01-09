% Create a new figure window
figure;

% Plot the first graph
subplot(2,2, 1,'position',[0.24,0.62,0.236220472440945,0.332753710261639]);
% Parameter settings
epsilon = 1;
beta = 0.01;
d = 8;
alpha_range = linspace(beta, 0.499999999, 100);
n = 1000;

% Before adjustment for GRR protocol
p_1 = exp(epsilon) / (exp(epsilon) + d - 1);
q_1 = 1 / (exp(epsilon) + d - 1);
var_before = (q_1 * (1 - q_1)) / (n * (p_1 - q_1)^2) + (1 - p_1 - q_1) / (d * n * (p_1 - q_1));

% After adjustment for GRR protocol
var_after = zeros(size(alpha_range));
for i = 1:length(alpha_range)
    alpha = alpha_range(i);
    p_2 = min(1, ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - d * alpha) - (1 - d * beta) * exp(epsilon)));
    q_2 = (1 - p_2) / (d - 1);
    var_after(i) = (q_2 * (1 - q_2)) / (n * (p_2 - q_2)^2) + ((1 - p_2 - q_2)) / (d * n * (p_2 - q_2));
end

% Define marker shapes
marker_shapes = { 'o', 's'};

% Plot the graph
plot(alpha_range, var_before * ones(size(alpha_range)), 'Color', [0.6235, 0, 0], 'LineWidth', 2, 'Marker', marker_shapes{1},'MarkerSize', 12, 'MarkerIndices', 1:15:numel(alpha_range));
hold on;
plot(alpha_range, var_after,'Color', [0.0, 0.227, 0.459], 'LineWidth', 2, 'Marker', marker_shapes{2}, 'MarkerSize', 12,'MarkerIndices', 1:15:numel(alpha_range));
set(gca, 'FontName', 'Times New Roman');
xlabel('Conditional Probability \alpha');
ylabel('Mean Squared Error');
set(gca, 'FontSize', 16);
legend('GRR', 'AGRR', 'FontName', 'Times New Roman','FontSize', 14,'position',[0.3578,0.835,0.0746,0.0609]);

% Set axis limits
xlim([beta, 0.5]);
ylim([0, 0.0035]);

% Add grid lines
grid on;

% Display the graph
title('(a) \alpha','HorizontalAlignment', 'center', 'FontWeight', 'bold','FontSize', 18, 'FontName', 'Times New Roman','position',[0.255000708562837,-0.00135,0]);
hold off;

% Plot the second graph
subplot(2, 2, 2,'position',[0.57,0.62,0.236220472440945,0.332753710261639]);
% Parameter settings
epsilon = 1;
alpha = 0.1;
d = 8;
beta_range = linspace(0.000001, alpha, 100000);
n = 1000;

% Before adjustment for GRR protocol
p_1 = exp(epsilon) / (exp(epsilon) + d - 1);
q_1 = 1 / (exp(epsilon) + d - 1);
var_before = (q_1 * (1 - q_1)) / (n * (p_1 - q_1)^2) + ((1 - p_1 - q_1)) / (d * n * (p_1 - q_1));

% After adjustment for GRR protocol
var_after = zeros(size(beta_range));
for i = 1:length(beta_range)
    beta = beta_range(i);
    p_2 = min(1, ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - d * alpha) - (1 - d * beta) * exp(epsilon)));
    q_2 = (1 - p_2) / (d - 1);
    var_after(i) = (q_2 * (1 - q_2)) / (n * (p_2 - q_2)^2) + ((1 - p_2 - q_2)) / (d * n * (p_2 - q_2));
end

% Define marker shapes
marker_shapes = { 'o', 's'};

% Plot the graph
plot(beta_range, var_before * ones(size(beta_range)), 'Color', [0.6235, 0, 0], 'LineWidth', 2, 'Marker', marker_shapes{1}, 'MarkerSize', 12, 'MarkerIndices', 1:20000:numel(beta_range));
hold on;
plot(beta_range, var_after, 'Color', [0.0, 0.227, 0.459],'LineWidth', 2, 'Marker', marker_shapes{2},  'MarkerSize', 12,'MarkerIndices', 1:20000:numel(beta_range));
set(gca, 'FontName', 'Times New Roman');
xticks(0:0.02:0.1);
xlabel('Conditional Probability \beta');
ylabel('Mean Squared Error');
set(gca, 'FontSize', 16);
legend('GRR', 'AGRR', 'FontName', 'Times New Roman','FontSize', 14,'Location','southeast');

% Set axis limits
xlim([0, alpha]);
ylim([0, 0.004]);

% Add grid lines
grid on;

% Display the graph
hold off;
title('(b) \beta','HorizontalAlignment', 'center', 'FontWeight', 'bold','FontSize', 18, 'FontName', 'Times New Roman','position',[0.050000278571667,-0.00155,0]);

% Plot the third graph
subplot(2, 2, 3,'position',[0.24,0.15,0.236220472440945,0.332753710261639]);
% Parameter settings
alpha = 0.1;
beta = 0.01;
d = 8;
epsilon_range = linspace(0.1, 3, 10000);
n = 1000;

% Before adjustment for GRR protocol
var_before = zeros(size(epsilon_range));
for i = 1:length(epsilon_range)
    epsilon = epsilon_range(i);
    p_1 = exp(epsilon) / (exp(epsilon) + d - 1);
    q_1 = 1 / (exp(epsilon) + d - 1);
    var_before(i) = (q_1 * (1 - q_1)) / (n * (p_1 - q_1)^2) + ((1 - p_1 - q_1)) / (d * n * (p_1 - q_1));
end

% After adjustment for GRR protocol
var_after = zeros(size(epsilon_range));
for i = 1:length(epsilon_range)
    epsilon = epsilon_range(i);
    p_2 = min(1, ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - d * alpha) - (1 - d * beta) * exp(epsilon)));
    q_2 = (1 - p_2) / (d - 1);
    var_after(i) = (q_2 * (1 - q_2)) / (n * (p_2 - q_2)^2) + ((1 - p_2 - q_2)) / (d * n * (p_2 - q_2));
end

% Define marker shapes
marker_shapes = { 'o', 's'};

% Plot the graph
plot(epsilon_range, var_before, 'Color', [0.6235, 0, 0], 'LineWidth', 2, 'Marker', marker_shapes{1},'MarkerSize', 12, 'MarkerIndices', 1:2000:numel(epsilon_range));
hold on;
plot(epsilon_range, var_after,'Color', [0.0, 0.227, 0.459], 'LineWidth', 2, 'Marker', marker_shapes{2},'MarkerSize', 12, 'MarkerIndices', 1:2000:numel(epsilon_range));
set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget \epsilon');
ylabel('Mean Squared Error');
set(gca, 'FontSize', 16);
legend('GRR', 'AGRR', 'FontName', 'Times New Roman','FontSize', 14);

% Set axis limits
xlim([0.1, 3]);
ylim([0, 0.7]);

% Add grid lines
grid on;
title('(c) \epsilon', 'HorizontalAlignment', 'center', 'FontWeight', 'bold','FontSize', 18, 'FontName', 'Times New Roman','position',[1.55000419494165,-0.27,0]);
hold off;

% Plot the fourth graph
subplot(2, 2, 4,'position',[0.57,0.15,0.236220472440945,0.332753710261639]);
% Parameter settings
epsilon = 1;
alpha = 0.1;
beta = 0.01;
d_range = 3:10;
n = 1000;

% Before adjustment for GRR protocol
var_before = zeros(size(d_range));
for i = 1:length(d_range)
    d = d_range(i);
    p_1 = exp(epsilon) / (exp(epsilon) + d - 1);
    q_1 = 1 / (exp(epsilon) + d - 1);
    var_before(i) = (q_1 * (1 - q_1)) / (n * (p_1 - q_1)^2) + ((1 - p_1 - q_1)) / (d * n * (p_1 - q_1));
end

% After adjustment for GRR protocol
var_after = zeros(size(d_range));
for i = 1:length(d_range)
    d = d_range(i);
    p_2 = min(1, ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - d * alpha) - (1 - d * beta) * exp(epsilon)));
    q_2 = (1 - p_2) / (d - 1);
    var_after(i) = (q_2 * (1 - q_2)) / (n * (p_2 - q_2)^2) + ((1 - p_2 - q_2)) / (d * n * (p_2 - q_2));
end

% Define marker shapes
marker_shapes = { 'o', 's'};

% Plot the graph
plot(d_range, var_before, 'Color', [0.6235, 0, 0], 'LineWidth', 2, 'Marker', marker_shapes{1}, 'MarkerSize', 12,'MarkerIndices', 1:1:numel(d_range));
hold on;
plot(d_range, var_after, 'Color', [0.0, 0.227, 0.459],'LineWidth', 2, 'Marker', marker_shapes{2}, 'MarkerSize', 12,'MarkerIndices', 1:1:numel(d_range));
set(gca, 'FontName', 'Times New Roman');
xlabel('Domain Size d');
ylabel('Mean Squared Error');
set(gca, 'FontSize', 16);
legend('GRR', 'AGRR', 'FontName', 'Times New Roman','FontSize', 14,'Location','northwest');

% Set axis limits
xlim([3, 10]);
ylim([0, 0.0045]);

% Add grid lines
grid on;
title('(d) d', 'HorizontalAlignment', 'center', 'FontWeight', 'bold','FontSize', 18, 'FontName', 'Times New Roman','position',[6.50001944786261,-0.0018,0]);

% Display the final graph
hold off;
